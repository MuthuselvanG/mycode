import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
import json
import pandas as pd
import time
import datetime
import pymysql
import ast 

db=pymysql.connect(host='localhost',user='root',password='@ggreg@te',database='Traning')
cursor=db.cursor()
print("db connected")

headers = {'Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',}
response = requests.get(
    'https://www.google.com/search?q=jobs%20in%20coimbatore&oq=jobs%20in%20coimbatore&gs_lcrp=EgZjaHJvbWUqDAgAEEUYOxixAxiABDIMCAAQRRg7GLEDGIAEMgcIARAAGIAEMgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAEqAIAsAIA&sourceid=chrome&ie=UTF-8&jbr=sep:0&udm=8&ved=2ahUKEwjdoLym2daMAxUUyDgGHfKrM3QQ3L8LegQIKBAO',
    
    headers=headers,
)
print(response.status_code)
soup=response.content.decode('unicode_escape')

def insert(title,company_name,loaction,job_des,apply_link,jid,post,Wmode,Clogo):
    cursor.execute("insert into job (title,cname,location,job_desc,link,Workmode,job_id,posted,logo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(title,company_name,loaction,job_des,apply_link,Wmode,jid,post,Clogo))
    #print(f'{title} inserted')
    db.commit()
#print(soup)
all_job=[]
def extract(datas):
    exdta=[]
    for data in datas:    
        #print(data)   
        
        data=json.loads(data)
        #print(data)      
        title=data['520084652'][0]
        company_name=data['520084652'][1]
        loaction=data['520084652'][2]
        job_des = data['520084652'][19]
        apply_link=[]
        for i in range(len(data['520084652'][3])):
            link_name=data['520084652'][3][i][2]
            link=data['520084652'][3][i][0].split("?utm")
            link=link[0]
            dic_lnk={'link_name':link_name,'link':link}
            #dic_lnk=json.dumps(dic_lnk)
            apply_link.append(dic_lnk)
        apply_link=json.dumps(apply_link)
        jid=data['520084652'][3][0][3]
        post=data['520084652'][12]
        if data['520084652'][23]:
            Wmode=data['520084652'][23]
            Wmode=Wmode.encode('latin1').decode('utf-8')
        Clogo=data['520084652'][17]
        #print(title,company_name,loaction,job_des,apply_link,id,post)
        #print(apply_link)
        ext_dict={'title':title,'company_name':company_name,'loaction':loaction,'job_des':job_des,'apply_link':apply_link,'Wmode':Wmode,'jid':jid,'Posted':post,'clogo':Clogo}
        insert(title,company_name,loaction,job_des,json.dumps(apply_link),jid,post,Wmode,Clogo)
        #print(ext_dict)
        exdta.append(ext_dict)
    return(exdta)
import json
datas=re.findall(r'\[\[\[\[\{.*?491935102.*?\[\[\[\[(.*?)]]]]]',soup)
jobs=extract(datas)
#print(job)
nextid=re.findall(r'jsname="Yust4d".*?data-async-fc="(.*?)" data-a',soup)
#print(nextid)item

page=1
while nextid:
    #print(datetime.datetime.now())
    #time.sleep(20)
    #print(datetime.datetime.now())
    nextid=nextid[0]
    next_url=f'https://www.google.com/async/callback:550?fc={nextid}&fcv=3&vet=12ahUKEwiZ69Wjn9mMAxWjd2wGHUQvHMAQw40IegQIJBAO..i&ei=X-b9Z9m_GaPvseMPxN7wgAw&opi=89978449&sca_esv=a5672ed9c1a134ac&udm=8&yv=3&cs=0&async=_basejs:%2Fxjs%2F_%2Fjs%2Fk%3Dxjs.s.en_GB.7dq7KLbWqlg.2018.O%2Fam%3DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAABAAAUBIAAAAAAAAAAgAAQAAAAAAACAAQAAAAAAAAkIAAFBAgAAAAAIAAAAAAAAEwCAgGAFAKAAAAAAAAAAAAAAEAAAAAAQEAHwvn8wAAAAAAAAAAAAAAAAAAAEQAIAAAAAAAAAuAAAEAAHABCyCxAAAAAAAAAAAAQAAAAAAAAIAAAAAABAAAAAAAUAAAAAAAAAABAAAAAAAAAACAAAACAAAEAAAAAAAAAAAAAAAAAAAAAAACAAgAYAAAoAIIAfAAAAAAAABwAAAKAAAAAAOMYoAAIAAAAAAADyAPB4AIcUFAAAAAAAAAAAAAAAAASgIJgD6RcECAAAAAAAAAAAAAAAAAAAIEXQxLUGAAg%2Fdg%3D0%2Fbr%3D1%2Frs%3DACT90oEJRBK8Jld4KzC7cG12n5RtfwNYWw,_basecss:%2Fxjs%2F_%2Fss%2Fk%3Dxjs.s.JLbRv4firFU.L.B1.O%2Fam%3DAIQjEAIAAAABAAAgBIAKQAAAAAAAAAAAAAAAAAAAAAAAAAAAEgAAAEAAAAAAAAAQAGAMEAEABGYKAAAAgOAEAGQHAAAAAD4AADgVABAAAAAAAAFAAgAAAAAAAAgA0BMAEhAAABAFAAAAAAQIQhgAIAAAGwAAkAgAAEEAAIAgYAAAGQAAAAAgAABOBQDEAQAQAAAGAgCOgAAgAQAAABAKC4AAAACUIAAAAAAAAAUAAAAIAAAQAYBDMAyAQAWAATgCAAAAACIAIBAAAAAIABACAGIAgAIAQIAAwAMAAvABAAAgASIAADTAAAQIAAoBAAGAHwAgAAAAIAEAABAAgCIAOMYoAAIAAAAAAACQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAQ%2Fbr%3D1%2Frs%3DACT90oGkyCX8g6nBXeIixUwdgWWyVEDqhg,_basecomb:%2Fxjs%2F_%2Fjs%2Fk%3Dxjs.s.en_GB.7dq7KLbWqlg.2018.O%2Fck%3Dxjs.s.JLbRv4firFU.L.B1.O%2Fam%3DAIQjEAIAAAABAAAgBIAKQAAAAAAAAAAAAAAAAAAAAAAAAAAAEgAAAEAAAAAAAAAQAGBMEAUBJGYKAAAAgOAkAGQHAAAAAD6AATgVABAAAAkIAAFBAgAAAAAIAAgA0BMAExCAgHAFAKAAAAQIQhgAIAAAGwAAkAgQEEHwvv8wYAAAGQAAAAAgAABOBQDEQQIQAAAGAgCOuAAgEQAHABC6C5AAAACUIAAAAAQAAAUAAAAIAAAQAYBDMAyAQAWAATgCAAAAADIAIBAAAAAICBACAGIAgEIAQIAAwAMAAvABAAAgASIAADTAgAYIAAoBIIGfHwAgAAAAJwEAALAAgCIAOMYoAAIAAAAAAADyAPB4AIcUFAAAAAAAAAAAAAAAAASgIJgD6RcECAAAAAAAAAAAAAAAAAAAIEXQxLUGAAg%2Fd%3D1%2Fed%3D1%2Fdg%3D0%2Fbr%3D1%2Fujg%3D1%2Frs%3DACT90oGLK-4mHY6SD0g-PDy8Qw8STM-Kyw,_fmt:prog,_id:fc_X-b9Z9m_GaPvseMPxN7wgAw_2'
    response = requests.get(next_url,
    #cookies=cookies,
    headers=headers)
    print(f'page{response.status_code}')
    res=response.content.decode('unicode_escape')
    #res=response.content.decode('utf-8', errors='replace')
    next_data=re.findall(r'\[\[\[\[\{.*?491935102.*?\[\[\[\[(.*?)]]]]]',res)
    #next_data=ast.literal_eval(next_data)
    page_job=extract(next_data)
    #jobs.extend(page_job)
    if re.findall(r'jsname="Yust4d".*?data-async-fc="(.*?)" data-a',res):
        nextid=re.findall(r'jsname="Yust4d".*?data-async-fc="(.*?)" data-a',res)
    else:
        nextid=''
    #print(page_job)
    #print(nextid)
    page+=1
    if page==3:
    #if nextid=='':
        print('all page extrac')
        break
        
cursor.execute("select * from  job")
nuumber_rows=cursor.fetchall()
nuumber_rows=cursor.rowcount
print(f'{nuumber_rows} Number jobs inserted ')
#df=pd.DataFrame(jobs)
#df.to_csv('google.csv')