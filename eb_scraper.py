import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import numpy as np
from numpy import percentile
from scipy.stats import iqr, kurtosis, kurtosistest
from unicodedata import normalize
import MySQLdb
import time
plt.style.use('fivethirtyeight')
from random import shuffle
from requests.exceptions import ProxyError,SSLError,ConnectTimeout,ReadTimeout,ConnectionError,ChunkedEncodingError
import ast
import time
pd.set_option('display.max_colwidth',-1)

def rotate(l, n):
    return l[n:] + l[:n]

def eb_scraper(urls,proxies):

    sleep = [3,4,5,6,7,8,9,10]
    times = 0

    headers = [{'User-Agent':"Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"},
                {'User-Agent':"Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0"},
                {'User-Agent':"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/62.0"},
                {'User-Agent':"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.13; ko; rv:1.9.1b2) Gecko/20081201 Firefox/60.0"},
                {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"},
                {'User-Agent':"Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko"},
                {'User-Agent':"Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0"},
                {'User-Agent':"Mozilla/5.0 (PLAYSTATION 3; 3.55)"},
                {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"},
                {'User-Agent':"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0"},
                {'User-Agent':"wii libnup/1.0"},
                {'User-Agent':"Googlebot/2.1 (+http://www.googlebot.com/bot.html)"},
                {'User-Agent':"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"},
                {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"},
                {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko"},
                {'User-Agent':"Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko"},
                {'User-Agent':"Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0"},
                {'User-Agent':"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)"},
                {'User-Agent':"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"},
                {'User-Agent':"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"},
                {'User-Agent':"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)"},
                {'User-Agent':"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)"},
                {'User-Agent':"Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"},
                {'User-Agent':"Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"}]
    shuffle(headers)

    titles = []
    prices = []
    links = []

    html_soup = []

    for url in urls:
        while True:
            try:
                for proxy in proxies:
                    for header in headers:
                        r = requests.get(url,proxies=proxy,headers=header,timeout=2)
                        shuffle(headers)
                        break
                    html_content = r.text
                    html_soup.append(BeautifulSoup(html_content,"html.parser"))
                    times += 1
                    proxies = rotate(proxies,1)
                    print('Page',times,'done')
                    print ('Link:',url)
                    print ('Proxy:',proxy)
                    print ('Header:',header)
                    for s in sleep:
                        print('Sleeping',s,'seconds')
                        time.sleep(s)
                        shuffle(sleep)
                        break
                    break
            except SSLError:
                print('SSLError, rotating proxies...',proxy)
                proxies = rotate(proxies,1)
                continue
                break
            except ProxyError:
                print('ProxyError, rotating proxies...',proxy)
                proxies = rotate(proxies,1)
                continue
                break
            except ConnectTimeout:
                print('ConnectTimeout, rotating proxies...',proxy)
                proxies = rotate(proxies,1)
                continue
                break
            except ReadTimeout:
                print('ReadTimeout, rotating proxies...',proxy)
                proxies = rotate(proxies,1)
                continue
                break
            except ConnectionError:
                print('ConnectionError, rotating proxies...',proxy)
                proxies = rotate(proxies,1)
                continue
                break
            except ChunkedEncodingError:
                print('Connection broken, rotating proxies...',proxy)
                proxies = rotate(proxies,1)
                continue
                break

                continue
            break

    for t in html_soup:
        T = t.findAll('h3',class_='s-item__title',attrs={'role':'text'})
        for title in T:
            titles.append(title.text)

    for p in html_soup:
        P = p.findAll('span',class_='s-item__price')
        for price in P:
            prices.append(int(price.text.replace(',','').split()[1][1:-3]))

    for l in html_soup:
        L = l.findAll('a',class_='s-item__link',href=True)
        for link in L:
            links.append(link['href'])




    print(len(titles),len(prices))

    df = pd.DataFrame({'Title':titles,
                       'Price':prices,
                       'Link':links})

    return df
