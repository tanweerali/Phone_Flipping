from eb_scraper import eb_scraper
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import numpy as np
from numpy import percentile
from scipy.stats import iqr, kurtosis, kurtosistest
from unicodedata import normalize
import MySQLdb
plt.style.use('fivethirtyeight')
from random import shuffle
from requests.exceptions import ProxyError,SSLError,ConnectTimeout,ReadTimeout,ConnectionError,ChunkedEncodingError
import ast
import time
from datetime import date, timedelta
from cleaning import phone
pd.set_option('display.max_colwidth',-1)

date = str(date.today())

proxy_list = []
with open('/home/REDACTED/Python/proxy/proxies.txt','r') as f:
    proxies = f.readlines()
    for proxy in proxies:
        d = ast.literal_eval(proxy)
        proxy_list.append(d)



### Iphone 6 ###

urls = []
for i in range(1,50):
    url = 'https://www.ebay.ca/b/iPhone-6/9355/bn_3897179?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6/iphone6_{}.txt'.format(date))


# 16 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6-16GB-Cell-Phones-Smartphones/9355/bn_3888385?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6/iphone6_16g_{}.txt'.format(date))

# 32 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6-32GB-Smartphones/9355/bn_15566232?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6/iphone6_32g_{}.txt'.format(date))

# 64GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6-64GB-Cell-Phones-Smartphones/9355/bn_3907343?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6/iphone6_64g_{}.txt'.format(date))

# 128 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6-128GB-Smartphones/9355/bn_3885798?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6/iphone6_128g_{}.txt'.format(date))



### Iphone 6S ###

urls = []
for i in range(1,50):
    url = 'https://www.ebay.ca/b/iPhone-6s/9355/bn_2714825?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6S/iphone6s_{}.txt'.format(date))

# 16 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-Apple-iPhone-6s-16GB-Cell-Phones-Smartphones/9355/bn_99613285?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6S/iphone6s_16g_{}.txt'.format(date))

# 32 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6s-32GB-Cell-Phones-Smartphones/9355/bn_80197281?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6S/iphone6s_32g_{}.txt'.format(date))

# 64 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6s-64GB/9355/bn_2714838?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6S/iphone6s_64g_{}.txt'.format(date))

# 128 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6s-128GB-Cell-Phones-Smartphones/9355/bn_95708157?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6S/iphone6s_128g_{}.txt'.format(date))




### Iphone 6S Plus ###

urls = []
for i in range(1,50):
    url = 'https://www.ebay.ca/b/iPhone-6s-Plus/9355/bn_2714814?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6S_Plus/iphone6splus_{}.txt'.format(date))

# 16 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6s-Plus-16GB-Cell-Phones-Smartphones/9355/bn_95708781?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6S_Plus/iphone6splus_16g_{}.txt'.format(date))

# 32 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6s-Plus-32GB-Cell-Phones-Smartphones/9355/bn_80196276?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6S_Plus/iphone6splus_32g_{}.txt'.format(date))

# 64 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6s-Plus-64GB-Cell-Phones-Smartphones/9355/bn_95708215?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6S_Plus/iphone6splus_64g_{}.txt'.format(date))

# 128 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6s-Plus-128GB/9355/bn_5570757?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6S_Plus/iphone6splus_128g_{}.txt'.format(date))


### Iphone 6 Plus ###

urls = []
for i in range(1,50):
    url = 'https://www.ebay.ca/b/iPhone-6-Plus/9355/bn_3894020?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6_Plus/iphone6plus_{}.txt'.format(date))

# 16 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6-Plus-16GB-Cell-Phones-Smartphones/9355/bn_95707652?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6_Plus/iphone6plus_16g_{}.txt'.format(date))

# 64 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6-Plus-64GB/9355/bn_3899922?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6_Plus/iphone6plus_64g_{}.txt'.format(date))

# 128 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-6-Plus-128GB/9355/bn_3901559?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6_Plus/iphone6plus_128g_{}.txt'.format(date))




### Iphone 7 ###

urls = []
for i in range(1,50):
    url = 'https://www.ebay.ca/b/iPhone-7/9355/bn_36834265?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_7/iphone7_{}.txt'.format(date))

# 32  GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-7-32GB-Smartphones/9355/bn_55140636?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_7/iphone7_32g_{}.txt'.format(date))

# 128  GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-7-128GB-Smartphones/9355/bn_55140818?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_7/iphone7_128g_{}.txt'.format(date))

# 256  GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-7-256GB-Smartphones/9355/bn_55129457?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_7/iphone7_256g_{}.txt'.format(date))



### Iphone 7 Plus ###

urls = []
for i in range(1,50):
    url = 'https://www.ebay.ca/b/iPhone-7-Plus/9355/bn_36834266?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_7_Plus/iphone7plus_{}.txt'.format(date))

# 32 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-7-Plus-32GB-Cell-Phones-Smartphones/9355/bn_95709289?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_7_Plus/iphone7plus_32g_{}.txt'.format(date))

# 128 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-7-Plus-128GB-Smartphones/9355/bn_55137302?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_7_Plus/iphone7plus_128g_{}.txt'.format(date))

# 256 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-7-Plus-256GB-Cell-Phones-Smartphones/9355/bn_95708676?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_7_Plus/iphone7plus_256g_{}.txt'.format(date))


### Iphone 8 ###

urls = []
for i in range(1,50):
    url = 'https://www.ebay.ca/b/iPhone-8/9355/bn_85259852?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_8/iphone8_{}.txt'.format(date))

# 64 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-8-64GB/9355/bn_85259902?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_8/iphone8_64g_{}.txt'.format(date))

# 256 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-8-256GB/9355/bn_85259905?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_8/iphone8_256g_{}.txt'.format(date))



### Iphone 8 Plus ###

urls = []
for i in range(1,50):
    url = 'https://www.ebay.ca/b/iPhone-8-Plus/9355/bn_85259853?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_8_Plus/iphone8plus_{}.txt'.format(date))

# 64 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-8-Plus-64GB/9355/bn_85259903?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_8_Plus/iphone8plus_64g_{}.txt'.format(date))

# 256 GB

urls = []
for i in range(1,5):
    url = 'https://www.ebay.ca/b/Apple-iPhone-8-Plus-256GB/9355/bn_85259906?LH_BIN=1&LH_PrefLoc=3&rt=nc&_pgn={}'.format(i)
    urls.append(url)

df = eb_scraper(urls,proxy_list)

df.drop_duplicates(subset='Title',inplace=True)
df.to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_8_Plus/iphone8plus_256g_{}.txt'.format(date))
