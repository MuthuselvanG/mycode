import requests,re
from bs4 import BeautifulSoup

#headers = {'Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',}




import requests

cookies = {
    'CTK': '1iteqppaviaj3800',
    'RF': '"TFTzyBUJoNr6YttPP3kyivpZ6-9J49o-Uk3iY6QNQqKE2fh7FyVgtd5HRlA72jHvYM_BYCa5_9I="',
    'SURF': '9cFzt57tPrrw9mlvYHVeMIZobfJfjBX9',
    '_ga': 'GA1.1.704871216.1749623307',
    'FPID': 'FPID2.2.bzYJquN7lGubfKRlaa%2FnUEdbbr5Evub99hnu8y8lGWY%3D.1749623307',
    'LC': '"co=IN"',
    'LOCALE': 'en_IN',
    'IRF': '7YXfKDzcx1JT-QT4QnjgSBxoeWd-bJfGJVEnksMzWzzhLYVke-XK0A==',
    #'_gcl_au': '1.1.1873797544.1749623798',
    #'optimizelySession': '1749623813947',
    '_ga_5KTMMETCF4': 'GS2.1.s1749623798$o1$g1$t1749623815$j43$l0$h0',
    'CO': 'IN',
    'CO': 'IN',
    'LOCALE': 'en_IN',
    'indeed_rcc': 'LOCALE:PREF:LV:CTK:CO:RQ',
    'INDEED_CSRF_TOKEN': 'hyI99EOFhPfXmhOVA2xovfphs7JszZ1J',
    'LV': 'LA=1749716087:LV=1749629072:CV=1749716087:TS=1749623301',
    '_cfuvid': 'bwjpgEcSS2jjiW4okeQn3L8CEorgsSYH1PTVTCySQiA-1749716087944-0.0.1.1-604800000',
    'FPLC': 'mAnf%2FaWJuDHzCM4VomzafCNlflPEUxEWXfU65j9zpZLa34ejy2Mqrf4qxkaRNGc1cxq%2BGEKHyal9vt%2BJpWCd4uzah8u%2BD8Baa5zg5eGuWB5ZNkfYaBrNLBEe8dZlsg%3D%3D',
    'MICRO_CONTENT_CSRF_TOKEN': 'KRzpZEC59cSN70COlFQOFTz05tAsWXQF',
    'RSJC': '2ab926492ae799aa:1b10f6d5a37e94ea:d81deb904040c139:2a34c0e3822fa1f2:582378155f241069',
    'SHARED_INDEED_CSRF_TOKEN': 'hyI99EOFhPfXmhOVA2xovfphs7JszZ1J',
    'PREF': '"TM=1749717497006:L=coimbatore%2C+tamil+nadu"',
    'ROJC': 'df8633cc730d7cf6:ca692bb9e842fe2c:7c04cebd511ed667:16d7fad7b2039525:87d8f37af211e4a2:1c1db7ab31116a7d',
    'RQ': '"q=data+entry&l=coimbatore%2C+tamil+nadu&ts=1749717612899:q=&l=coimbatore%2C+tamil+nadu&ts=1749717497007&pts=1749629328043:q=work+from+home&l=&ts=1749716139212:q=fresher&l=Coimbatore%2C+Tamil+Nadu&ts=1749623348463"',
    'JSESSIONID': 'node017bbsyzsuftg3o17qh0d69gc91884735.node0',
    '__cf_bm': 'NrhF49hgx_AqBJp1WdhEYe3ABcW1yIMXT8hSVc4_Bzg-1749721577-1.0.1.1-Hutuw2MhschIHDYTQPReOa..9HT7KYio0XyeXN0HB3wmkmJfjxbVlz9vHpqC3XfjkihsS8xyNXMSQsQwZQcNzWGRn9sQ5vTNwL9BDVX2TRg',
    'cf_clearance': 'qESGKwfM0Wmndr1bQcUavFa.AbkaUp68nZ65qHYUnoE-1749721612-1.2.1.1-dj4kictZvavufIc7KP8QgHophGsRpV7F7OBYgi3psU0FNkL07yZ8mjkaa3mGfAEeXQj_h8.H8G6leXZnVfyzQkOTNc4PrNP7pPpDYhECZO3otpigBGiDGCVwgMw9vMdPS.wzhGWxYZiI5ZkieUtOLfdFUCw5JpXocJmohEz7w71c33m0g1n8xTHSlf0UQke5L0iRSGDpgFY9qiVOhzwoO_pY817iAKwoy420BivcK8kJVXxyYLfvW9UgydhvJSbPODKsyZm3RFtBDFRBGvcVqHVt.Kgu5fH0gFzQxafgc7y.otEkTL86rr9OmCSJLuVvr1rTAfhPKbFIUfj1GtrgQJy7wTVNEtxW4FvHL4UaRs5bSnpPlP3vQFq02HH6u4kv',
    '_ga_LYNT3BTHPG': 'GS2.1.s1749721611$o4$g0$t1749721611$j60$l0$h1343556621',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"137.0.7151.55"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="137.0.7151.55", "Chromium";v="137.0.7151.55", "Not/A)Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '"6.8.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': 'CTK=1iteqppaviaj3800; RF="TFTzyBUJoNr6YttPP3kyivpZ6-9J49o-Uk3iY6QNQqKE2fh7FyVgtd5HRlA72jHvYM_BYCa5_9I="; SURF=9cFzt57tPrrw9mlvYHVeMIZobfJfjBX9; _ga=GA1.1.704871216.1749623307; FPID=FPID2.2.bzYJquN7lGubfKRlaa%2FnUEdbbr5Evub99hnu8y8lGWY%3D.1749623307; LC="co=IN"; LOCALE=en_IN; IRF=7YXfKDzcx1JT-QT4QnjgSBxoeWd-bJfGJVEnksMzWzzhLYVke-XK0A==; _gcl_au=1.1.1873797544.1749623798; optimizelySession=1749623813947; _ga_5KTMMETCF4=GS2.1.s1749623798$o1$g1$t1749623815$j43$l0$h0; CO=IN; CO=IN; LOCALE=en_IN; indeed_rcc=LOCALE:PREF:LV:CTK:CO:RQ; INDEED_CSRF_TOKEN=hyI99EOFhPfXmhOVA2xovfphs7JszZ1J; LV=LA=1749716087:LV=1749629072:CV=1749716087:TS=1749623301; _cfuvid=bwjpgEcSS2jjiW4okeQn3L8CEorgsSYH1PTVTCySQiA-1749716087944-0.0.1.1-604800000; FPLC=mAnf%2FaWJuDHzCM4VomzafCNlflPEUxEWXfU65j9zpZLa34ejy2Mqrf4qxkaRNGc1cxq%2BGEKHyal9vt%2BJpWCd4uzah8u%2BD8Baa5zg5eGuWB5ZNkfYaBrNLBEe8dZlsg%3D%3D; MICRO_CONTENT_CSRF_TOKEN=KRzpZEC59cSN70COlFQOFTz05tAsWXQF; RSJC=2ab926492ae799aa:1b10f6d5a37e94ea:d81deb904040c139:2a34c0e3822fa1f2:582378155f241069; SHARED_INDEED_CSRF_TOKEN=hyI99EOFhPfXmhOVA2xovfphs7JszZ1J; PREF="TM=1749717497006:L=coimbatore%2C+tamil+nadu"; ROJC=df8633cc730d7cf6:ca692bb9e842fe2c:7c04cebd511ed667:16d7fad7b2039525:87d8f37af211e4a2:1c1db7ab31116a7d; RQ="q=data+entry&l=coimbatore%2C+tamil+nadu&ts=1749717612899:q=&l=coimbatore%2C+tamil+nadu&ts=1749717497007&pts=1749629328043:q=work+from+home&l=&ts=1749716139212:q=fresher&l=Coimbatore%2C+Tamil+Nadu&ts=1749623348463"; JSESSIONID=node017bbsyzsuftg3o17qh0d69gc91884735.node0; __cf_bm=NrhF49hgx_AqBJp1WdhEYe3ABcW1yIMXT8hSVc4_Bzg-1749721577-1.0.1.1-Hutuw2MhschIHDYTQPReOa..9HT7KYio0XyeXN0HB3wmkmJfjxbVlz9vHpqC3XfjkihsS8xyNXMSQsQwZQcNzWGRn9sQ5vTNwL9BDVX2TRg; cf_clearance=qESGKwfM0Wmndr1bQcUavFa.AbkaUp68nZ65qHYUnoE-1749721612-1.2.1.1-dj4kictZvavufIc7KP8QgHophGsRpV7F7OBYgi3psU0FNkL07yZ8mjkaa3mGfAEeXQj_h8.H8G6leXZnVfyzQkOTNc4PrNP7pPpDYhECZO3otpigBGiDGCVwgMw9vMdPS.wzhGWxYZiI5ZkieUtOLfdFUCw5JpXocJmohEz7w71c33m0g1n8xTHSlf0UQke5L0iRSGDpgFY9qiVOhzwoO_pY817iAKwoy420BivcK8kJVXxyYLfvW9UgydhvJSbPODKsyZm3RFtBDFRBGvcVqHVt.Kgu5fH0gFzQxafgc7y.otEkTL86rr9OmCSJLuVvr1rTAfhPKbFIUfj1GtrgQJy7wTVNEtxW4FvHL4UaRs5bSnpPlP3vQFq02HH6u4kv; _ga_LYNT3BTHPG=GS2.1.s1749721611$o4$g0$t1749721611$j60$l0$h1343556621',
}

