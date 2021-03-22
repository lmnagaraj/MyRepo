import requests, urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html"
guide = "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/"
page = requests.get(url, verify=False)

soup = BeautifulSoup(page.text, 'html.parser')

for y in soup.find_all('ul'):
    for i in y.find_all('li'):
        for z in i.find_all('a'):
            guided_url = guide + z['href'].split('/')[-1]
            pages = requests.get(guided_url, verify=False)
            soups = BeautifulSoup(pages.text, 'html.parser')
            for x in soups.find_all('div'):
                for p in x.find_all('p'):
                    if 'AWS::' in p.text:
                        print(p.text)
