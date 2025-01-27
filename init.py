# -*- codeing=utf-8 -*-
import sqlite3
import sys
sys.path.append ('./Web_Scraping')
from Web_Scraping.TheVerge.theverge import *


def init_all ():
    # create database to save links from various web
    conn = sqlite3.connect ("Web_Scraping/links.db")
    cursor = conn.cursor ()
    # create a table
    cursor.execute ('''
    CREATE TABLE IF NOT EXISTS Links (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    href TEXT UNIQUE,
                    source TEXT,
                    date TEXT
                    )
    ''')
    conn.commit ()
    conn.close ()

    # web_scraping func init
    TheVerge_init ()
