
import requests
import time
import json
from news_file import get_news_from_keyword, get_news_from_topic
import sys

# Saved in local file
import keys



# Get Telegram key, Saved in another file
telegram_key = keys.get_telegram_key()
base_url='https://api.telegram.org/' + str(telegram_key)


while True:

    try:
        offset
    except:
        url = base_url+'/getUpdates'
        res=requests.get(url)

        # If no Update id found, we will have to use last update ID saved    
        res=res.text
        res=json.loads(res)['result']

        if res==[]:
            continue 

        res=res[0]['update_id']
        offset=int(res)+1

       
    
    
    url = base_url + '/getUpdates' + '?timeout=500&offset=' + str(offset)
    res=requests.get(url)
    if len(json.loads(res.text)['result'])==0:
        continue
    
    result=json.loads(res.text)['result'][0]
    text=result['message']['text']
    
    # ending operation
    if text.lower()=='end':
        break
    
    if text.lower().startswith('keyword'):
        keyword=text.split(' ')[1:]
        keyword = "%20".join(keyword)
        to_send=get_news_from_keyword(keyword)
        
    
    elif text.lower().startswith('topic'):
        topic=text.split(' ')[1:]
        topic='%20'.join(topic)
        to_send=get_news_from_topic(topic)
        

    else:
        to_send='\nThe NewsBot Powered by Newsapi.org\n\n'\
            'Get the News For a Topic :\n'\
            'Type "Topic Topic_Name" \n'\
            'Example : "Topic Weather" \n\n\n'\
            'To Get News for a specific word\n'\
            'Type "keyword key" \n'\
            'Example : "Keyword Rain" \n\n\n'\
            'If you are not getting news,\n'\
            'Try sending again with Proper Code\n\n\n'\
            'Please Wait atleast for 5 seconds to get a Reply\n'

    sender = str(result['message']['from']['id'])
    
    
    
    if type(to_send)==str:
        reply_url = base_url +'/sendMessage?chat_id='+str(sender)+'&text='+str(to_send)
        requests.get(reply_url)
        
   
    
    if type(to_send)==list:
        if len(to_send)==0:
            header='Did not found any news for :'+str(text)+'\nPlease Rephrase it.'
            reply_url = base_url +'/sendMessage?chat_id='+str(sender)+'&text='+str(header)
            requests.get(reply_url)
            requests.get(reply_url)
        
        else:
            header='Top '+str(len(to_send))+' results for you'
            reply_url = base_url +'/sendMessage?chat_id='+str(sender)+'&text='+str(header)
            requests.get(reply_url)

            for reply in to_send:
                reply_url = base_url +'/sendMessage?chat_id='+str(sender)+'&text='+str(reply)
                requests.get(reply_url)

    offset+=1






    