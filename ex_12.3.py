import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

x = list()
url = input('Enter - ')
count = input('Enter count - ')
position = input('Enter position - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

for i in range(int(count)):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup('a')
    url = tags[int(position)-1].get('href',None)
    print('Retrieving: ', url)
