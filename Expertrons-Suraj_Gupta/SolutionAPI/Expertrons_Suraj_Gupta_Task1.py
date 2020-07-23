#solution 1
import re
from newsapi import NewsApiClient

def find_q(text): 
  matches = re.findall(r'\"(.+?)\"',text) 
  return matches[0]


option = input("""Press 1 For Query.\nPress 2 for Source\n""")
source = ''
query = ''
if int(option) == 1:    
    query =find_q(input("""Enter the query"""))
    
else:
    
    source = input("Enter the Source")
    
    
    

Api_token = "e18d352396c540129970ec12982bbf85"

# Inititalize 
newsapi = NewsApiClient(api_key=Api_token)

# fetch all articles
all_articles = newsapi.get_everything(q=query,
                                      sources='',
                                      domains='bbc.co.uk,techcrunch.com',
                                      #from_param='2020-06-21',
                                      #to='2020-06-21',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

for e in all_articles['articles'][:10]:
    if source != '' and  source.lower() in e['source']['name'].lower():
        print(f"source={e['source']['name']}\nAuthor={e['author']}\n\nTitle={e['title']}\n\nDescription={e['description']}\n\nURL={e['url']}\n\nPublished at {e['publishedAt']}\nContent={e['content']}\n\n")
    elif source == '':
        print(f"source={e['source']['name']}\nAuthor={e['author']}\n\nTitle={e['title']}\n\nDescription={e['description']}\n\nURL={e['url']}\n\nPublished at {e['publishedAt']}\nContent={e['content']}\n\n")
    
        
    
