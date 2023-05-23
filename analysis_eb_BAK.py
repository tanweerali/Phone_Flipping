# %matplotlib inline
import matplotlib
matplotlib.use('Agg')
from cleaning import phone
from iqrc import iqrcleaner
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')
from cleaning import phone
import pandas as pd
import time
from datetime import date, timedelta
import matplotlib
import sys
import os
from random import shuffle
pd.set_option('display.max_colwidth',-1)

today = str(date.today() - timedelta(1))

iphone6_today = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6/iphone6_%s.txt'% (today))[['Title','Price']]
iphone6s_today = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6S/iphone6s_%s.txt'% (today))[['Title','Price']]
iphone6splus_today = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6S_Plus/iphone6splus_%s.txt'% (today))[['Title','Price']]
iphone6plus_today = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_6_Plus/iphone6plus_%s.txt'% (today))[['Title','Price']]

iphone7_today = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_7/iphone7_%s.txt'% (today))[['Title','Price']]
iphone7plus_today = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_7_Plus/iphone7plus_%s.txt'% (today))[['Title','Price']]

iphone8_today = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_8/iphone8_%s.txt'% (today))[['Title','Price']]
iphone8plus_today = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/Iphone_8_Plus/iphone8plus_%s.txt'% (today))[['Title','Price']]


y = [len(iphone6_today),len(iphone6plus_today),len(iphone6s_today),len(iphone6splus_today),len(iphone7_today),len(iphone7plus_today),len(iphone8_today),len(iphone8plus_today)]
N = len(y)
x = range(N)
width = 0.80/1.9

plt.figure(figsize=(9,4))
plt.title('Phone Posted (Ebay)')
plt.xlabel('Phones')
plt.ylabel('Amount')
plt.xticks([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0],['Iphone 6','Iphone 6 Plus','Iphone 6S','Iphone 6S Plus','Iphone 7','Iphone 7 Plus','Iphone 8','Iphone 8 Plus'])
plt.bar(x,y,width,edgecolor='black')
plt.savefig('/home/REDACTED/Python/phone_flipping/eb/plot/barplot.png',bbox_inches='tight')

###

iphone6_processed = phone(iphone6_today,'iphone6',clean='yes')
iphone6s_processed = phone(iphone6s_today,'iphone6s',clean='yes')
iphone6splus_processed = phone(iphone6splus_today,'iphone6splus',clean='yes')
iphone6plus_processed = phone(iphone6plus_today,'iphone6plus',clean='yes')
iphone7_processed = phone(iphone7_today,'iphone7',clean='yes')
iphone7plus_processed = phone(iphone7plus_today,'iphone7plus',clean='yes')
iphone8_processed = phone(iphone8_today,'iphone8',clean='yes')
iphone8plus_processed = phone(iphone8plus_today,'iphone8plus',clean='yes')

iphone6_clean = iqrcleaner(iphone6_processed.Price)
iphone6s_clean = iqrcleaner(iphone6s_processed.Price)
iphone6splus_clean = iqrcleaner(iphone6splus_processed.Price)
iphone6plus_clean = iqrcleaner(iphone6plus_processed.Price)
iphone7_clean = iqrcleaner(iphone7_processed.Price)
iphone7plus_clean = iqrcleaner(iphone7plus_processed.Price)
iphone8_clean = iqrcleaner(iphone8_processed.Price)
iphone8plus_clean = iqrcleaner(iphone8plus_processed.Price)


iphone6_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone6_ma.txt')
iphone6s_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone6s_ma.txt')
iphone6splus_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone6splus_ma.txt')
iphone6plus_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone6plus_ma.txt')

iphone7_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone7_ma.txt')
iphone7plus_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone7plus_ma.txt')

iphone8_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone8_ma.txt')
iphone8plus_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone8plus_ma.txt')

iphone6_ma.append({'Mean':iphone6_clean.mean()},ignore_index=True).to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone6_ma.txt',index=False)
iphone6s_ma.append({'Mean':iphone6s_clean.mean()},ignore_index=True).to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone6s_ma.txt',index=False)
iphone6splus_ma.append({'Mean':iphone6splus_clean.mean()},ignore_index=True).to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone6splus_ma.txt',index=False)
iphone6plus_ma.append({'Mean':iphone6plus_clean.mean()},ignore_index=True).to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone6plus_ma.txt',index=False)

iphone7_ma.append({'Mean':iphone7_clean.mean()},ignore_index=True).to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone7_ma.txt',index=False)
iphone7plus_ma.append({'Mean':iphone7plus_clean.mean()},ignore_index=True).to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone7plus_ma.txt',index=False)

iphone8_ma.append({'Mean':iphone8_clean.mean()},ignore_index=True).to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone8_ma.txt',index=False)
iphone8plus_ma.append({'Mean':iphone8plus_clean.mean()},ignore_index=True).to_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone8plus_ma.txt',index=False)

iphone6_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone6_ma.txt')
iphone6s_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone6s_ma.txt')
iphone6splus_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone6splus_ma.txt')
iphone6plus_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone6plus_ma.txt')

iphone7_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone7_ma.txt')
iphone7plus_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone7plus_ma.txt')

