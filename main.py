import os
from bs4 import BeautifulSoup
import urllib.request
import re
import json


def getLinks(name):
    link = b'https://www.imdb.com/find?ref_=nv_sr_fn&q={}&s=all'.decode(
        'ASCII').format('+'.join(name.split()))
    print('[INFO] link: {}'.format(link))
    site = urllib.request.urlopen(link)
    soup = BeautifulSoup(site, 'html.parser')
    list_of_links = []
    for link in soup.find_all('a'):
        hre = str(link.get('href')).split('\n')
        # print(hre)
        for lnk in hre:

            try:
                if '/title/' in lnk and 'ref' not in lnk:  #and 'fn_al_' in lnk:

                    list_of_links.append('https://www.imdb.com' + lnk)
            except Exception as e:
                print(e)
    print('[INFO] Done with {}'.format('link'))
    print(list_of_links[0])
    return list_of_links[0]


def getinfo(list_of_links):
    site = urllib.request.urlopen(list_of_links)
    soup = BeautifulSoup(site, 'html.parser')
    # print(l)
    print('[INFO] Done with {}'.format('info'))
    results = json.loads(soup.find('script', type='application/ld+json').text)

    # x = [a for a in results]
    req_fields = [
        'name', 'image', 'genre', 'actor', 'director', 'datePublished',
        'trailer'
    ]
    dic = {}
    # fields = [results[x] for x in req_fields]
    fields = []
    for x in req_fields:
        try:
            fields.append(results[x])
        except:
            pass

    for a in range(len(req_fields)):
        try:
            dic[req_fields[a]] = fields[a]
        except:
            pass

    return dic


def return_summary(movie):
    l = getinfo(getLinks(movie))
    # print(l)

    return l


# print(return_summary('hitchikers guide to the galaxy'))
