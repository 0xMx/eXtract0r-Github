from bs4 import BeautifulSoup as bs4 
import requests as rq 
import re
import os 


banner = """

  ___                        _                _ 
 / _ \__  __ /\/\   ___  ___| |__   __ _ _ __(_)
| | | \ \/ //    \ / _ \/ __| '_ \ / _` | '__| |
| |_| |>  </ /\/\ \  __/\__ \ | | | (_| | |  | |
 \___//_/\_\/    \/\___||___/_| |_|\__,_|_|  |_|
                                                
                                           
            By; Meshari-Almalki
            Twitter: @slv0d                                     
            

"""

print(banner)

def githubTools():
    header={'Host':'github.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate, br',
    'Connection':'keep-alive',
    'Cookie':'_gh_sess=KFVApFOyA6S3tV0UM6F9KLFHbRx7mC3XS%2BOAT5di%2FVjsS8V1Jrm5gzrMzG81496zkCEPY1ZSYB8keQUhwRp2W7VNvTJgoM674%2B%2BSc%2BlkWAZ6j2dVTdlAnPFu0UEVaxBjHFtWbRg1OhMQ0cBIeyYPUgBi3S6viynrQVl1UShUwqGYawUN%2BPUlDK4iWGGMqu%2BTxM0xKLRAzvoUiEsd4knn2hfND0qjevcb15sehLfaYira1Y5plbRVBUo%2BiLS0qVV81bkIXjiCU2SN6fpjmlo%2FKg%3D%3D--jWwTcqWLp18PGMFl--6Tm1NORcNnfTbZDemtan7Q%3D%3D; _octo=GH1.1.909761208.1632468008; logged_in=no; tz=America%2FLos_Angeles',
    'Upgrade-Insecure-Requests':'1',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'none',
    'Sec-Fetch-User':'?1',
    'If-None-Match':'W/"a36e1931e30c82d24240660456233235"',
    'Cache-Control':'max-age=0'}

    url= input('Enter Url of github : ')
    f=open('temp.txt','w')
    sender = rq.get(url,headers=header).text
    # print(sender.text)
    html = bs4(sender, 'lxml')
    href = html.find('div', class_='Box-body px-5 pb-5').findAll('a')
    for a in href:
        f.write(a['href'])
        f.write('\n')



githubTools()

f = open('temp.txt','r')
url = open('sources.txt','w')
for i in f.read().splitlines():
    urls = re.findall(r'https?://[^\s]+',str(i))
    for x in urls:
        url.write(f"{x}\n")
os.remove("temp.txt")