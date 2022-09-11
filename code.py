from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

brightest_stars_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(brightest_stars_url)
# print(page)

soup = bs(page.text , 'html.parser')

star_table = soup.find('table')

table_rows = star_table[7].find_all('tr')

temp_list = []

for tr in table_rows :
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)


Star_names = []
Distance =[]
Mass = []
Radius =[]
 
# temp_list = [ [a , b] , [f , h , 5] , []  ]
# temp_list[1][2]

for i in range(1, len(temp_list)):
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])

print(df2)

df2.to_csv("brightStars.csv")




