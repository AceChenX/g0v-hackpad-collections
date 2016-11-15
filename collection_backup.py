from lxml import html
import requests
import os.path

page = requests.get('https://g0v.hackpad.com/')
tree = html.fromstring(page.content)
collections = tree.xpath('//div[@class="group-item"]/@data-groupid')

baseurl = 'https://g0v.hackpad.com/ep/group/feed?groupId='

for groupid in collections:
    url = baseurl + groupid
    xml_content = requests.get(url).content
    if os.path.isfile(groupid+'.xml'):
        continue
    else:
        with open(groupid+'.xml','w') as f:
            f.write(xml_content.decode('utf-8'))
            print(groupid)
