from city_days_forecast import cityDaysForecast

try:
    forecast = cityDaysForecast().daysForecast(city="Missal", state="Paraná", days=23)
    print(forecast)
except Exception as e:
            print(f"Ocorreu um erro: {e}")