import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
from fastapi import HTTPException


def scrapping_broadcast():

    print('iniciando a request em broadcast')
    url = 'http://broadcast.com.br'
    
    try:
        result = requests.get(url)
        #time.sleep(5)
        print(f'request finalizada. StatusCode: {result.status_code}')
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'Internal error on request broadcast. Error: {ex}')

    soup = BeautifulSoup(result.text, 'html.parser')
    tabela = soup.find_all('div', class_ = 'materia')

    if tabela == []:
        raise Exception('find noticias retornou vazio')

    data = []

    for i in tabela:
        titulo = i.a.get_text()
        link = i.a.get('href')
        url_noticia = url+link

        print(f'Titulo de notícia: {titulo}\nLink: {url_noticia}')

        try:
            result_noticia = requests.get(url_noticia)
            #time.sleep(3)
            print(f'request finalizada. StatusCode: {result_noticia.status_code}')
        except Exception as ex:
            raise HTTPException(status_code=500, detail=f'Internal error on request broadcast. Error: {ex}')

        soup_noticia = BeautifulSoup(result_noticia.text, 'html.parser')
        tabela_noticia = soup_noticia.find('div', class_= 'integra-materia')
        tabela_noticia_tratada = tabela_noticia.text.replace('\n','')

        if tabela_noticia == []:
            raise Exception('find noticia retornou vazio')

        data_hora = soup_noticia.find('div', class_='data_hora')

        if data_hora == []:
            raise Exception('find de data retornou vazio') 
        try:
            response = {
                'titulo': titulo,
                'url_noticia': url_noticia,
                'data_hora': data_hora.text,
                'noticia': tabela_noticia_tratada
            }

            data.append(response)
        except Exception as ex:
            print(ex)
    
    return data