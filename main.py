from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests.get(url=url)
soup = BeautifulSoup(response.content,'html.parser')
rows = soup.find('table',{'id' :'example2'}).tbody.find_all('tr')
list_country=[]
for row in rows:
    dic= {}
    dic['Country (or dependency)'] = row.find_all('td')[1].text
    dic['Population'] = row.find_all('td')[2].text
    dic['Yearly change'] = row.find_all('td')[3].text
    dic['Net change'] = row.find_all('td')[4].text
    dic['Density  (P/Km²)'] = row.find_all('td')[5].text
    dic['Land Area  (Km²)'] = row.find_all('td')[6].text
    dic['Migrants  net'] = row.find_all('td')[7].text
    dic['Fert. Rate'] = row.find_all('td')[8].text
    dic['Med. Age'] = row.find_all('td')[9].text
    dic['Med. Age'] = row.find_all('td')[10].text
    dic['Urban.  Pop %'] = row.find_all('td')[11].text
    dic['World  Share'] = row.find_all('td')[11].text
    list_country.append(dic)
df = pd.DataFrame(list_country)
df.to_csv('data.csv',index=False)