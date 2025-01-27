import importlib
import json
import sqlite3
import random
from datetime import datetime
import sys
sys.path.append ('./Web_Scraping')

def DelAndRegenerate (conn, cursor, id):         # delete invalid content and regenerate id
    cursor.execute ("DELETE FROM Links WHERE id = ?", (id,))
    conn.commit()
    cursor.execute ("SELECT MAX(id) FROM Links")
    max_id = cursor.fetchone ()[0]
    random_id = random.randint(1, max_id)
    return random_id

def MsgGen ():
    # connect to db
    conn = sqlite3.connect ("Web_Scraping/links.db")
    cursor = conn.cursor ()
    # get max_id and generate random_id
    cursor.execute ("SELECT MAX(id) FROM Links")
    max_id = cursor.fetchone ()[0]
    random_id = random.randint (1, max_id)
    # get content of random_id
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_date = datetime.strptime (current_date, '%Y-%m-%d')
    while (True):   
        cursor.execute ("SELECT * FROM Links WHERE id = ?", (random_id,))
        res = cursor.fetchone ()
        '''
        date = res [3]
        record_date = datetime.strptime (date, '%Y-%m-%d')
        if ((current_date - record_date).days > 7):     # check if find outdated news
            random_id = DelAndRegenerate(conn, cursor, random_id)
            continue
        '''
        # Dynamic import GetContent function
        with open ("Web_Scraping/sources.json", "r", encoding="utf-8") as f:
            sources = json.load (f)
        source = res [2]
        link = res [1]
        module = importlib.import_module (sources[source])
        GetContent = getattr(module, 'GetContent', None)
        content = GetContent (link)
        if content == "Invalid Content":         # check if it's too short
            random_id = DelAndRegenerate(conn, cursor, random_id)
            continue
        else:
            break
    
    prompt = "\nSuppose you are the one who won't say many words and you've read the passage and want to talk with me. According to the article, focus on only one aspect and start the conversation, can be the form of exclamation or asking opinions. As the user hasn't read it, brief summary and introduction is necessary, proper greetings are needed too, but don't tell them 'This article...', because they don't know the article, no details, 4 sentences are enough, within 200 words, keep your tone light and nature."
    message = content + prompt
    '''
    with open ("message.txt", 'w', encoding="utf-8") as f:
        f.write (message)
    '''
    return message