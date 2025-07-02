import re,requests
from bs4 import BeautifulSoup
import html as parser1
import json
from datetime import datetime,time
import  time
import pandas as pd


headers = {'Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',}
#tttttttttttttttt
params = {
    'location_id': '1',
    'location_identifier': '1',
    'location_type': 'State',
    'location_name': 'Tamil Nadu',
    'search': 'true',
    'text': 'Data Analyst',
    'entity_id': '226',
    'entity_type': 'JobTitle',
    'raw_text_correction': 'true',
    #'session_id': 'f60c3e33-6d0a-4521-aa2c-b0a08925375e',
    'page': '2',
    'page_size': '14',
}

response = requests.get('https://production.apna.co/user-profile-orchestrator/public/v1/jobs/', params=params, headers=headers)

#print(response.text)
soup=json.loads(response.text)
total_Result=[]
count=soup['count']/14
for page in range(1,2):
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
        Jid=soup['results']['jobs'][i]['id']
        Jurl=soup['results']['jobs'][i]['public_url']
        print(Jid,Jurl)

        resp=requests.get(Jurl, headers=headers,timeout=10)
        time.sleep(5)
        #print(resp.status_code)
        res=resp.text
        if re.findall(r'class="m-0 truncate text-wrap text-md font-semibold text-\[\#190A28\]">(.*?)</p>',res):
            if re.findall(r'class="m-0 truncate text-wrap text-md font-semibold text-\[\#190A28\]">(.*?)</p>',res):
                JobTite=re.findall(r'class="m-0 truncate text-wrap text-md font-semibold text-\[\#190A28\]">(.*?)</p>',res)
            else:
                JobTite=""
            if re.findall(r'class="m-0 truncate text-wrap text-md font-semibold text-\[\#190A28\]">.*?class="m-0 text-sm text-\[\#8C8594\]">(.*?)</p>',res):
                CName=re.findall(r'class="m-0 truncate text-wrap text-md font-semibold text-\[\#190A28\]">.*?class="m-0 text-sm text-\[\#8C8594\]">(.*?)</p>',res)
            else:
                CName=""
            if re.findall(r'class="m-0 truncate text-sm text-\[\#8C8594\]">(.*?)</p>',res):
                location=re.findall(r'class="m-0 truncate text-sm text-\[\#8C8594\]">(.*?)</p>',res)
            else:
                location=""
            if re.findall(r'class="m-0 truncate text-sm text-\[\#8C8594\]">.*?class="m-0 text-sm text-\[\#8C8594\]">(.*?)</p>',res):
                salry=re.findall(r'class="m-0 truncate text-sm text-\[\#8C8594\]">.*?class="m-0 text-sm text-\[\#8C8594\]">(.*?)</p>',res)
            else:
                salry=""
            if re.findall(r'<div class="flex items-center gap-\[4px]">.*?-\[#8C8594]">(.*?)</p>',res):
                Workmode=re.findall(r'<div class="flex items-center gap-\[4px]">.*?-\[#8C8594]">(.*?)</p>',res)
            else:
                Workmode=''
            if re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Employment type</p>.*?\[24px]">(.*?)</p></div>',res):
                worktype=re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Employment type</p>.*?\[24px]">(.*?)</p></div>',res)
            else:
                worktype=""
            if re.findall(r'<div class="styles__DescriptionTextFull-sc-1532ppx-9 bHTOGx"><div>(.*?)</div>',res):
                JD=re.findall(r'<div class="styles__DescriptionTextFull-sc-1532ppx-9 bHTOGx"><div>(.*?)</div>',res)
            else:
                JD=""
            if re.findall(r'<div class="flex-1"><p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Work location</p>.*?\[24px]">(.*?)</p></div>',res):
                Clocation=re.findall(r'<div class="flex-1"><p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Work location</p>.*?\[24px]">(.*?)</p></div>',res)
            else:
                Clocation=""
            if re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Department</p>.*?\[24px]">(.*?)</p></div>',res):
                Deparment=re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Department</p>.*?\[24px]">(.*?)</p></div>',res)
            else:
                Deparment=""
            if re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Role / Category</p>.*?\[24px]">(.*?)</p></div>',res):
                Category=re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Role / Category</p>.*?\[24px]">(.*?)</p></div>',res)
            else:
                Category=""
            if re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Shift</p>.*?\[24px]">(.*?)</p></div>',res):
                shift=re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Shift</p>.*?\[24px]">(.*?)</p></div>',res)
            else:
                shift=''
            # Jd=re.sub(r'<.*?>','',JD)

            # data={'JobTite':JobTite[0],'CName':CName[0],'location':location[0],'salry':salry[0],'Workmode':Workmode[0],
            #       'worktype':worktype[0],'JD':JD[0],'Deparment':Deparment[0],'Category':Category[0],'shift':shift[0],"PageNumber":page,'Jurl':Jurl,
            #       'Jid':Jid}
            data={'JobTite':JobTite,'CName':CName,'Clocation':Clocation,'location':location,'salry':salry,'Workmode':Workmode,
                  'worktype':worktype,'JD':JD,'Deparment':Deparment,'Category':Category,'shift':shift,"PageNumber":page,'Jurl':Jurl,
                  'Jid':Jid}
            
            total_Result.append(data)
df=pd.DataFrame(total_Result)
df.to_excel("job.xlsx")