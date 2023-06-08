import tkinter as tk
from tkinter import ttk
from threading import Thread
import time
import webbrowser
import subprocess
import pandas as pd
from selenium import webdriver
import tkinter as tk
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import pandas as pd
import numpy as np
import warnings
import tabulate
###
warnings.simplefilter(action='ignore', category=FutureWarning)

def funciones_extraccion():
    def funcion_isaac():
        municipios = {
            "Quintana Roo": 20,
            "Aguascalientes": 20,
            "Baja California": 10, 
            "Baja California Sur": 10, 
            "Campeche": 30,
            "Chiapas": 300,
            "Chihuahua": 120, 
            "Ciudad de Mexico": 30,
            "Coahuila": 80,
            "Colima": 20, 
            "Durango": 80, 
            "Guanajuato": 100,
            "Guerrero": 120,
            "Hidalgo": 120, 
            "Jalisco": 160, 
            "Estado de Mexico": 200,
            "Michoacan": 160,
            "Morelos": 60,
            "Nayarit": 40,
            "Nuevo Leon": 80,
            "Oaxaca": 800,
            "Puebla": 400,
            "Queretaro": 40,
            "San Luis Potosi": 90,
            "Sinaloa": 40, 
            "Sonora": 120,
            "Tabasco": 40,
            "Tamaulipas": 70,
            "Tlaxcala": 100,
            "Veracruz": 270, 
            "Yucatan": 160,
            "Zacatecas": 100     
                }

        estados = {
            "Estado de Mexico": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_del_Estado_de_México_(2021-2024)",
            "Aguascalientes": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Aguascalientes_(2021-2024)",
            "Baja California": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Baja_California_(2021-2024)",
            "Baja California Sur": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Baja_California_Sur_(2021-2024)",
            "Campeche": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Campeche_(2021-2024)",
            "Coahuila": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Coahuila_(2021-2024)",
            "Colima": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Colima_(2021-2024)",
            "Chiapas": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Chiapas_(2021-2024)",
            "Chihuahua": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Chihuahua_(2021-2024)",
            "Durango": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Durango_(2022-2025)",
            "Ciudad de Mexico": "https://es.wikipedia.org/wiki/Anexo:Alcaldes_de_la_Ciudad_de_M%C3%A9xico_(2021-2024)",
            "Guanajuato": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Guanajuato_(2021-2024)",
            "Guerrero": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Guerrero_(2021-2024)",
            "Hidalgo" :"https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Hidalgo_(2020-2024)",
            "Jalisco": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Jalisco_(2021-2024)",
            "Michoacan": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Michoac%C3%A1n_(2021-2024)",
            "Morelos": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Morelos_(2021-2024)",
            "Nayarit": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Nayarit_(2021-2024)",
            "Nuevo Leon": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Nuevo_Le%C3%B3n_(2021-2024)",
            "Oaxaca": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Oaxaca_(2022-2024)",
            "Puebla": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Puebla_(2021-2024)",
            "Queretaro": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Quer%C3%A9taro_(2021-2024)",
            "Quintana Roo": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Quintana_Roo_(2021-2024)",
            "San Luis Potosi": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_San_Luis_Potos%C3%AD_(2021-2024)",
            "Sinaloa": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Sinaloa_(2021-2024)",
            "Sonora": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Sonora_(2021-2024)",
            "Tabasco": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Tabasco_(2021-2024)",
            "Tamaulipas": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Tamaulipas_(2021-2024)",
            "Tlaxcala": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Tlaxcala_(2021-2024)",
            "Veracruz" : "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Veracruz_(2022-2025)",
            "Yucatan": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Yucat%C3%A1n_(2021-2024)",
            "Zacatecas": "https://es.wikipedia.org/wiki/Anexo:Presidentes_municipales_de_Zacatecas_(2021-2024)"
        }
        df = pd.DataFrame(columns=['Municipio', 'Presidente Municipal', 'Estado',"Gobernador","Partido"])

        def normalize(s):
            replacements = (
                ("á", "a"),
                ("é", "e"),
                ("í", "i"),
                ("ó", "o"),
                ("ú", "u"),
            )
            for a, b in replacements:
                s = s.replace(a, b).replace(a.upper(), b.upper())
            return s

        def webscraping(estados,municipios,df):
            enlace = "https://es.wikipedia.org/wiki/Anexo:Gobernantes_de_las_entidades_federativas_de_M%C3%A9xico"
            for i in estados:
                link = estados[i]
                #chrome_options = webdriver.ChromeOptions()
                #chrome_options.add_argument('window-size=1280,800')
                #driver = webdriver.Chrome("C:/Users/isaac/Desktop/WebScraping/chromedriver.exe")
                
                op = webdriver.ChromeOptions()
                op.add_argument('headless')
                driver = webdriver.Chrome(options=op)
                driver.get(link)
                time.sleep(1)
                print(i)
                for j in range(municipios[i]):
                    try:
                        mun_path = f"//table[@class='wikitable'][2]/tbody/tr[{j+1}]/td"
                        pre_path = f"//table[@class='wikitable'][2]/tbody/tr[{j+1}]/td[2]"
                        partido = f"//table[@class='wikitable'][2]/tbody/tr[{j+1}]/td[4]/a[2]"
                        #datos = driver.find_element(By.XPATH,'//table[@class="wikitable"][2]/tbody/tr/td/a').text
                        municipio = driver.find_element(By.XPATH,mun_path).text
                        presidente = driver.find_element(By.XPATH,pre_path).text
                        partido = driver.find_element(By.XPATH,partido).text
                        #(municipio,presidente)
                        municipio = normalize(municipio)
                        presidente = normalize(presidente)
                        df = df.append({
                            'Municipio': municipio,
                            'Estado': i,
                            'Presidente Municipal': presidente,
                            "Partido": partido,
                            },ignore_index=True)
                    except NoSuchElementException:
                        pass
            driver.get(enlace)
            time.sleep(1)
            try: 
                for j in range(32):
                    estado = f"//table[@class='wikitable sortable col6izq jquery-tablesorter'][1]/tbody/tr[{j+1}]/td[1]/a[2]"
                    gob_path = f"//table[@class='wikitable sortable col6izq jquery-tablesorter'][1]/tbody/tr[{j+1}]/td[4]"
                    estado =  driver.find_element(By.XPATH,estado).text
                    gob_path = driver.find_element(By.XPATH,gob_path).text
                    
                    estado = normalize(estado)
                    gob_path = normalize(gob_path)
                    df['Gobernador'] = df.apply(lambda x: gob_path if estado == x.Estado else x['Gobernador'],axis=1)
            except NoSuchElementException:
                        pass 
            df = df.rename(columns={"Presidente Municipal": "Municipal", "Gobernador":  "Gobernador"})
            for index, row in df.iterrows():
                if(pd.isnull(row["Municipal"])):
                    df.loc[row[index]-1, ['Municipal']] = row["Municipio"]
            df["Municipal"] = df["Municipal"].apply(lambda x: "".join(char for char in x if not char.isdigit()))
            df["Municipal"] = df["Municipal"].apply(lambda x: x.split("(")[0])
            df["Gobernador"] = df["Gobernador"].apply(lambda x: x.split("\n(")[0])
            df["Municipio"] = df["Municipio"].apply(lambda x: x.split("(")[0])
            df['Municipio'].replace('', np.nan, inplace=True)
            df['Municipal'].replace('', np.nan, inplace=True)
            dataframe = df.dropna()
            dataframe = dataframe[~dataframe["Municipio"].str.contains("Predecesor", case=False)]
            print(len(dataframe))
            dataframe.to_csv("Presidentes_Municipales.csv")
            
        
        
        webscraping(estados,municipios,df)
    #funcion_isaac()
    #funcion_jesus.funcion_final()
    # Crear los procesos
    #proceso_1 = multiprocessing.Process(target=funcion_isaac())
    #proceso_2 = multiprocessing.Process(target=funcion_jesus.funcion_final())


    def funcion_municipales():
        def funcion_yisus():
            # Inicializar el controlador de Selenium (requiere el controlador correspondiente al navegador que se utilice)
            op = webdriver.ChromeOptions()
            op.add_argument('headless')
            driver = webdriver.Chrome(options=op)
                
            #driver = webdriver.Chrome(r"C:/Users/52998/Desktop/Supervised Learning with scikit-learn/chromedriver.exe")

            # Acceder a la página de los diputados federales
            driver.get("https://web.diputados.gob.mx/inicio/tusDiputados/listadoDiputadosBuscador;nombre=;estado=;cabeceraMunicipal=;grupoParlamentario=")

            # Esperar hasta que los elementos deseados estén presentes en la página
            wait = WebDriverWait(driver, 20)
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//tr[contains(@class, "dx-data-row")]')))

            # Crear una lista para almacenar los datos de los diputados federales
            data_federales = []

            # Iterar sobre los elementos y extraer los datos de los diputados federales
            for element in elements:
                nombre = element.find_element(By.XPATH, './td[1]').text
                partido = element.find_element(By.XPATH, './td[2]').text
                estado = element.find_element(By.XPATH, './td[3]').text
                cabecera_municipal = element.find_element(By.XPATH, './td[4]').text
                
                # Agregar los datos a la lista de diputados federales
                data_federales.append([nombre, partido, estado, cabecera_municipal])

            # Crear un DataFrame con los datos de los diputados federales
            df_federales = pd.DataFrame(data_federales, columns=['Nombre', 'Partido', 'Estado', 'Cabecera Municipal'])

            # Guardar el DataFrame de diputados federales en un archivo CSV
            df_federales.to_csv('Diputados_Federales.csv', index=False)


            # Acceder a la página de los diputados municipales de Quintana Roo
            driver.get("https://es.wikipedia.org/wiki/Anexo:XVII_Legislatura_del_Congreso_del_Estado_de_Quintana_Roo#Diputados")

            # Esperar hasta que los elementos deseados estén presentes en la página
            wait = WebDriverWait(driver, 20)
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//table[@class="wikitable"]/tbody/tr[position()>1 and not(position()=last())]')))

            # Crear una lista para almacenar los datos de los diputados municipales
            # Lista de enlaces de los diputados municipales
            enlaces = [
                "https://es.wikipedia.org/wiki/Anexo:LXV_Legislatura_del_Congreso_del_Estado_de_Aguascalientes",
                "https://es.wikipedia.org/wiki/Anexo:XVI_Legislatura_del_Congreso_del_Estado_de_Baja_California_Sur",
                "https://es.wikipedia.org/wiki/Anexo:LXIX_Legislatura_del_Congreso_del_Estado_de_Durango",
                "https://es.wikipedia.org/wiki/Anexo:LXV_Legislatura_del_Congreso_del_Estado_de_Guanajuato",
                "https://es.wikipedia.org/wiki/Anexo:LXV_Legislatura_del_Congreso_de_Hidalgo",
                "https://es.wikipedia.org/wiki/Anexo:LXXV_Legislatura_del_Congreso_del_Estado_de_Michoac%C3%A1n",
                "https://es.wikipedia.org/wiki/Anexo:LV_Legislatura_del_Congreso_del_Estado_de_Morelos",
                "https://es.wikipedia.org/wiki/Anexo:XXXIII_Legislatura_del_Congreso_del_Estado_de_Nayarit",
                "https://es.wikipedia.org/wiki/Anexo:LXXVI_Legislatura_del_Congreso_del_Estado_de_Nuevo_Le%C3%B3n",
                "https://es.wikipedia.org/wiki/Anexo:LX_Legislatura_del_Congreso_del_Estado_de_Quer%C3%A9taro",
                "https://es.wikipedia.org/wiki/Anexo:XVII_Legislatura_del_Congreso_del_Estado_de_Quintana_Roo",
                "https://es.wikipedia.org/wiki/Anexo:II_Legislatura_del_Congreso_de_la_Ciudad_de_M%C3%A9xico",
                "https://es.wikipedia.org/wiki/Anexo:LXI_Legislatura_del_Congreso_del_Estado_de_M%C3%A9xico",
                "https://es.wikipedia.org/wiki/Anexo:LXIV_Legislatura_del_Congreso_de_Tabasco",
                "https://es.wikipedia.org/wiki/Anexo:LXIV_Legislatura_del_Congreso_del_Estado_de_Zacatecas",
                "https://es.wikipedia.org/wiki/Anexo:LX_Legislatura_del_Congreso_del_Estado_de_Colima",
                "https://es.wikipedia.org/wiki/Anexo:LXIII_Legislatura_del_Congreso_del_Estado_de_Yucat%C3%A1n"

            ]

            enlaces_4_municipales = [
                    "https://es.wikipedia.org/wiki/Anexo:XXIV_Legislatura_del_Congreso_del_Estado_de_Baja_California" ,
                    "https://es.wikipedia.org/wiki/Anexo:LXIV_Legislatura_del_Congreso_del_Estado_de_Campeche",
                    "https://es.wikipedia.org/wiki/Anexo:LXVIII_Legislatura_del_Congreso_del_Estado_de_Chiapas",
                    "https://es.wikipedia.org/wiki/Anexo:LXVII_Legislatura_del_Congreso_del_Estado_de_Chihuahua",
                    "https://es.wikipedia.org/wiki/Anexo:LXIII_Legislatura_del_Congreso_del_Estado_de_Guerrero",
                    "https://es.wikipedia.org/wiki/Anexo:LXIII_Legislatura_del_Congreso_del_Estado_de_Jalisco",
                    "https://es.wikipedia.org/wiki/Anexo:LXV_Legislatura_del_Congreso_del_Estado_de_Oaxaca",
                    "https://es.wikipedia.org/wiki/Anexo:LXI_Legislatura_del_Congreso_del_Estado_de_Puebla",
                    #"https://es.wikipedia.org/wiki/Anexo:LXI_Legislatura_del_Congreso_del_Estado_de_M%C3%A9xico",
                    "https://es.wikipedia.org/wiki/Anexo:LXIII_Legislatura_del_Congreso_del_Estado_de_San_Luis_Potos%C3%AD",
                    "https://es.wikipedia.org/wiki/Anexo:LXIV_Legislatura_del_Congreso_del_Estado_de_Sinaloa",
                    "https://es.wikipedia.org/wiki/Anexo:LXIII_Legislatura_del_Congreso_del_Estado_de_Sonora",
                    "https://es.wikipedia.org/wiki/Anexo:LXV_Legislatura_del_Congreso_del_Estado_de_Tamaulipas",
                    "https://es.wikipedia.org/wiki/Anexo:LXIV_Legislatura_del_Congreso_del_Estado_de_Tlaxcala",
                    "https://es.wikipedia.org/wiki/Anexo:LXVI_Legislatura_del_Congreso_del_Estado_de_Veracruz",
                    #"https://es.wikipedia.org/wiki/Anexo:LIV_Legislatura_del_Congreso_del_Estado_de_Colima",
                    "https://es.wikipedia.org/wiki/Anexo:LXII_Legislatura_del_Congreso_del_Estado_de_Coahuila"
                ]

            # Crear una lista para almacenar los datos de los diputados municipales
            data_municipales = []

            # Iterar sobre los enlaces y recopilar los datos de los diputados municipales
            for enlace in enlaces + enlaces_4_municipales:
                # Acceder al enlace
                driver.get(enlace)

                # Esperar hasta que los elementos deseados estén presentes en la página
                wait = WebDriverWait(driver, 20)

                if enlace == "https://es.wikipedia.org/wiki/Anexo:LXV_Legislatura_del_Congreso_de_Hidalgo":
                    # Utilizar una expresión XPath específica para la tabla en el enlace "https://es.wikipedia.org/wiki/Anexo:LXV_Legislatura_del_Congreso_de_Hidalgo"
                    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/center[1]/table[1]/tbody/tr[position()>1]')))
                    
                    # Iterar sobre los elementos y extraer los datos de los diputados municipales
                    for element in elements:
                        tds = element.find_elements(By.XPATH, './td')
                        if len(tds) >= 3:
                            distrito = tds[0].text.strip()
                            cabecera_municipal = "Sin datos"
                            diputado = tds[1].text.strip()
                            partido = "Sin datos"

                            # Agregar los datos a la lista de diputados municipales
                            data_municipales.append([distrito, cabecera_municipal, diputado, partido])

                elif enlace in enlaces_4_municipales:
                    # Agregar el partido para aquellos enlaces que no tienen la columna de suplente
                    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//table[@class="wikitable"]/tbody/tr[position()>1]')))
                    
                    # Iterar sobre los elementos y extraer los datos de los diputados municipales
                    for element in elements:
                        tds = element.find_elements(By.XPATH, './td')
                        if len(tds) >= 4:
                            distrito = tds[0].text.strip()
                            cabecera_municipal = tds[1].text.strip()
                            diputado = tds[2].text.strip()
                            partido = tds[4].text.strip()

                            # Agregar los datos a la lista de diputados municipales
                            data_municipales.append([distrito, cabecera_municipal, diputado, partido])

                elif enlace == "https://es.wikipedia.org/wiki/Anexo:LXV_Legislatura_del_Congreso_del_Estado_de_Guanajuato":
                    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//table[@class="wikitable"]/tbody/tr[position()>1]')))

                    for element in elements:
                        tds = element.find_elements(By.XPATH, './td')
                        if len(tds) >= 4:
                            distrito = tds[0].text.strip()
                            cabecera_municipal = "Sin datos"
                            diputado = tds[2].text.strip()
                            partido = tds[3].text.strip()

                            # Agregar los datos a la lista de diputados municipales
                            data_municipales.append([distrito, cabecera_municipal, diputado, partido])

                elif enlace == "https://es.wikipedia.org/wiki/Anexo:LXV_Legislatura_del_Congreso_del_Estado_de_Aguascalientes":
                    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//table[@class="wikitable"]/tbody/tr[position()>1]')))

                    for element in elements:
                        tds = element.find_elements(By.XPATH, './td')
                        if len(tds) >= 5:
                            distrito = tds[0].text.strip()
                            cabecera_municipal = tds[1].text.strip()
                            diputado = tds[2].text.strip()
                            partido = tds[4].text
                            
                            # Agregar los datos a la lista de diputados municipales
                            data_municipales.append([distrito, cabecera_municipal, diputado, partido])

                elif enlace == "https://es.wikipedia.org/wiki/Anexo:LXI_Legislatura_del_Congreso_del_Estado_de_M%C3%A9xico":
                    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//table[@class="wikitable"]/tbody/tr[position()>1]')))

                    for element in elements:
                        tds = element.find_elements(By.XPATH, './td')
                        if len(tds) >= 5:
                            distrito = tds[0].text.strip()
                            cabecera_municipal = tds[1].text.strip()
                            diputado = tds[2].text.strip()
                            partido = tds[3].text
                            
                            # Agregar los datos a la lista de diputados municipales
                            data_municipales.append([distrito, cabecera_municipal, diputado, partido])

                elif enlace == "https://es.wikipedia.org/wiki/Anexo:LXIV_Legislatura_del_Congreso_de_Tabasco":
                    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//table[@class="wikitable"]/tbody/tr[position()>1]')))

                    for element in elements:
                        tds = element.find_elements(By.XPATH, './td')
                        if len(tds) >= 5:
                            distrito = tds[0].text.strip()
                            cabecera_municipal = tds[1].text.strip()
                            diputado = tds[2].text.strip()
                            partido = tds[4].text
                            
                            # Agregar los datos a la lista de diputados municipales
                            data_municipales.append([distrito, cabecera_municipal, diputado, partido])

                elif enlace == "https://es.wikipedia.org/wiki/Anexo:LXIII_Legislatura_del_Congreso_del_Estado_de_Yucat%C3%A1n":
                    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//table[@class="wikitable"]/tbody/tr[position()>1]')))

                    for element in elements:
                        tds = element.find_elements(By.XPATH, './td')
                        if len(tds) >= 6:
                            distrito = tds[4].text.strip()
                            cabecera_municipal = tds[5].text.strip()
                            diputado = tds[2].text.strip()
                            partido = "Sin datos"
                            
                            # Agregar los datos a la lista de diputados municipales
                            data_municipales.append([distrito, cabecera_municipal, diputado, partido])

                else:
                    # Utilizar el formato estándar para las demás tablas
                    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//table[@class="wikitable"]/tbody/tr[position()>1]')))

                    # Iterar sobre los elementos y extraer los datos de los diputados municipales
                    for element in elements:
                        tds = element.find_elements(By.XPATH, './td')
                        if len(tds) >= 5:
                            distrito = tds[0].text.strip()
                            cabecera_municipal = tds[1].text.strip()
                            diputado = tds[2].text.strip()
                            partido = tds[5].text.strip()

                            # Agregar los datos a la lista de diputados municipales
                            data_municipales.append([distrito, cabecera_municipal, diputado, partido])

            # Cerrar el controlador de Selenium
            driver.quit()

            # Crear un DataFrame con los datos de los diputados municipales
            df_municipales = pd.DataFrame(data_municipales, columns=['Distrito', 'Cabecera Municipal', 'Diputado',"Partido"])
            
            df_municipales.replace('', np.nan, inplace=True)
            #df['Municipal'].replace('', np.nan, inplace=True)
            #dataframe = df.dropna()
            # Eliminar las filas con valores NaN
            df_municipales = df_municipales.dropna()

            # Guardar el DataFrame de diputados municipales en un archivo CSV
            #df_municipales.to_csv('Diputados_Municipales.csv', index=False)

            #Eliminamos nan
            #municipales = pd.read_csv("Diputados_Municipales.csv")
            df_municipales = df_municipales.dropna().reset_index(drop = True)
            return df_municipales
            # Imprimir el DataFrame de diputados municipales en formato tabular
            #print(tabulate(df_municipales, headers='keys', tablefmt='psql'))


        def transformacion(municipales):
            import pandas as pd
            import roman


            #municipales = pd.read_csv("Diputados_Municipales.csv")


            pd.set_option('display.max_rows', None)
            municipales = municipales.dropna().reset_index(drop = True)



            cabeceras_guanajuato = {49: 'Acámbaro',50: 'León Oriente',51: 'León Poniente',52: 'San Francisco del Rincón',53: 'Purísima del Rincón',54: 'Manuel Doblado',55: 'Celaya Poniente',56: 'Celaya Oriente',57: 'Salvatierra',58: 'Uriangato',59: 'Yuriria',60: 'Valle de Santiago',61: 'Moroleón',62: 'Cortazar',63: 'Jaral del Progreso',64: 'Irapuato Oriente',65: 'Irapuato Poniente',66: 'Abasolo',67: 'Pénjamo',68: 'Guanajuato',69: 'Silao',70: 'San Miguel de Allende',71: 'Dolores Hidalgo',72: 'San Felipe',73: 'Ocampo',74: 'San José Iturbide',75: 'Doctor Mora',76: 'Tierra Blanca',77: 'Victoria',78: 'Xichú',79: 'Atarjea',80: 'Santa Catarina',81: 'San Luis de la Paz',82: 'Guanajuato',83: 'Santa Cruz de Juventino Rosas',84: 'Celaya',85: 'Comonfort',86: 'Apaseo el Alto',87: 'Apaseo el Grande',88: 'Juventino Rosas'
            }

            for i in range(49, 71):
                municipales.at[i, 'Cabecera Municipal'] = cabeceras_guanajuato[i]

            cabeceras_hidalgo = {70: 'San Miguel de Allende',71: 'Dolores Hidalgo',72: 'San Felipe',73: 'Ocampo',74: 'San José Iturbide',75: 'Doctor Mora',76: 'Tierra Blanca',77: 'Victoria',78: 'Xichú',79: 'Atarjea',80: 'Santa Catarina',81: 'San Luis de la Paz',82: 'Guanajuato',83: 'Santa Cruz de Juventino Rosas',84: 'Celaya',85: 'Comonfort',86: 'Apaseo el Alto',87: 'Apaseo el Grande',88: 'Juventino Rosas'
            }

            for i in range(71, 89):
                municipales.at[i, 'Cabecera Municipal'] = cabeceras_hidalgo[i]

                
            diputados_hidalgo = {
                71: 'Partido Verde Ecologista',72: 'Partido Revolucionario Institucional',73: 'Nueva Alianza',74: 'Movimiento Regeneración Nacional',75: 'Partido del Trabajo',76: 'Partido Acción Nacional',77: 'Movimiento Regeneración Nacional',78: 'Partido Revolucionario Institucional',79: 'Partido de la Revolución Democrática',80: 'Movimiento Regeneración Nacional',81: 'Movimiento Regeneración Nacional',82: 'Partido Revolucionario Institucional',83: 'Partido del Trabajo',84: 'Partido Verde Ecologista',85: 'Partido del Trabajo',86: 'Movimiento Regeneración Nacional',87: 'Partido del Trabajo',88: 'Nueva Alianza'}

            for i in range(71, 89):
                municipales.at[i, 'Partido'] = diputados_hidalgo[i]

            partido_yucatan = {294: 'Partido Acción Nacional',295: 'Partido Acción Nacional',296: 'Partido Acción Nacional',297: 'Partido Acción Nacional',298: 'Partido Acción Nacional',299: 'Partido Acción Nacional',300: 'Partido Acción Nacional',301: 'Movimiento Regeneración Nacional',302: 'Partido Acción Nacional',303: 'Partido Acción Nacional',304: 'Partido Acción Nacional',305: 'Partido Acción Nacional',306: 'Partido Acción Nacional',307: 'Partido Acción Nacional',308: 'Partido Acción Nacional'}

            for i in range(294, 309):
                municipales.at[i, 'Partido'] = partido_yucatan[i]


            municipales = municipales.drop(index=range(287, 294))
            def normalize(s):
                replacements = (
                    ("á", "a"),
                    ("é", "e"),
                    ("í", "i"),
                    ("ó", "o"),
                    ("ú", "u"),
                )
                for a, b in replacements:
                    s = s.replace(a, b).replace(a.upper(), b.upper())
                return s
            #Estandarizar Distritos
            def convert_roman_to_int(value):
                if isinstance(value, str):
                    try:
                        return roman.fromRoman(value)
                    except roman.InvalidRomanNumeralError:
                        return value
                else:
                    return value

            # Aplicar la función a la columna 'Distrito'
            municipales['Distrito'] = municipales['Distrito'].apply(convert_roman_to_int)

            # Create a dictionary of states and their corresponding municipal heads
            states = {
            "Rincón de Romos": "Aguascalientes",
            "El Llano": "Aguascalientes",
            "Pabellón de Arteaga": "Aguascalientes",
            "San Francisco de los Romo": "Aguascalientes",
            "Aguascalientes": "Aguascalientes",
            "Jesús María": "Aguascalientes",
            "Calvillo": "Aguascalientes",
            "San José del Cabo": "Baja California Sur",
            "La Paz": "Baja California Sur",
            "Cabo San Lucas": "Baja California Sur",
            "Ciudad Constitución": "Baja California Sur",
            "Loreto": "Baja California Sur",
            "Guerrero Negro": "Baja California Sur",
            "Victoria de Durango": "Durango",
            "Pueblo Nuevo": "Durango",
            "Santiago Papasquiaro": "Durango",
            "El Oro": "Durango",
            "Mapimí": "Durango",
            "Gómez Palacio": "Durango",
            "Lerdo": "Durango",
            "Cuencamé": "Durango",
            "Nombre de Dios": "Durango",
            "Acámbaro": "Guanajuato",
            "León Oriente": "Guanajuato",
            "León Poniente": "Guanajuato",
            "San Francisco del Rincón": "Guanajuato",
            "Purísima del Rincón": "Guanajuato",
            "Manuel Doblado": "Guanajuato",
            "Celaya Poniente": "Guanajuato",
            "Celaya Oriente": "Guanajuato",
            "Salvatierra": "Guanajuato",
            "Uriangato": "Guanajuato",
            "Yuriria": "Guanajuato",
            "Valle de Santiago": "Guanajuato",
            "Moroleón": "Guanajuato",
            "Cortazar": "Guanajuato",
            "Jaral del Progreso": "Guanajuato",
            "Irapuato Oriente": "Guanajuato",
            "Irapuato Poniente": "Guanajuato",
            "Abasolo": "Guanajuato",
            "Pénjamo": "Guanajuato",
            "Guanajuato": "Guanajuato",
            "Silao": "Guanajuato",
            "San Miguel de Allende": "Guanajuato",
            "Dolores Hidalgo": "Guanajuato",
            "San Felipe": "Guanajuato",
            "Ocampo": "Guanajuato",
            "San José Iturbide": "Guanajuato",
            "Doctor Mora": "Guanajuato",
            "Tierra Blanca": "Guanajuato",
            "Victoria": "Guanajuato",
            "Xichú": "Guanajuato",
            "Atarjea": "Guanajuato",
            "Santa Catarina": "Guanajuato",
            "San Luis de la Paz": "Guanajuato",
            "Santa Cruz de Juventino Rosas": "Guanajuato",
            "Celaya": "Guanajuato",
            "Comonfort": "Guanajuato",
            "Apaseo el Alto": "Guanajuato",
            "Apaseo el Grande": "Guanajuato",
            "Juventino Rosas": "Guanajuato",
            "La Piedad": "Michoacan",
            "Puruándiro": "Michoacan",
            "Maravatío": "Michoacan",
            "Jiquilpan": "Michoacan",
            "Paracho": "Michoacan",
            "Zamora": "Michoacan",
            "Zacapu": "Michoacan",
            "Tarímbaro": "Michoacan",
            "Los Reyes": "Michoacan",
            "Morelia": "Michoacan",
            "Hidalgo": "Hidalgo",
                "Zitácuaro": "Michoacan",
            "Uruapan": "Michoacan",
            "Pátzcuaro": "Michoacan",
            "Huetamo": "Michoacan",
            "Tacámbaro": "Michoacan",
            "Coalcomán": "Michoacan",
            "Múgica": "Michoacan",
            "Apatzingán": "Michoacan",
            "Lázaro Cárdenas": "Michoacan",
            "Cuernavaca": "Morelos",
            "Tepoztlán": "Morelos",
            "Yecapixtla": "Morelos",
            "Temixco": "Morelos",
            "Jiutepec": "Morelos",
            "Cuautla": "Morelos",
            "Xochitepec": "Morelos",
            "Puente de Ixtla": "Morelos",
            "Ciudad Ayala": "Morelos",
            "Jojutla": "Morelos",
            "Yautepec": "Morelos",
            "Acaponeta": "Nayarit",
            "Tecuala": "Nayarit",
            "Del Nayar": "Nayarit",
            "Tuxpan": "Nayarit",
            "Santiago Ixcuintla": "Nayarit",
            "Tepic": "Nayarit",
            "San Blas": "Nayarit",
            "Santa María del Oro": "Nayarit",
            "Xalisco": "Nayarit",
            "Compostela": "Nayarit",
            "Ixtlán del Río": "Nayarit",
            "Bahía de Banderas": "Nayarit",
            "Monterrey": "Nuevo Leon",
            "Apodaca": "Nuevo Leon",
            "San Nicolás de los Garza": "Nuevo Leon",
            "Guadalupe": "Nuevo Leon",
            "General Escobedo": "Nuevo Leon",
            "San Pedro Garza García": "Nuevo Leon",
            "García": "Nuevo Leon",
            "Sabinas Hidalgo": "Nuevo Leon",
            "Juárez": "Nuevo Leon",
            "Linares": "Nuevo Leon",
            "Santiago": "Nuevo Leon",
            "Querétaro": "Queretaro",
            "Corregidora": "Queretaro",
            "San Juan del Río": "Queretaro",
            "Pedro Escobedo": "Queretaro",
            "Tequisquiapan": "Queretaro",
            "El Marqués": "Queretaro",
            "Cadereyta de Montes": "Queretaro",
            "Jalpan de Serra": "Queretaro",
            "Kantunilkín": "Quintana Roo",
            "Cancún": "Quintana Roo",
            "Tulum": "Quintana Roo",
            "Playa del Carmen": "Quintana Roo",
            "Cozumel": "Quintana Roo",
            "Felipe Carrillo Puerto": "Quintana Roo",
            "Bacalar": "Quintana Roo",
            "Chetumal": "Quintana Roo",
            "Gustavo A. Madero": "Distrito Federal",
            "Azcapotzalco": "Distrito Federal",
            "Milpa Alta": "Distrito Federal",
            "Tláhuac": "Distrito Federal",
            "Cuauhtémoc": "Distrito Federal",
            "Venustiano Carranza": "Distrito Federal",
            "Miguel Hidalgo": "Distrito Federal",
            "Tlalpan": "Distrito Federal",
            "Iztacalco": "Distrito Federal",
            "Benito Juárez": "Distrito Federal",
            "Álvaro Obregón": "Distrito Federal",
            "Iztapalapa": "Distrito Federal",
            "Xochimilco": "Distrito Federal",
            "Coyoacán": "Distrito Federal",
            "Magdalena Contreras": "Distrito Federal",
            "Tenosique": "Tabasco",
            "Cárdenas": "Tabasco",
            "Huimanguillo": "Tabasco",
            "Centla": "Tabasco",
            "Centro": "Tabasco",
            "Tacotalpa": "Tabasco",
            "Comalcalco": "Tabasco",
            "Cunduacán": "Tabasco",
            "Emiliano Zapata": "Tabasco",
            "Jalpa de Méndez": "Tabasco",
            "Macuspana": "Tabasco",
            "Nacajuca": "Tabasco",
            "Paraíso": "Tabasco",
            "Zacatecas": "Zacatecas",
            "Fresnillo": "Zacatecas",
            "Ojocaliente": "Zacatecas",
            "Jerez": "Zacatecas",
            "Villanueva": "Zacatecas",
            "Villa de Cos": "Zacatecas",
            "Jalpa": "Zacatecas",
            "Tlaltenango": "Zacatecas",
            "Pinos": "Zacatecas",
            "Río Grande": "Zacatecas",
            "Sombrerete": "Zacatecas",
            "Juan Aldama": "Zacatecas",
            "Colima": "Colima",
            "Comala": "Colima",
            "Coquimatlán": "Colima",
            "Villa de Álvarez": "Colima",
            "Armería": "Colima",
            "Ixtlahuacán": "Colima",
            "Manzanillo": "Colima",
            "Minatitlán": "Colima",
            "Tecomán": "Colima",
            "Mérida": "Yucatan",
            "Kanasín": "Yucatan",
            "Umán": "Yucatan",
            "Progreso": "Yucatan",
            "Tizimín": "Yucatan",
            "Valladolid": "Yucatan",
            "Tekax": "Yucatan",
            "Ticul": "Yucatan",
            "Tecoh": "Yucatan",
            "Izamal": "Yucatan",
            "Mexicali": "Baja California",
            "Tecate": "Baja California",
            "Tijuana": "Baja California",
            "Playas de Rosarito": "Baja California",
            "Ensenada": "Baja California",
            "Campeche": "Campeche",
            "Tenabo": "Campeche",
            "Carmen": "Campeche",
            "Escárcega": "Campeche",
            "Candelaria": "Campeche",
            "Champotón": "Campeche",
            "Seybaplaya": "Campeche",
            "Calkiní": "Campeche",
            "Hopelchén": "Campeche",
            "Hecelchakán": "Campeche",
            "Palizada": "Campeche",
            "Calakmul": "Campeche",
            "Tuxtla Gutiérrez": "Chiapas",
            "Chiapa de Corzo": "Chiapas",
            "Yajalón": "Chiapas",
            "San Cristóbal de Las Casas": "Chiapas",
            "Comitán de Domínguez": "Chiapas",
            "Ocosingo": "Chiapas",
            "Simojovel de Allende": "Chiapas",
            "Palenque": "Chiapas",
            "Frontera Comalapa": "Chiapas",
            "Bochil": "Chiapas",
            "Pichucalco": "Chiapas",
            "Cintalapa": "Chiapas",
            "Villaflores": "Chiapas",
            "Huixtla": "Chiapas",
            "Motozintla": "Chiapas",
            "Mapastepec": "Chiapas",
            "Tapachula": "Chiapas",
            "Las Margaritas": "Chiapas",
            "Tenejapa": "Chiapas",
            "San Juan Chamula": "Chiapas",
            "Villa Corzo": "Chiapas",
            "Cacahoatán": "Chiapas",
                "Nuevo Casas Grandes": "Chihuahua",
                "Ciudad Juárez": "Chihuahua",
                "Meoqui": "Chihuahua",
                "Chihuahua": "Chihuahua",
                "Guerrero": "Chihuahua",
                "Delicias": "Chihuahua",
                "Camargo": "Chihuahua",
                "Hidalgo del Parral": "Chihuahua",
                "Guachochi": "Chihuahua",
                "Chilpancingo": "Guerrero",
                "Acapulco": "Guerrero",
                "Tecpan": "Guerrero",
                "Zihuatanejo": "Guerrero",
                "San Marcos": "Guerrero",
                "Ayutla": "Guerrero",
                "San Luis Acatlán": "Guerrero",
                "Ometepec": "Guerrero",
                "Coyuca": "Guerrero",
                "Pungarabato": "Guerrero",
                "Eduardo Neri": "Guerrero",
                "Teloloapan": "Guerrero",
                "Taxco de Alarcón": "Guerrero",
                "Iguala": "Guerrero",
                "Huitzuco": "Guerrero",
                "Tixtla": "Guerrero",
                "Chilapa": "Guerrero",
                "Atlixtac": "Guerrero",
                "Tlapa": "Guerrero",
                "Tequila": "Jalisco",
                "Lagos de Moreno": "Jalisco",
                "Tepatitlán de Morelos": "Jalisco",
                "Zapopan": "Jalisco",
                "Puerto Vallarta": "Jalisco",
                "Tonalá": "Jalisco",
                "Guadalajara": "Jalisco",
                "Tlajomulco de Zúñiga": "Jalisco",
                "San Pedro Tlaquepaque": "Jalisco",
                "La Barca": "Jalisco",
                "Jocotepec": "Jalisco",
                "Autlán de Navarro": "Jalisco",
                "Zapotlan el Grande": "Jalisco",
                "San Juan Bautista Tuxtepec": "Oaxaca",
                "Loma Bonita": "Oaxaca",
                "Teotitlán de Flores Magón": "Oaxaca",
                "Asunción Nochixtlán": "Oaxaca",
                "Heroica Huajuapan de León": "Oaxaca",
                "Putla Villa de Guerrero": "Oaxaca",
                "Heroica Ciudad de Tlaxiaco": "Oaxaca",
                "Ixtlán de Juárez": "Oaxaca",
                "San Pedro y San Pablo Ayutla": "Oaxaca",
                "Matías Romero Avendaño": "Oaxaca",
                "Santa Lucía del Camino": "Oaxaca",
                "Oaxaca de Juárez": "Oaxaca",
                "Santa Cruz Xoxocotlán": "Oaxaca",
                "Zimatlán de Álvarez": "Oaxaca",
                "Tlacolula de Matamoros": "Oaxaca",
                "Santo Domingo Tehuantepec": "Oaxaca",
                "Salina Cruz": "Oaxaca",
                "Heroica Juchitán de Zaragoza": "Oaxaca",
                "Heroica Ciudad de Ejutla de Crespo": "Oaxaca",
                "Santiago Pinotepa Nacional": "Oaxaca",
                "San Pedro Mixtepec": "Oaxaca",
                "Miahuatlán de Porfirio Díaz": "Oaxaca",
                "San Pedro Pochutla": "Oaxaca",
                "Xicotepec de Juárez": "Puebla",
                "Huauchinango": "Puebla",
                "Zacatlán": "Puebla",
                "Zacapoaxtla": "Puebla",
                "Tlatlauquitepec": "Puebla",
                "Teziutlán": "Puebla",
                "San Martín Texmelucan": "Puebla",
                "Huejotzingo": "Puebla",
                "Puebla de Zaragoza": "Puebla",
                "Amozoc": "Puebla",
                "Tepeaca": "Puebla",
                "Chalchicomula de Sesma": "Puebla",
                "Tecamachalco": "Puebla",
                "San Pedro Cholula": "Puebla",
                "Atlixco": "Puebla",
                "Izúcar de Matamoros": "Puebla",
                "Acatlán de Osorio": "Puebla",
                "Tehuacán": "Puebla",
                "Ajalpan": "Puebla",
                "Matehuala": "San Luis Potosi",
                "San Luis Potosí": "San Luis Potosi",
                "Santa María del Río": "San Luis Potosi",
                "Salinas": "San Luis Potosi",
                "Soledad de Graciano Sánchez": "San Luis Potosi",
                "Rioverde": "San Luis Potosi",
                "Ciudad Valles": "San Luis Potosi",
                "Tamuín": "San Luis Potosi",
                "Tancanhuitz": "San Luis Potosi",
                "Tamazunchale": "San Luis Potosi",
                "El Fuerte": "Sinaloa",
                "Ahome": "Sinaloa",
                "Sinaloa de Leyva": "Sinaloa",
                "Guasave": "Sinaloa",
                "Salvador Alvarado": "Sinaloa",
                "Mocorito": "Sinaloa",
                "Navolato": "Sinaloa",
                "Culiacán": "Sinaloa",
                "Elota": "Sinaloa",
                "Mazatlán": "Sinaloa",
                "Concordia": "Sinaloa",
                "Rosario": "Sinaloa",
                "San Luis Río Colorado": "Sonora",
                "Puerto Peñasco": "Sonora",
                "Heroica Caborca": "Sonora",
                "Heroica Nogales": "Sonora",
                "Hermosillo": "Sonora",
                "Agua Prieta": "Sonora",
                "Heroica Guaymas": "Sonora",
                "Empalme": "Sonora",
                "Ciudad Obregón": "Sonora",
                "Santa Ana": "Sonora",
                "Navojoa": "Sonora",
                "Etchojoa": "Sonora",
                "Huatabampo": "Sonora",
                "Nuevo Laredo": "Tamaulipas",
                "Reynosa": "Tamaulipas",
                "Rio Bravo": "Tamaulipas",
                "Valle Hermoso": "Tamaulipas",
                "Matamoros": "Tamaulipas",
                "San Fernando": "Tamaulipas",
                "Ciudad Victoria": "Tamaulipas",
                "Xicoténcatl": "Tamaulipas",
                "El Mante": "Tamaulipas",
                "Altamira": "Tamaulipas",
                "Miramar": "Tamaulipas",
                "Ciudad Madero": "Tamaulipas",
                "Tampico": "Tamaulipas",
                "Calpulalpan": "Tlaxcala",
                "Tlaxco": "Tlaxcala",
                "Xaloztoc": "Tlaxcala",
                "Apizaco": "Tlaxcala",
                "Yauhquemecan": "Tlaxcala",
                "Ixtacuixtla": "Tlaxcala",
                "Tlaxcala": "Tlaxcala",
                "Contla": "Tlaxcala",
                "Chiautempan": "Tlaxcala",
                "Huamantla": "Tlaxcala",
                "Teolocholco": "Tlaxcala",
                "Zacatelco": "Tlaxcala",
                "Natívitas": "Tlaxcala",
                "San Pablo del Monte": "Tlaxcala",
                "Pánuco": "Veracruz",
                "Tantoyuca": "Veracruz",
                "Álamo": "Veracruz",
                "Poza Rica": "Veracruz",
                "Papantla": "Veracruz",
                "Martínez de la Torre": "Veracruz",
                "Misantla": "Veracruz",
                "Perote": "Veracruz",
                "Xalapa": "Veracruz",
                "Coatepec": "Veracruz",
                "Veracruz": "Veracruz",
                "Boca del Río": "Veracruz",
                "Medellín": "Veracruz",
                "Huatusco": "Veracruz",
                "Córdoba": "Veracruz",
                "Orizaba": "Veracruz",
                "Camerino Z. Mendoza": "Veracruz",
                "Zongolica": "Veracruz",
                "Cosamaloapan": "Veracruz",
                "Santiago Tuxtla": "Veracruz",
                "San Andrés Tuxtla": "Veracruz",
                "Cosoleacaque": "Veracruz",
                "Acayucan": "Veracruz",
                "Coatzacoalcos": "Veracruz",
                "Ciudad Acuña": "Coahuila",
                "Piedras Negras": "Coahuila",
                "Sabinas": "Coahuila",
                "San Pedro": "Coahuila",
                "Monclova": "Coahuila",
                "Frontera": "Coahuila",
                "Torreón": "Coahuila",
                "Ramos Arizpe": "Coahuila",
                "Saltillo": "Coahuila"
            }

            # Create a new column called "state" and assign the corresponding value from the dictionary
            municipales["Estado"] = municipales["Cabecera Municipal"].map(states)

            municipales.to_csv("Diputados_Municipales.csv")
        municipales = funcion_yisus()
        transformacion(municipales)

    funcion_municipales()
    funcion_isaac()

