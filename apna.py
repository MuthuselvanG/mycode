import re,requests
from bs4 import BeautifulSoup
import html as parser1
import json
from datetime import datetime,time
import  time

headers = {'Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',}

params = {
    'search': 'true',
    'text': 'Data Analyst',
    'entity_id': '10039789',
    'entity_type': 'JobTitle',
    'raw_text_correction': 'true',
    #'session_id': '4985ffdd-d4f4-44f8-9df8-1f11608a326c',
    'page': '1',
    'page_size': '14',
}

response = requests.get('https://production.apna.co/user-profile-orchestrator/public/v1/jobs/', params=params, headers=headers)

#print(response.text)
soup=json.loads(response.text)
count=soup['count']/14
for page in range(1,int(count)+1):
    time.sleep(20)
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
    for i in range(1,len(results)):
        time.sleep(10)
        print(i)
        Jid=soup['results']['jobs'][i]['id']
        Jurl=soup['results']['jobs'][i]['public_url']
        print(Jid,Jurl)

        resp=requests.get(Jurl, headers=headers,timeout=10)
        print(resp.status_code)
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
                Workmode=""
            if re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Employment type</p>.*?\[24px]">(.*?)</p></div>',res):
                worktype=re.findall(r'<p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Employment type</p>.*?\[24px]">(.*?)</p></div>',res)
            else:
                worktype=""
            if re.findall(r'<div class="styles__DescriptionTextFull-sc-1532ppx-9 bHTOGx"><div><p><p>(.*?)</div>',res):
                JD=re.findall(r'<div class="styles__DescriptionTextFull-sc-1532ppx-9 bHTOGx"><div><p><p>(.*?)</div>',res)
            else:
                JD=""
            # if re.findall(r'<div class="flex-1"><p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Work location</p>.*?\[24px]">(.*?)</p></div>',res):
            #     location=re.findall(r'<div class="flex-1"><p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Work location</p>.*?\[24px]">(.*?)</p></div>',res)
            # else:
            #     location=""
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
            # Jd=re.sub(r'<.*?>','',JD)

            print(JobTite,location)