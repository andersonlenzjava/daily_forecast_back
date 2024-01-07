from city_days_forecast import cityDaysForecast

try:
    forecast = cityDaysForecast().daysForecast(city="Erec", state="Rio Grande do Sul", days=10)
    print(forecast)
except Exception as e:
            print(f"Ocorreu um erro: {e}")