from src.service.Accu_Wheater_Forecast.accu_weather_daily import DailyWeatherData
from src.service.Accu_Wheater_Forecast.accu_weather_location import LocationCity


class cityDaysForecast:
    
    def daysForecast(self, city='', state='', days=1):
    
        # pegar o data location da cidade
        data_location = 0
        try: 
            data_location = LocationCity().cityLocation(city=city, state=state)
            print(data_location)
            
            if data_location is None:
                return {}
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        # pegar as previsões de chuva e o dia

        day_forecast_list = []
        
        print(days)
        
        for i in range(1, days + 1):
            print(i)
            
            try:
                data = DailyWeatherData().dailyData(
                        city=city, 
                        data_location=data_location, 
                        day=i)

                day_forecast_list.append(data)

            except Exception as e:
                print(f"Ocorreu um erro: {e}")
                
        # print(day_forecast_list)
    
        return {
            "city": city,
            "state": state,
            "daily_forecast": day_forecast_list
        }
        
