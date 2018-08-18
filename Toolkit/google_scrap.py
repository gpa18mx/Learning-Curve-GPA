from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.request import Request
from urllib.request import HTTPCookieProcessor as HCProc
from urllib.request import build_opener as bo
import http.cookiejar

import pandas as pd
import random

user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
                  'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/99.0',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991',
             'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, como Gecko) Chrome / 66.0.3359.181 Safari / 537.36 ',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36 ']

def google_search(values, num = 10, pais = "MX",ua=user_agent ):
    global user_agent_list
    user_agent_list = ua
    code = []
    descriptions_db = []
    url_db = []
    # Simulate a Browser
    user_agent = random.choice(user_agent_list)
    #Set the headers
    headers = {'User-Agent': user_agent}
    #set cookies
    cj = http.cookiejar.CookieJar()
    op = bo(HCProc(cj))
    #setting url characteristics
    search_org = values
    num_fix = num
    country_code = pais
    separator = "+"
    #cleaning the name to search
    word = search_org.split(' ')
    search = separator.join(word)
    #defining the url
    #my_url = 'https://www.google.com.mx/search?as_epq='+search+"&num="+str(num)
    my_url = 'https://www.google.com/search?q='+search+"&num="+str(num_fix)+"&cr=country"+country_code
    agent="\n\033[36m\033[1mAgent Used:\033[0m"
    print(my_url,agent, user_agent)
    #opening up connections, grabbing the page
    req = Request(my_url, headers=headers)
    Uclient2 = op.open(req)
    page_html = Uclient2.read()
    Uclient2.close()
    #uClient = uReq(req)
    #page_html = uClient.read()
    #uClient.close()
    #html parsing
    page_soup= soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class":"rc"})
    for container in containers:
        url = container.a["href"]
        desc = container.div.findAll("span", {"class":"st"})
        try:
            description = desc[0].text
        except:
            description = ''
            pass
        descriptions_db.append(str(description))
        url_db.append(str(url))

    number_values = len(url_db)
    for _ in range(number_values):
        code.append(str(search_org))

    df = pd.DataFrame(
    {'Code': code,
     'Url': url_db,
     'Description': descriptions_db
    })

    return df
