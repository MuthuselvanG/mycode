import re,requests
from bs4 import BeautifulSoup
import html as parser1
import json
from datetime import datetime,time
import  time
import pandas as pd
import pymysql


db=pymysql.connect(host='localhost',user='root',password='@ggreg@te',database='Traning')
input_table='apnajob_input'
out_table = 'apnajob1'
print('db connected')
cursor=db.cursor()
cursor.execute(f'select id,search_word,status  from {input_table} where status=0')
def update(status,input_id):
        cursor.execute(f'update {input_table} set status=(%s) where id=(%s)',(status,input_id))
        print(f'{status} - updated')
        
def insert(jdata):#(jid,JobTite,Cname,Clocation,pdate,expiry,salary,experice,description,Workmode,worktype,category,deparment,shift,Refurl,appliedurl,page):
            

            try:
                cursor.execute('insert into '+out_table+'(jobid,jobtitle,Postdate,expireddate,cname,cloaction,salary,experience,workmode,worktype,description,deparment,Category,shift,appliedurl,Pagenum,joburl,input_id)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                                    (jdata))#(jid,JobTite,pdate,expiry,Cname,Clocation,salary,experice,Workmode,worktype,description,deparment,category,shift,appliedurl,page,Refurl,input_id))
                db.commit()
                print(f'{jdata[0]} - inserted')
                update(2,jdata[-1])
                cursor.close()
            except Exception as e:
                print(e)

inputs=cursor.fetchall()
for input in inputs:
    inputid=input[0]
    search_word=input[1]
    status=input[2]
    print(inputid,search_word,status)

    cursor.execute(f'select jobid from {out_table} where (%s)',(inputid))
    tdata=cursor.fetchall()
    column=cursor.description

    tdata=list(d[0]for d in tdata)
    #print(column)
    

    headers = {'Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',}

    params = {
        'location_id': '1',
        'location_identifier': '1',
        'search': 'true',
        'text': search_word,
        'entity_id': '226',
        'entity_type': 'JobTitle',
        'raw_text_correction': 'true',
        #'session_id': 'f60c3e33-6d0a-4521-aa2c-b0a08925375e',
        'posted_in': '72',
        'page': '1',
        'page_size': '14',
    }

    response = requests.get('https://production.apna.co/user-profile-orchestrator/public/v1/jobs/', params=params, headers=headers)

    #print(response.text)
    soup=json.loads(response.text)
    Totaljob=1#soup['count']
    if len(tdata)==0:
        print(Totaljob)
        if Totaljob>14:
            if (Totaljob%14)==0:
                expagecount=int(Totaljob/14)
            else:
                expagecount=int(Totaljob/14)+1
        else:
            expagecount=2
        print(expagecount)
    else:
        print(Totaljob)
        expagecount=2
        print(expagecount)
    jids=[]
    for page in range(1,expagecount):
        print(page ,'-',response.status_code )
        params = {
            'search': 'true',
            'text': 'Data Analyst',
            'entity_id': '10039789',
            'entity_type': 'JobTitle',
            'raw_text_correction': 'true',
            #'session_id': '4985ffdd-d4f4-44f8-9df8-1f11608a326c',
            'page': page,
            'page_size': '14',
        }

        response = requests.get('https://production.apna.co/user-profile-orchestrator/public/v1/jobs/', params=params, headers=headers)

        print(response.status_code,page)
        results=soup['results']['jobs']
        print(len(results))
        time.sleep(10)
        for i in range(1,len(results)):
            print(i)
            #Jid=soup['results']['jobs'][i]['id']
            Jurl=soup['results']['jobs'][i]['public_url']
            #print(Jurl)

            resp=requests.get(Jurl, headers=headers,timeout=10)
            print(f'jobpage -{resp.status_code}')
            #print(f'jobpage -{resp.status_code}')
            res=resp.text
            datas=re.findall(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',res)
            open ('dummy.txt','w').write(datas[0])
            data=json.loads(datas[0])
            job=data['props']['pageProps']['job']
            jid=job['id']
            JobTite=job['title']
            pdate=job['created_on']
            if 'expiry' in job:
                expiry=job['expiry']
            else:
                expiry=''
            if 'fixed_min_salary' in job:
                minsalary=job['fixed_min_salary']
            else:
                minsalary=''
            if 'fixed_max_salary' in job:
                    maxsalary=job['fixed_max_salary']
            else:
                maxsalary=''
            if minsalary=='':
                salary=''
            elif maxsalary=='':
                salary=minsalary
            else:   
                salary=str(minsalary)+' - '+str(maxsalary)
            description=job['description']
            experice=job['experience_in_years']
            Workmode=job['ui_tags'][0]['text']
            worktype=job['employment_type']
            #shift=job['job_details_section'][4]
            if 'shift' in job:
                shift=job['shift']
            else:
                shift=''
            category=job['job_category']
            if 'job_department' in job:
                deparment=job['job_department']
            else:
                deparment=''
            Cname=job['organization']['name']
            if 'interview_details' in job:
                Clocation=job['interview_details']['data'][0]['sub_heading']
            elif 'address' in job:
                Clocation=job['address']['line_1']
            else:
                Clocation=''
            #experice=data.get('props',{}).get('pageProps',{}).get('job',{}).get('ui_tags',{})
            #experice=data['props']['pageProps']['job']['ui_tags'][2]['text']
            if 'public_url' in job:  
                Refurl=job['public_url']
            elif 'public_url_v2' in job:
                Refurl=job['public_url_v2']
            if 'external_job_url' in job:
                appliedurl=job['external_job_url']
            else:
                appliedurl=''
            print(shift,deparment)
            #print(jid,JobTite,pdate,expiry,salary,experice,description,Workmode,worktype,shift,category,deparment,Cname,Clocation,Refurl)
            #data=[jid,JobTite,Cname,Clocation,pdate,expiry,salary,experice,description,Workmode,worktype,category,shift,deparment,Refurl,appliedurl,page]
            data=[jid,JobTite,pdate,expiry,Cname,Clocation,salary,experice,Workmode,worktype,description,deparment,category,shift,appliedurl,page,Refurl,inputid]
            jids.append(data)
        #insert(jid,JobTite,Cname,Clocation,pdate,expiry,salary,experice,description,Workmode,worktype,category,shift,deparment,Refurl,appliedurl,page)
    for jdata in jids:
        if jdata[0] not in tdata:
            insert(jdata)
            #print(jdata)
        else:
            print(f'{jdata[0]} - already insert')

            # if re.findall(r'class="m-0 truncate text-wrap text-md font-semibold text-\[\#190A28\]">(.*?)</p>',res):
                # if re.findall(r'class="m-0 truncate text-wrap text-md font-semibold text-\[\#190A28\]">(.*?)</p>',res):
                #     JobTite=re.findall(r'class="m-0 truncate text-wrap text-md font-semibold text-\[\#190A28\]">(.*?)</p>',res)
                # else:
                #     JobTite=""
                # if re.findall(r'class="m-0 truncate text-wrap text-md font-semibold text-\[\#190A28\]">.*?class="m-0 text-sm text-\[\#8C8594\]">(.*?)</p>',res):
                #     CName=re.findall(r'class="m-0 truncate text-wrap text-md font-semibold text-\[\#190A28\]">.*?class="m-0 text-sm text-\[\#8C8594\]">(.*?)</p>',res)
                # else:
                #     CName=""
                # if re.findall(r'class="m-0 truncate text-sm text-\[\#8C8594\]">(.*?)</p>',res):
                #     location=re.findall(r'class="m-0 truncate text-sm text-\[\#8C8594\]">(.*?)</p>',res)
                # else:
                #     location=""
                # if re.findall(r'class="m-0 truncate text-sm text-\[\#8C8594\]">.*?class="m-0 text-sm text-\[\#8C8594\]">(.*?)</p>',res):
                #     salry=re.findall(r'class="m-0 truncate text-sm text-\[\#8C8594\]">.*?class="m-0 text-sm text-\[\#8C8594\]">(.*?)</p>',res)
                # else:
                #     salry=""
                # if re.findall(r'<div class="flex items-center gap-\[4px]">.*?-\[#8C8594]">(.*?)</p>',res):
                #     Workmode=re.findall(r'<div class="flex items-center gap-\[4px]">.*?-\[#8C8594]">(.*?)</p>',res)
                # else:
                #     Workmode=''
                # if re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Employment type</p>.*?\[24px]">(.*?)</p></div>',res):
                #     worktype=re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Employment type</p>.*?\[24px]">(.*?)</p></div>',res)
                # else:
                #     worktype=""
                # if re.findall(r'<div class="styles__DescriptionTextFull-sc-1532ppx-9 bHTOGx"><div>(.*?)</div>',res):
                #     JD=re.findall(r'<div class="styles__DescriptionTextFull-sc-1532ppx-9 bHTOGx"><div>(.*?)</div>',res)
                # else:
                #     JD=""
                # if re.findall(r'<div class="flex-1"><p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Work location</p>.*?\[24px]">(.*?)</p></div>',res):
                #     Clocation=re.findall(r'<div class="flex-1"><p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Work location</p>.*?\[24px]">(.*?)</p></div>',res)
                # else:
                #     Clocation=""
                # print(Clocation)
                # if re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Department</p>.*?\[24px]">(.*?)</p></div>',res):
                #     Deparment=re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Department</p>.*?\[24px]">(.*?)</p></div>',res)
                # else:
                #     Deparment=""
                # if re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Role / Category</p>.*?\[24px]">(.*?)</p></div>',res):
                #     Category=re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Role / Category</p>.*?\[24px]">(.*?)</p></div>',res)
                # else:
                #     Category=""
                # if re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Shift</p>.*?\[24px]">(.*?)</p></div>',res):
                #     shift=re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Shift</p>.*?\[24px]">(.*?)</p></div>',res)
                # else:
                #     shift=''
                # # Jd=re.sub(r'<.*?>','',JD)
                # print(JobTite)

                # data={'JobTite':JobTite[0],'CName':CName[0],'location':location[0],'salry':salry[0],'Workmode':Workmode[0],
                #       'worktype':worktype[0],'JD':JD[0],'Deparment':Deparment[0],'Category':Category[0],'shift':shift[0],"PageNumber":page,'Jurl':Jurl,
                #       'Jid':Jid}
                # # data={'JobTite':JobTite,'CName':CName,'Clocation':Clocation,'location':location,'salry':salry,'Workmode':Workmode,
                # #       'worktype':worktype,'JD':JD,'Deparment':Deparment,'Category':Category,'shift':shift,"PageNumber":page,'Jurl':Jurl,
                # #       'Jid':Jid}
                # print(data)
    #             j.append(data)
    #             print(data)
    #     jids.extend(j)    
    #         #insert(Jid,JobTite,CName,Clocation,location,salry,Workmode,worktype,JD,Deparment,Category,shift,page,Jurl)        
    #             #total_Result.append(data)
    # # df=pd.DataFrame(total_Result)
    # # df.to_excel("job.xlsx")
    # print(jids)
            #insert(Jid,JobTite,CName,Clocation,location,salry,Workmode,worktype,JD,Deparment,Category,shift,page,Jurl)'''