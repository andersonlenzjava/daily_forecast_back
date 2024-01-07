from accu_weather_daily import DailyWeatherData
from accu_weather_location import LocationCity


class cityDaysForecast:
    
    def daysForecast(self, city='', state='', days=1):
    
        # pegar o data location da cidade
        data_location = 0
        try: 
            data_location = LocationCity().cityLocation(city=city, state=state)
            print(data_location)
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        # pegar as previsões de chuva e o dia

        day_forecast_list = []
        
        for i in range(days):
            
            try:
                data = DailyWeatherData().dailyData(
                        city='Missal', 
                        data_location=2308465, 
                        day=i)

                day_forecast_list.append(data)

                print(data)
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
                
        print(day_forecast_list)
    
        return {
            "city": city,
            "State": state,
            "Daily_forecast": day_forecast_list
        }
        
