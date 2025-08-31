import re,requests
from bs4 import BeautifulSoup
import html as parser1
import json
from datetime import datetime,time
import  time
import pandas as pd
import pymysql
from fake_useragent import UserAgent
import requests


ua = UserAgent()

db=pymysql.connect(host='localhost',user='root',password='@ggreg@te',database='Traning')
input_table='olympics'
medals_table='olympics_medals'
curuser=db.cursor()

print('db connected')

curuser.execute(f'select * from {input_table}')
results=curuser.fetchall()

def page_insert(olymic_name,Year,slug,location,url,startdate,Enddate,olimg_url,status=0):
    if  slug not in [i[3] for i in results] or len(results)==0:
        curuser.execute('insert into '+input_table+'(olymic,olymic_year,slug,location,Page_url,start_date,end_date,logo,status)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(olymic_name,Year,slug,location,url,startdate,Enddate,olimg_url,status))
        print('inserted')
        db.commit()
    else:   
        print('alredy insert')
    db.commit()
def update(ref_id,status):
    curuser.execute(f"update {input_table} set status=%s where id=%s",(status,ref_id))
    print(f'update {status}')
    db.commit()

def medels_insert(ref_id,olymic_name,Year,slug,location,country,Countrycode,country_img,gold,Silver,bronze,Total,url):    
    curuser.execute('insert into olympics_medals(ref_id,olympic,olympic_year,slug,location,country,Country_code,country_img,Gold,silver,Bronze,total,page_url)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(ref_id,olymic_name,Year,slug,location,country,Countrycode,country_img,gold,Silver,bronze,Total,url))
    print('Medal insert')
    update(ref_id,status=1)
    
    db.commit()
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
    startdate=Pages[i]['startDate'].replace("Z",'')
    Enddate=Pages[i]['endDate'].replace("Z",'')
    img_tag=Pages[i]['emblem']['image']['urlTemplate']
    img_form=Pages[i]['emblem']['image']['format']
    olimg_url=img_tag.replace('{formatInstructions}','f_auto')+"."+img_form
    url=f'https://www.olympics.com/en/olympic-games/{slug}/medals'
    page_insert(olymic_name,Year,slug,location,url,startdate,Enddate,olimg_url,status=0)
curuser.execute(f'select * from {input_table} where status=0')
results=curuser.fetchall()
for input in results:
    url=input[5]
    ref_id=input[0]
    olymic_name=input[1]
    Year=input[2]
    slug=input[3]
    location=input[4]
    #time.sleep(10)
    response = requests.get('https://www.olympics.com/en/olympic-games/paris-2024/medals', headers=headers)
    print(url)
    response=response.text
    if re.findall(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',response):
        props=re.findall(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',response)
        props=json.loads(props[0]) 
        props=props['props']['pageProps']['olympicGame']
        if 'countryAwards' in props:
            countryAwards= props['countryAwards']
            if  type(len(countryAwards))==int :
                for i in range (len(props['countryAwards'])):
                    country= props['countryAwards'][i]['country']['name']
                    Countrycode=props['countryAwards'][i]['countryCode']
                    country_img='https://gstatic.olympics.com/s3/noc/oly/3x2/'+Countrycode+'.png'
                    medals=props['countryAwards'][i]['medals']
                    gold=Silver=bronze=0
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
                    Total=gold+Silver+bronze
                    print(f'{country} - gold:{gold},Sliver:{Silver},brozne:{bronze},Total:{gold+Silver+bronze}')
                    medels_insert(ref_id,olymic_name,Year,slug,location,country,Countrycode,country_img,gold,Silver,bronze,Total,url)    
            else:
                update(ref_id,status=2)
        else:
            update(ref_id,status=2)
    else:
        update(ref_id,status=2)
            #print(len(medals))
db.close()
