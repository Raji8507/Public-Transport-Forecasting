# Public Transport Passenger Forecasting

This project forecasts daily passenger journeys for different public transport services using historical data and Facebook Prophet. It helps analyze trends and predict future ridership for planning and operational decisions.

---

## Dataset

- **Source:** ACT Government Open Data  
- **Data Includes:** Daily passenger counts for Local Route, Light Rail, Peak Service, Rapid Route, and School Services.  
- **URL:** [ACT Government Transport Data](https://www.data.act.gov.au/Transport/Daily-Public-Transport-Passenger-Journeys-by-Servi/nkxy-abdj)

---

## Forecasting Approach

- **Model:** Facebook Prophet (time series forecasting)  
- **Features:**  
  - Handles missing data and outliers  
  - Captures seasonal patterns (weekly, yearly)  
  - Incorporates holidays and school breaks  
- **Key Parameters:**  
  - Changepoint Prior Scale: 0.05  
  - Seasonality Mode: Multiplicative

---