#funciones_extraccion()

###
def ejecutar_dashboard():
    # Desactivar el botón
    #boton.config(state=tk.DISABLED)

    # Ejecutar el comando para iniciar el dashboard en la misma ventana
    comando = ["python", "interfaz.py"]
    subprocess.Popen(comando)
    time.sleep(8)
    abrir_navegador()

def abrir_navegador():
    url = "http://127.0.0.1:8050/"
    webbrowser.open_new(url)

def ejecutar_funcion():
    # Desactivar el botón
    boton.config(state=tk.DISABLED)

    # Actualizar la etiqueta de texto
    etiqueta.config(text="Cargando...")
    ventana.update()

    # Mostrar la barra de progreso
    progress_bar.place(x=100, y=80)

    # Iniciar la animación de la barra de progreso en un hilo separado
    t = Thread(target=animar_barra_progreso)
    t.start()

    # Simular una operación larga en un hilo separado
    t2 = Thread(target=realizar_operacion_larga)
    t2.start()

def realizar_operacion_larga():
    # Simular una operación larga
    # Puedes reemplazar este bloque con tu propia lógica
    funciones_extraccion()
    #time.sleep(5)
    # Detener la animación de la barra de progreso
    detener_barra_progreso()

    # Actualizar la etiqueta de texto
    ventana.after(0, lambda: etiqueta.config(text="Finalizado"))

    # Activar el botón nuevamente
    ventana.after(0, lambda: boton.config(state=tk.NORMAL))

    # Ocultar la barra de progreso
    ventana.after(0, lambda: progress_bar.place_forget())

