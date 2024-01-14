import requests
from bs4 import BeautifulSoup
import json
import re

class DailyWeatherData:
    """
    Return weather forecast data for one day 
    """

    def dailyData(self, city='', data_location=0, day=1):
        
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        link = f"https://www.accuweather.com/pt/br/{city}/{data_location}/daily-weather-forecast/{data_location}?day={day}"
        
        print(link)
        
        requisicao = requests.get(link, headers=headers)
        site = BeautifulSoup(requisicao.text, "html.parser")
        # print(site.prettify())
        
        data = site.find('span', class_="short-date")
        precipitacao_list = site.find_all("p", class_="panel-item")
        temperature_previsao = site.find('div', class_="row first")
        phrase_forecast_day = site.find_all("div", class_="phrase")

        # Filtrar os itens que contêm "Precipitação"
        itens_precipitacao = [item for item in precipitacao_list if "Precipitação" in item]

        # Imprimir os itens filtrados
        # for item in itens_precipitacao:
        #     print(item)
        
#-------------------------------------------------------------------------------------------
# trata a mensagem de previsão do dia 
        conteudos = [div.text for div in phrase_forecast_day]
        
        nebulosidade_dia = ''
        nebulosidade_noite = ''
        
        if conteudos is not None:
            nebulosidade_dia = conteudos[0]
            
            if len(conteudos) > 1:
                nebulosidade_noite = conteudos[1]
            else:
                nebulosidade_noite = ''
# -------------------------------------------------------------------------------------------    
# trata os valores de temperatura 
        temperatures = []
        if temperature_previsao:
            temperatures = temperature_previsao.find_all('div', class_='temperature')
# -------------------------------------------------------------------------------------------
# pega os valores de precipitação do dia
        valores_spans = []

        for item_html in itens_precipitacao:
            # Faz o parsing do HTML usando BeautifulSoup
            soup = BeautifulSoup(str(item_html), 'html.parser')
            
            # Encontra o span dentro do elemento
            span = soup.find('span', {'class': 'value'})
            
            # Se encontrou o span, adiciona o conteúdo à lista
            if span:
                valores_spans.append(span.text)
            
        consulta_dia = {}
        
        if data is not None:

            mm_manha = float(valores_spans[0].split()[0])
            
            if len(valores_spans) > 1:
                mm_tarde = float(valores_spans[1].split()[0])
            else:
                mm_tarde = 0
            
            # criação do objeto            
            consulta_dia = {
                "dia": data.text.strip(),
                "mm_manha": mm_manha,
                "mm_tarde": mm_tarde,
                "mm_dia": float(format(mm_manha + mm_tarde, '.1f')),
                "temp_max": int(re.sub(r'°', '', temperatures[0].text)),
                "temp_min": int(re.sub(r'°', '', temperatures[1].text)),
                "unidade": "°C",
                "nebulosidade_dia": nebulosidade_dia,
                "nebulosidade_noite": nebulosidade_noite
            }

        return consulta_dia
