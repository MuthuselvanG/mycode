import re,requests
from bs4 import BeautifulSoup
headers = {'Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',}
resp=requests.get("https://apna.co/job/coimbatore/data-analyst-463089022?search=true", headers=headers,timeout=10)
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
    if re.findall(r'<div class="flex-1"><p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Work location</p>.*?\[24px]">(.*?)</p></div>',res):
        location=re.findall(r'<div class="flex-1"><p class="m-0 text-sm leading-\[20px] text-\[#8C8594] md:leading-\[24px]">Work location</p>.*?\[24px]">(.*?)</p></div>',res)
    else:
        location=""
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

    print(JobTite,location,Category,Deparment)