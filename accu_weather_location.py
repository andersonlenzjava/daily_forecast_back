from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import re
import time

class LocationCity:
    
    def cityLocation(self, city='', state=''):

        servico_crome = Service(ChromeDriverManager().install())
        opcoes_chrome = Options()
        opcoes_chrome.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        opcoes_chrome.add_argument("--headless=new")
        # Inicializa o driver do Chrome usando webdriver_manager 
        navegador = webdriver.Chrome(service=servico_crome, options=opcoes_chrome)

        url = "https://www.accuweather.com/"

        # Abre o site
        navegador.get(url)
        time.sleep(1)

        # pega o campo de pesquisa e realiza a pesquisa
        campo_pesquisa = navegador.find_element("css selector", "input.search-input")
        campo_pesquisa.send_keys(f"{city},{state}")
        campo_pesquisa.send_keys(Keys.ENTER)
        time.sleep(1)
        print("URL da página redirecionada:", navegador.current_url)

        data_location = 0
        data_location_url = 0
        data_location_ahref = 0

        # Pegar URL ---------------------------------------------------------------------------
        try:
            pattern = r'/(\d+)/weather-forecast/\d+'
            match = re.search(pattern, navegador.current_url)
            numero_extraido = match.group(1) if match else None
            print("Número extraído:", numero_extraido)
            data_location_url = numero_extraido
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        # Se tiver mais de um resultado pega o primeiro ---------------------------------------
        site = BeautifulSoup(navegador.page_source, "html.parser")
        try:
            div_locations_list = site.find('div', class_='locations-list')

                # TRATAR PARA VER SE PODE SER NONE
            if div_locations_list:
                tags_a = div_locations_list.find_all('a') # type: ignore
                print(tags_a[0].get('href'))
                
                if tags_a:
                    pattern = r'\bkey=([^&]*)'
                    match = re.search(pattern, tags_a[0].get('href'))
                    valor_da_key = match.group(1) if match else None
                    print("Valor da chave 'key':", valor_da_key)
                    data_location_ahref = valor_da_key
                    print("href", data_location_ahref)
                
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        # Conforme o tipo de retorna pega um ou outro data_location -------------------------
        try:
            if data_location_url != 0:
                data_location = data_location_url
            if data_location_ahref != 0:
                data_location = data_location_ahref
                
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
                
        # Fecha o navegador
        navegador.quit()
        
        return data_location
    