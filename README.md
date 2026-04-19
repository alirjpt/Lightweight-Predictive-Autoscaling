# Predictive Autoscaling in Cloud Systems using ARIMA

## Overview

This project implements a lightweight predictive autoscaling system for cloud environments using time-series forecasting. The system uses ARIMA (Autoregressive Integrated Moving Average) to predict future workload demand and dynamically adjust resource scaling decisions.

Unlike traditional reactive autoscaling, which responds after workload changes occur, this approach anticipates future demand and enables proactive resource allocation.

---

## Problem Statement

Reactive autoscaling methods trigger scaling actions only after workload thresholds are exceeded. This often results in delayed responses, resource shortages, and degraded system performance.

This project aims to solve this problem by introducing a predictive autoscaling mechanism that forecasts workload demand and scales resources in advance.

---

## Methodology

### 1. Workload Forecasting

* Model: ARIMA (2,1,2)
* Predicts future workload demand based on historical data
* Forecast horizon: 12 time steps

### 2. Dynamic Threshold Mechanism

* Threshold = 0.85 × mean(predicted demand)
* Enables adaptive scaling based on workload trends

### 3. Scaling Strategies

* **Reactive Scaling**: Based on actual demand
* **Predictive Scaling**: Based on forecasted demand

---

## Experimental Setup

* Dataset: Time-series workload dataset
* Training/Test split: Last 12 values used for testing
* Metrics:

  * MAE (Mean Absolute Error)
  * RMSE (Root Mean Square Error)

---

## Results

* MAE: 41.83
* RMSE: 55.22

### Scaling Comparison:

* Reactive Scaling Actions: 10
* Predictive Scaling Actions: 12
* Missed Scaling Events (Reactive): [1, 10]

### Key Insight:

Predictive autoscaling captures workload changes more consistently and avoids missed scaling events observed in reactive approaches.

---

## Visualization

![Autoscaling Result](results/autoscaling_result.png)

---

## Key Contributions

* Lightweight predictive autoscaling using ARIMA
* Dynamic threshold-based scaling mechanism
* Comparative analysis of reactive vs predictive scaling
* Identification of missed scaling events

---

## How to Run

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the experiment

```
python src/arima_experiment.py
```

---

## Future Work

* Integration with real cloud platforms (e.g., Kubernetes)
* Use of advanced models (LSTM, Prophet)
* Real-time autoscaling implementation

---

## Author

Ali Nawaz

---

## License

This project is open-source and available under the MIT License.
