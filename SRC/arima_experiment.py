import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv("workload_timeseries.csv")
data.columns = ["time", "demand"]

# Split data into training and testing
train = data["demand"][:-12]
test = data["demand"][-12:]

# Train ARIMA model
model = ARIMA(train, order=(2,1,2))
model_fit = model.fit()

# Forecast future demand
forecast = model_fit.forecast(steps=12)

# ---- Dynamic Threshold ----
dynamic_threshold = np.mean(forecast) * 0.85

# ---- Accuracy Evaluation ----
mae = mean_absolute_error(test, forecast)
rmse = np.sqrt(((test - forecast) ** 2).mean())

print("\nForecast Accuracy:")
print("MAE:", mae)
print("RMSE:", rmse)

# ---- Reactive vs Predictive Scaling ----
print("\nReactive vs Predictive Scaling Comparison")

reactive_actions = []
predictive_actions = []

for actual, predicted in zip(test, forecast):

    # Reactive scaling
    if actual > dynamic_threshold:
        reactive_actions.append("Scale")
    else:
        reactive_actions.append("No Action")

    # Predictive scaling
    if predicted > dynamic_threshold:
        predictive_actions.append("Scale")
    else:
        predictive_actions.append("No Action")

print("\nReactive Scaling:", reactive_actions)
print("Predictive Scaling:", predictive_actions)

# ---- Scaling Delay Analysis ----
print("\n--- Scaling Delay Analysis ---")

reactive_times = []
predictive_times = []

for i, (actual, predicted) in enumerate(zip(test, forecast)):

    if actual > dynamic_threshold:
        reactive_times.append(i)

    if predicted > dynamic_threshold:
        predictive_times.append(i)

print("Reactive scaling triggered at steps:", reactive_times)
print("Predictive scaling triggered at steps:", predictive_times)

if reactive_times and predictive_times:
    delay = reactive_times[0] - predictive_times[0]
    print("\nScaling Delay (Reactive - Predictive):", delay)
else:
    print("\nNot enough scaling events to calculate delay")

# ---- NEW: Scaling Efficiency Analysis ----
print("\n--- Scaling Efficiency ---")

print("Total Reactive Scaling Actions:", len(reactive_times))
print("Total Predictive Scaling Actions:", len(predictive_times))

# Missed events (important research insight)
missed = [i for i in predictive_times if i not in reactive_times]
print("Missed Scaling Events by Reactive:", missed)

# ---- Predictive Scaling Decisions ----
print("\nDynamic Threshold:", dynamic_threshold)
print("\nPredictive Scaling Decisions:")

for i, value in enumerate(forecast):
    if value > dynamic_threshold:
        print(f"Step {i+1}: Scale UP")
    else:
        print(f"Step {i+1}: Maintain")

# ---- Plot Results ----
plt.plot(range(len(data)), data["demand"], label="Actual Workload")
plt.plot(range(len(train), len(train)+12), forecast, label="Predicted Workload")
plt.axhline(dynamic_threshold, linestyle="--", label="Dynamic Threshold")

plt.legend()
plt.title("Predictive Autoscaling using ARIMA Forecasting")
plt.xlabel("Time Step")
plt.ylabel("Workload Demand")

plt.savefig("autoscaling_result.png")
plt.show()