iphone8_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone8_ma.txt')
iphone8plus_ma = pd.read_csv('/home/REDACTED/Python/phone_flipping/eb/data/scraped/moving_avg/iphone8plus_ma.txt')

###

plt.figure(figsize=(6,3))
plt.title('Iphone 6')
plt.xlabel('Closing')
plt.ylabel('Average Price')
plt.plot(iphone6_ma)
# plt.plot(iphone6_ma.Price.rolling(window=20).mean(),'b')
# plt.plot(iphone6_ma.Price.rolling(window=40).mean(),'g')
# plt.plot(iphone6_ma.Price.rolling(window=100).mean(),'r')
# plt.legend(['Short-term','Medium-term','Long-term'])
plt.savefig('/home/REDACTED/Python/phone_flipping/eb/plot/ma_plot_iphone6.png',bbox_inches='tight')

plt.figure(figsize=(6,3))
plt.title('Iphone 6 Plus')
plt.xlabel('Closing')
plt.ylabel('Average Price')
plt.plot(iphone6plus_ma)
# plt.plot(iphone6plus.Price.rolling(window=20).mean(),'b')
# plt.plot(iphone6plus.Price.rolling(window=40).mean(),'g')
# plt.plot(iphone6plus.Price.rolling(window=100).mean(),'r')
# plt.legend(['Short-term','Medium-term','Long-term'])
plt.savefig('/home/REDACTED/Python/phone_flipping/eb/plot/ma_plot_iphone6plus.png',bbox_inches='tight')

plt.figure(figsize=(6,3))
plt.title('Iphone 6S')
plt.xlabel('Closing')
plt.ylabel('Average Price')
plt.plot(iphone6s_ma)
# plt.plot(iphone6s.Price.rolling(window=20).mean(),'b')
# plt.plot(iphone6s.Price.rolling(window=40).mean(),'g')
# plt.plot(iphone6s.Price.rolling(window=100).mean(),'r')
# plt.legend(['Short-term','Medium-term','Long-term'])
plt.savefig('/home/REDACTED/Python/phone_flipping/eb/plot/ma_plot_iphone6s.png',bbox_inches='tight')

plt.figure(figsize=(6,3))
plt.title('Iphone 6S Plus')
plt.xlabel('Closing')
plt.ylabel('Average Price')
plt.plot(iphone6splus_ma)
# plt.plot(iphone6splus.Price.rolling(window=20).mean(),'b')
# plt.plot(iphone6splus.Price.rolling(window=40).mean(),'g')
# plt.plot(iphone6splus.Price.rolling(window=100).mean(),'r')
# plt.legend(['Short-term','Medium-term','Long-term'])
plt.savefig('/home/REDACTED/Python/phone_flipping/eb/plot/ma_plot_iphone6splus.png',bbox_inches='tight')


plt.figure(figsize=(6,3))
plt.title('Iphone 7')
plt.xlabel('Closing')
plt.ylabel('Average Price')
plt.plot(iphone7_ma)
# plt.plot(iphone7.Price.rolling(window=20).mean(),'b')
# plt.plot(iphone7.Price.rolling(window=40).mean(),'g')
# plt.plot(iphone7.Price.rolling(window=100).mean(),'r')
# plt.legend(['Short-term','Medium-term','Long-term'])
plt.savefig('/home/REDACTED/Python/phone_flipping/eb/plot/ma_plot_iphone7.png',bbox_inches='tight')

plt.figure(figsize=(6,3))
plt.title('Iphone 7 Plus')
plt.xlabel('Closing')
plt.ylabel('Average Price')
plt.plot(iphone7plus_ma)
# plt.plot(iphone7plus.Price.rolling(window=20).mean(),'b')
# plt.plot(iphone7plus.Price.rolling(window=40).mean(),'g')
# plt.plot(iphone7plus.Price.rolling(window=100).mean(),'r')
# plt.legend(['Short-term','Medium-term','Long-term'])
plt.savefig('/home/REDACTED/Python/phone_flipping/eb/plot/ma_plot_iphone7plus.png',bbox_inches='tight')


plt.figure(figsize=(6,3))
plt.title('Iphone 8')
plt.xlabel('Closing')
plt.ylabel('Average Price')
plt.plot(iphone8_ma)
# plt.plot(iphone8.Price.rolling(window=20).mean(),'b')
# plt.plot(iphone8.Price.rolling(window=40).mean(),'g')
# plt.plot(iphone8.Price.rolling(window=100).mean(),'r')
# plt.legend(['Short-term','Medium-term','Long-term'])
plt.savefig('/home/REDACTED/Python/phone_flipping/eb/plot/ma_plot_iphone8.png',bbox_inches='tight')

plt.figure(figsize=(6,3))
plt.title('Iphone 8 Plus')
plt.xlabel('Closing')
plt.ylabel('Average Price')
plt.plot(iphone8plus_ma)
# plt.plot(iphone8plus.Price.rolling(window=20).mean(),'b')
# plt.plot(iphone8plus.Price.rolling(window=40).mean(),'g')
# plt.plot(iphone8plus.Price.rolling(window=100).mean(),'r')
# plt.legend(['Short-term','Medium-term','Long-term'])
plt.savefig('/home/REDACTED/Python/phone_flipping/eb/plot/ma_plot_iphone8plus.png',bbox_inches='tight')
