
import requests
import json

# Saved in local file
import keys


# Get NewsApi Key, Saved in different file
news_api_key = str(keys.get_news_api_key())
headers={'X-Api-Key':news_api_key}


def get_news_from_keyword(keyword):
    news_url = 'https://newsapi.org/v2/everything?language=en&q='+keyword

    response = requests.get(news_url,headers=headers).text
    response = json.loads(response)['articles']
    return_list=[]
    for r in response:
        source=r['source']['name']
        author=r['author']
        title=r['title']
        url=r['url']
        return_list.append('\n\nAgency: '+str(source)+'\nAuthor :'+str(author)+'\nTitle: '+title+'\n\nread here: '+str(url))
    if len(return_list)>5:
        return return_list[:5]

    return return_list

def get_news_from_topic(topic):
    
    news_url = 'https://newsapi.org/v2/everything?language=en&qInTitle='+topic
    response = requests.get(news_url,headers=headers).text
    response = json.loads(response)['articles']

    return_list=[]
    for r in response:
        source=r['source']['name']
        author=r['author']
        title=r['title']
        url=r['url']
        return_list.append('\n\nAgency: '+str(source)+'\nAuthor :'+str(author)+'\nTitle: '+title+'\n\nread here: '+str(url))
    
    if len(return_list)>5:
        return return_list[:5]
    
    return return_list
    
