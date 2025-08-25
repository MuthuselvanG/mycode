import re,requests
from bs4 import BeautifulSoup
import html as parser1
import json
from datetime import datetime,time
import  time
import pandas as pd
import pymysql


headers = {
    'sec-ch-ua-platform': '"Linux"',
    'Referer': 'https://www.olympics.com/en/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
}

# response = requests.get('https://www.olympics.com/en/api/v1/b2p/menu/topbar/olympic-games', headers=headers)

# print(response.status_code)
# html=response.json()
# datetime=datetime.now()
# cyear=datetime.year
# for i in range(len(html['modules'][2]['content'])):
#     Season=html['modules'][2]['content'][i]['season']
#     pageurl=html['modules'][2]['content'][i]['url']
#     olypics_year=html['modules'][2]['content'][i]['year']
#     if int(olypics_year)<cyear:
#         landurl=pageurl+'/medals'
response = requests.get('https://www.olympics.com/en/olympic-games/paris-2024/medals', headers=headers)

response=response.text
props=re.findall(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',response)
props=json.loads(props[0])
Pages=props['props']['pageProps']['allGames']
#print(Pages)
for i in range (len(Pages)):
    slug=Pages[i]["meta"]['slug']
    location=Pages[i]['location']
    Year=Pages[i]['year']
    olymic_name=Pages[i]['name']
    startdate=Pages[i]['startDate']
    Enddate=Pages[i]['endDate']
    img_tag=Pages[i]['emblem']['image']['urlTemplate']
    img_form=Pages[i]['emblem']['image']['format']
    url=f'https://www.olympics.com/en/olympic-games/{slug}/medals'
    response = requests.get(url, headers=headers)
    print(url)
    time.sleep(10)
    response=response.text
    if re.findall(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',response):
        props=re.findall(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',response)
        props=json.loads(props[0]) 
        props=props['props']['pageProps']['olympicGame']
        countryAwards=props['countryAwards']

        if  type(len(countryAwards))==int :
            for i in range (len(props['countryAwards'])):
                country= props['countryAwards'][i]['country']['name']
                Countrycode=props['countryAwards'][i]['countryCode']
                country_img='https://gstatic.olympics.com/s3/noc/oly/3x2/'+Countrycode+'.png'
                medals=props['countryAwards'][i]['medals']
                gold=silver=bronze=0
                for j in range(len(medals)):
                    medalType=medals[j]['medalType']
                    if  medalType=='GOLD':
                        gold=medals[j]['count']
                    #print(f'gold:{gold}')
                    if medalType=='SILVER':
                        Silver=medals[j]['count']
                    #print(f'Sliver:{Silver}')
                    
                    if medalType=='BRONZE':
                        bronze=medals[j]['count']
                print(f'{country} - gold:{gold},Sliver:{Silver},brozne:{bronze},Total:{gold}+{Silver}+{bronze}')
        else:
            print('data not available')   
    else:
        print('da')
            #print(len(medals))