params = {
    'q': 'data entry',
    'l': 'coimbatore, tamil nadu',
    'radius': '25',
    'from': 'searchOnDesktopSerp,searchSuggestions,whatautocompleteSourceSimba',
    'cf-turnstile-response': '0.rmNdMjPNHOSjuSTAnKG4zR95G2r-u9l_k38wib2YnvrCX-oxmmSBnqhf-SqwALpqHDI9vN8YUxq8pNBCL2JXVkA8Ov1mxtnxv_zrXUlJBYWNHuBqK5hjinXs-UnRh11cYl_htXSXf_w0dAqcEouh9L4QWldebwr9q4ASJvipL-iYDhNb8fgFWuDgqsAEfuvXfVtMF7ZhTBHI-YskwTFNX_Kj8lWjgcKY8cMEKLrWuZma49IP8iJOaJAjzjHm5uEJ1hvVC3C3JpiKSkytaMSVt3rXZAqZFzNqk7rnW6jh7JcmFbHQKj--2APivIN8pCaF4EFaPQ7EBayl-ADoIfvwMJWfxK6WHusV3SESa4aMM63htyCKQhcHsevXzqkh5ODTQk1yKmNOjjxnGk66iduciWLtxYncEknq2UzSvLXnAuQ25mhRoNDLpDX33YEf-T69cUm1hMvft4HvqicxRmNDmrKMvSkRw7_7T1rfz4FpG3LFKB30J6artic3RYkVt6FtACOX3ltaVrR-3v42FI3iKe7yl2NX7Umaae4XQUoLG_G-hqZBNFumanssNc1AdHWdM4WcLCxH75wdmcChfdc0hRvEU01Ls24q_Szi4EMHGQMLig08CeiCGfwr9s-MZvnpaPwr6gKaR0UvnLS9UhiUhNJfmyQrPYFJBC5lFMawnUJxy3WzPxWrgLbG8OIqTb0DqMiTdbcm79ZpJXNuisf95Yy5_7LtnK9_sZ9VjxGp_oNNsALkRTAqQs8FPXm6HIIrEe6zxW19MDrxMQbLUeiDf6BB3l3-px6aVIxkPOrkaw6mwZd_kCfTCEYIoheyLOvcEhGX40XrSGtWieklivz-fBMopUsSGU-3CkJAD3C9aP8.Z1QCY9HwCk9O1upGJmvReQ.985aac9fc9f729a107bcd7487ebc1a0205e425e75222c8b5d3105e3875d00f8b',
    'vjk': 'ca692bb9e842fe2c',
}

response = requests.get('https://in.indeed.com/jobs', params=params, cookies=cookies, headers=headers)

print(response.status_code)
open("response.html","w").write(response.text)
res=BeautifulSoup(response.text,'html.parser')
#print(res)
div=res.find_all('div',class_="job_seen_beacon")
for i in div:
    #print (i)
    a=re.get(r'<h2 class="jobTitle mosaic-provider-jobcards-1psdjh5 eu4oa1w0" tabindex="-1">',res).href()
    print(a)
    break