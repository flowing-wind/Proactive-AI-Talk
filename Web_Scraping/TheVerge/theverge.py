# -*- codeing=utf-8 -*-
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
import sqlite3
from datetime import datetime


def TheVerge_init ():
    # Scrape Main Page
    page = requests.get ("https://theverge.com")
    '''
    with open ("theverge_main.html", "w", encoding="utf-8") as f:
        f.write (page.text)
    with open ("theverge_main.html", 'r', encoding="utf-8") as f:
        page = f.read ()
    '''
    soup = BeautifulSoup (page.text, "html.parser")
    
    # match all the links
    links = soup.find_all ("a", href=re.compile (r"^/\d"))
    # remove repeated links
    link_list = set ()
    for link in links:
        link_list.add ("https://theverge.com" + link.get('href'))
    link_list = list (link_list)

    # use sql to save links in db
    conn = sqlite3.connect ("Web_Scraping/links.db")
    cursor = conn.cursor ()
    current_date = datetime.now().strftime('%Y-%m-%d')
    for link in link_list:
        cursor.execute ("INSERT OR IGNORE INTO Links (href, source, date) VALUES (?, 'TheVerge', ?)", (link,current_date))
    conn.commit ()
    conn.close ()
    return

def GetContent (link):
    # Scrape content
    page = requests.get (link)
    '''
    with open ("output.html", "w", encoding="utf-8") as f:
        f.write (page.text)
    with open ("output.html", 'r', encoding="utf-8") as f:
        page = f.read ()
    '''
    soup = BeautifulSoup (page.text, "html.parser")

    # get article info
    title = soup.title.string
    # description = soup.find ('meta', attrs={'name': 'description'})['content']
    '''
    # get and transform time format
    ISO_8601 = soup.find('meta', attrs={'property': 'article:published_time'})['content']
    DATETIME = datetime.strptime (ISO_8601, '%Y-%m-%dT%H:%M:%S.%fZ')
    publish_time = DATETIME.strftime ('%Y-%m-%d %H:%M:%S')
    '''
    # get article
    script_tag = soup.find ('script', type='application/ld+json')
    json_data = script_tag.string
    match_articleBody = re.search(r'"articleBody":\s*"([^"]+)"', json_data)
    article_body = match_articleBody.group(1)
    article_body = re.sub(r'\[.*?\]', '', article_body)
    article_body = article_body.replace(r'\n', '') 
    if len(article_body.split()) <=200:
        return "Invalid Content"
    else:
        article = "Title: " + title + "\nContent: " + article_body
        return article