def animar_barra_progreso():
    # Mostrar la barra de progreso indeterminada
    progress_bar.start()

def detener_barra_progreso():
    # Detener la animación de la barra de progreso
    progress_bar.stop()
    # Reiniciar el valor de la barra de progreso
    progress_bar["value"] = 0

ventana = tk.Tk()

# Ajustar el tamaño de la ventana
ventana.geometry("400x200")

etiqueta = tk.Label(ventana, text="")
etiqueta.pack(pady=10)

# Configurar estilo para los botones
style = ttk.Style()
style.configure("Custom.TButton", foreground="black", background="blue")
style.map("Custom.TButton", background=[('pressed', 'dark blue'), ('active', 'green')])

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=0)

boton = ttk.Button(frame_botones, text="Actualizar datos", command=ejecutar_funcion, style="Custom.TButton")
boton.pack(side=tk.TOP, pady=0, padx=35, fill=tk.BOTH, expand=True)

botondash = ttk.Button(frame_botones, text="Dashboard", command=ejecutar_dashboard, style="Custom.TButton")
botondash.pack(side=tk.BOTTOM, pady=50, padx=35, fill=tk.BOTH, expand=True)

# Crear el indicador de carga utilizando una barra de progreso indeterminada
style.configure("TProgressbar", thickness=10)
progress_bar = ttk.Progressbar(ventana, style="TProgressbar", mode="indeterminate", length=200)

ventana.mainloop()

