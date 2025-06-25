import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
import json
import pandas as pd
import time
from  datetime import datetime, timedelta
import pymysql
import html as parser1
job_search='job in coimbatore'
try:
    
    db=pymysql.connect(host='localhost',user='root',password='Muthuplr99@',database='training')
    #db=pymysql.connect(host='localhost',user='root',password='@ggreg@te',database='Traning') #office connections

    cursor=db.cursor()
    print("db connected")
    cursor.execute("select * from job1 where job_search=%s",(job_search))
    result=cursor.fetchall()
    print(list(result))
    headers = {'Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',}
    response = requests.get(
        'https://www.google.com/search?q='+job_search+'&oq='+job_search+'&gs_lcrp=EgZjaHJvbWUqDAgAEEUYOxixAxiABDIMCAAQRRg7GLEDGIAEMgcIARAAGIAEMgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAEqAIAsAIA&sourceid=chrome&ie=UTF-8&jbr=sep:0&udm=8&ved=2ahUKEwjdoLym2daMAxUUyDgGHfKrM3QQ3L8LegQIKBAO',
        #'https://www.google.com/search?q=jobs%20in%20coimbatore&oq=jobs%20in%20coimbatore&gs_lcrp=EgZjaHJvbWUqDAgAEEUYOxixAxiABDIMCAAQRRg7GLEDGIAEMgcIARAAGIAEMgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAEqAIAsAIA&sourceid=chrome&ie=UTF-8&jbr=sep:0&udm=8&ved=2ahUKEwjdoLym2daMAxUUyDgGHfKrM3QQ3L8LegQIKBAO',    
        #'https://www.google.com/search?q=job%20in%20coimbatore&oq=jo&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDkyBggCEEUYOzIGCAMQRRg7MgoIBBAuGLEDGIAEMgYIBRBFGDwyBggGEEUYPDIGCAcQRRg80gEIMjQ2NGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8&jbr=sep:0&udm=8&ved=2ahUKEwi_x-23tvCMAxVp96ACHaCuMA0Q3L8LegQIIBAO',
        headers=headers,
    )
    print(response.status_code)
    #response.encoding = ''
    #soup=response.text
    #soup=parser1.unescape(response.content.decode('utf-8'))
    soup=response.text#decode('utf-8')
    #open("gott.html","w").write(soup)
    

    def insert(title,company_name,loaction,job_des,apply_link,jid,post,Wmode,Clogo,datepost,job_search):
        #cursor.execute("insert into job1 (title,cname,location,job_desc,link,Workmode,job_id,posted,logo,postdate,job_search) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(title,company_name,loaction,job_des,apply_link,Wmode,jid,post,Clogo,datepost,job_search))
        #print('inserted')
        db.commit()
    #print(soup)
    all_job=[]
    def extract(datas):
        exdta=[]
        for data in datas:
            #print(data)  
            if  'â'  in  data:
                data=data.encode('latin1',errors='ignore').decode('utf-8', errors='ignore')
                data=json.loads(data)
            else:
                data=json.loads(data)
            #print(data)
            # data=data.encode().decode('unicode_escape')
            # data=data.encode('utf-8').decode('utf-8', errors='ignore')
            # data=json.loads(data)
            #print(data)      
            title=data['520084652'][0]
            company_name=data['520084652'][1]
            loaction=data['520084652'][2]
            if data['520084652'][19]:
                job_des = data['520084652'][19]#.replace("â¢",".")
            apply_link=[]
            for i in range(len(data['520084652'][3])):
                link_name=data['520084652'][3][i][2]
                link=data['520084652'][3][i][0].split("?utm")
                link=link[0]
                dic_lnk={'link_name':link_name,'link':link}
                #dic_lnk=json.dumps(dic_lnk)
                apply_link.append(dic_lnk)
            #apply_link=json.dumps(apply_link)
            jid=data['520084652'][3][0][3]
            if data['520084652'][12]:
                post=data['520084652'][12]#.split(" ")
                #print(post)
            else:
                post=''
            if data['520084652'][23]:
                Wmode=data['520084652'][23]
            else:
                Wmode=''
                #Wmode=Wmode#.encode('latin1').decode('utf-8')
            Clogo=data['520084652'][17]
            #print(title,company_name,loaction,job_des,apply_link,id,post)
            #print(apply_link)
            #ext_dict={'title':title,'company_name':company_name,'loaction':loaction,'job_des':job_des,'apply_link':apply_link,'Wmode':Wmode,'jid':jid,'Posted':post,'clogo':Clogo}
            now=datetime.now()
            if 'hour' in post:
                print(post)
                hours=int(post.split(" ")[0])
                print(hours)
                datepost=(now - timedelta(hours=hours)).strftime('%Y-%m-%d')
                #print(now)
            elif 'day' in post:
                day=int(post.split(" ")[0])
                datepost=(now - timedelta(days=day)).strftime('%Y-%m-%d')
            
                #print(now)
            elif 'month' in post:
                Month=int(post.split(" ")[0])
                day=Month*30
                datepost=(now - timedelta(days=day)).strftime('%Y-%m-%d')
            else:
                datepost=None
            print(type(datepost))
            insert(title,company_name,loaction,job_des,str(apply_link),jid,post,Wmode,Clogo,datepost,job_search)
        
            #print(ext_dict)
            #exdta.append(ext_dict)
        #return(exdta)
    datas=re.findall(r'\[\[\[\[\{.*?491935102.*?\[\[\[\[(.*?)]]]]]',soup,re.DOTALL | re.MULTILINE)
    print(len(datas))
    jobs=extract(datas)
    #print(job)
    nextid=re.findall(r'jsname="Yust4d".*?data-async-fc="(.*?)" data-a',soup)
    #print(nextid)item

    # page=1
    # while nextid:
    #     #print(datetime.datetime.now())
    #     time.sleep(20)
    #     #print(datetime.datetime.now())
    #     nextid=nextid[0]
    #     next_url=f'https://www.google.com/async/callback:550?fc={nextid}&fcv=3&vet=12ahUKEwiZ69Wjn9mMAxWjd2wGHUQvHMAQw40IegQIJBAO..i&ei=X-b9Z9m_GaPvseMPxN7wgAw&opi=89978449&sca_esv=a5672ed9c1a134ac&udm=8&yv=3&cs=0&async=_basejs:%2Fxjs%2F_%2Fjs%2Fk%3Dxjs.s.en_GB.7dq7KLbWqlg.2018.O%2Fam%3DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAABAAAUBIAAAAAAAAAAgAAQAAAAAAACAAQAAAAAAAAkIAAFBAgAAAAAIAAAAAAAAEwCAgGAFAKAAAAAAAAAAAAAAEAAAAAAQEAHwvn8wAAAAAAAAAAAAAAAAAAAEQAIAAAAAAAAAuAAAEAAHABCyCxAAAAAAAAAAAAQAAAAAAAAIAAAAAABAAAAAAAUAAAAAAAAAABAAAAAAAAAACAAAACAAAEAAAAAAAAAAAAAAAAAAAAAAACAAgAYAAAoAIIAfAAAAAAAABwAAAKAAAAAAOMYoAAIAAAAAAADyAPB4AIcUFAAAAAAAAAAAAAAAAASgIJgD6RcECAAAAAAAAAAAAAAAAAAAIEXQxLUGAAg%2Fdg%3D0%2Fbr%3D1%2Frs%3DACT90oEJRBK8Jld4KzC7cG12n5RtfwNYWw,_basecss:%2Fxjs%2F_%2Fss%2Fk%3Dxjs.s.JLbRv4firFU.L.B1.O%2Fam%3DAIQjEAIAAAABAAAgBIAKQAAAAAAAAAAAAAAAAAAAAAAAAAAAEgAAAEAAAAAAAAAQAGAMEAEABGYKAAAAgOAEAGQHAAAAAD4AADgVABAAAAAAAAFAAgAAAAAAAAgA0BMAEhAAABAFAAAAAAQIQhgAIAAAGwAAkAgAAEEAAIAgYAAAGQAAAAAgAABOBQDEAQAQAAAGAgCOgAAgAQAAABAKC4AAAACUIAAAAAAAAAUAAAAIAAAQAYBDMAyAQAWAATgCAAAAACIAIBAAAAAIABACAGIAgAIAQIAAwAMAAvABAAAgASIAADTAAAQIAAoBAAGAHwAgAAAAIAEAABAAgCIAOMYoAAIAAAAAAACQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAQ%2Fbr%3D1%2Frs%3DACT90oGkyCX8g6nBXeIixUwdgWWyVEDqhg,_basecomb:%2Fxjs%2F_%2Fjs%2Fk%3Dxjs.s.en_GB.7dq7KLbWqlg.2018.O%2Fck%3Dxjs.s.JLbRv4firFU.L.B1.O%2Fam%3DAIQjEAIAAAABAAAgBIAKQAAAAAAAAAAAAAAAAAAAAAAAAAAAEgAAAEAAAAAAAAAQAGBMEAUBJGYKAAAAgOAkAGQHAAAAAD6AATgVABAAAAkIAAFBAgAAAAAIAAgA0BMAExCAgHAFAKAAAAQIQhgAIAAAGwAAkAgQEEHwvv8wYAAAGQAAAAAgAABOBQDEQQIQAAAGAgCOuAAgEQAHABC6C5AAAACUIAAAAAQAAAUAAAAIAAAQAYBDMAyAQAWAATgCAAAAADIAIBAAAAAICBACAGIAgEIAQIAAwAMAAvABAAAgASIAADTAgAYIAAoBIIGfHwAgAAAAJwEAALAAgCIAOMYoAAIAAAAAAADyAPB4AIcUFAAAAAAAAAAAAAAAAASgIJgD6RcECAAAAAAAAAAAAAAAAAAAIEXQxLUGAAg%2Fd%3D1%2Fed%3D1%2Fdg%3D0%2Fbr%3D1%2Fujg%3D1%2Frs%3DACT90oGLK-4mHY6SD0g-PDy8Qw8STM-Kyw,_fmt:prog,_id:fc_X-b9Z9m_GaPvseMPxN7wgAw_2'
    #     response = requests.get(next_url,
    #     #cookies=cookies,
    #     headers=headers)
    #     print(f'page{response.status_code}')
    #     #res=response.content.decode('unicode_escape')
    #     res=response.content.decode('unicode_escape')
    #     #res=res.content
    #     #res=response.content.decode('utf-8', errors='replace')
    #     next_data=re.findall(r'\[\[\[\[\{.*?491935102.*?\[\[\[\[(.*?)]]]]]',res)
    #     #print(next_data)
        
    #     #next_data=ast.literal_eval(next_data)
    #     #next_data=next_data.encode('latin1',errors='ignore')
    #     page_job=extract(next_data)
    #     #jobs.extend(page_job)
    #     if re.findall(r'jsname="Yust4d".*?data-async-fc="(.*?)" data-a',res):
    #         nextid=re.findall(r'jsname="Yust4d".*?data-async-fc="(.*?)" data-a',res)
    #         pass
    #     else:
    #         nextid=''
    #     #print(page_job)
    #     #print(nextid)
    #     page+=1
    #     #if page==3:
    #     if nextid=='':
    #         print('all page extrac')
    #         break
            
    cursor.execute("select * from  job")
    nuumber_rows=cursor.fetchall()
    nuumber_rows=cursor.rowcount
    print(f'{nuumber_rows} Number jobs inserted ')
    # #df=pd.DataFrame(jobs)
    # #df.to_csv('google.csv')
except Exception as e:
    print(e)
