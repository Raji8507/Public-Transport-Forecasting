import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
url = 'https://data.act.gov.au/resource/nkxy-abdj.csv'
data = pd.read_csv(url)
print(data.head())
data['ds'] = pd.to_datetime(data['date_column'])  
def prepare_data_for_service(df, service_col):
    df_service = df[['ds', service_col]].rename(columns={service_col: 'y'})
    df_service = df_service.set_index('ds').asfreq('D').reset_index()
    df_service['y'].fillna(method='ffill', inplace=True)  
    return df_service
local_route_df = prepare_data_for_service(data, 'Local_Route')
model = Prophet(weekly_seasonality=True, yearly_seasonality=False, daily_seasonality=False)
model.fit(local_route_df)
future = model.make_future_dataframe(periods=7)
forecast = model.predict(future)
model.plot(forecast)
plt.title('Local Route Passenger Forecast for Next 7 Days')
plt.show()
services = ['Local_Route', 'Light_Rail', 'Peak_Service', 'Rapid_Route', 'School']
for service in services:
    print(f"Forecasting for {service}")
    df_service = prepare_data_for_service(data, service)
    model = Prophet(weekly_seasonality=True, yearly_seasonality=False, daily_seasonality=False)
    model.fit(df_service)
    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)
    model.plot(forecast)
    plt.title(f'{service} Passenger Forecast for Next 7 Days')
    plt.show()
