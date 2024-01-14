import requests
from bs4 import BeautifulSoup
import json

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
        pesquisa = site.find_all("p", class_="panel-item")

        # Filtrar os itens que contêm "Precipitação"
        itens_precipitacao = [item for item in pesquisa if "Precipitação" in item]

        # Imprimir os itens filtrados
        # for item in itens_precipitacao:
        #     print(item)

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

            mm_manha = valores_spans[0].split()[0]
            
            if len(valores_spans) > 1:
                mm_tarde = valores_spans[1].split()[0]
            else:
                mm_tarde = 0
            
            # criação do objeto            
            consulta_dia = {
                "dia": data.text.strip(),
                "mm_manha": mm_manha,
                "mm_tarde": mm_tarde,
                "mm_dia": format(float(mm_manha) + float(mm_tarde), '.1f'),
            }

        return consulta_dia
