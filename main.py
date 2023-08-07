from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
# URL de la page web à scraper
url = "https://www.worldometers.info/world-population/population-by-country/"

# Envoi d'une requête GET à l'URL pour obtenir la page HTML
response = requests.get(url=url)

# Initialisation de l'objet BeautifulSoup pour analyser le contenu HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Recherche de la table contenant les données de population
table = soup.find('table', {'id': 'example2'})

# Extraction des lignes de la table (les pays et leurs données)
rows = table.tbody.find_all('tr')

# Liste pour stocker les données des pays
list_country = []

# Parcours des lignes pour extraire les données
for row in rows:
    dic = {}
    dic['Country (or dependency)'] = row.find_all('td')[1].text
    dic['Population'] = row.find_all('td')[2].text
    dic['Yearly change'] = row.find_all('td')[3].text
    dic['Net change'] = row.find_all('td')[4].text
    dic['Density  (P/Km²)'] = row.find_all('td')[5].text
    dic['Land Area  (Km²)'] = row.find_all('td')[6].text
    dic['Migrants  net'] = row.find_all('td')[7].text
    dic['Fert. Rate'] = row.find_all('td')[8].text
    dic['Med. Age'] = row.find_all('td')[9].text
    dic['Urban.  Pop %'] = row.find_all('td')[10].text
    dic['World  Share'] = row.find_all('td')[11].text
    list_country.append(dic)

# Création d'un DataFrame pandas à partir des données extraites
df = pd.DataFrame(list_country)

# Enregistrement du DataFrame au format CSV
df.to_csv('data.csv', index=False)  # Enregistrement au format CSV

# Enregistrement du DataFrame au format Excel
df.to_excel('data.xlsx', index=False)  # Enregistrement au format Excel
