# List of all stocks -> update daily -> sector -> category
# Technical data -> update daily
# -------
#
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='edc44f9d25ee43ef80f2f05b99202da4')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news',
                                          language='en')

news = newsapi.get_top_headlines(category='business',
                                 country='in',
                                 language='en',
                                 )



# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2021-02-01',
                                      to='2021-02-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# f = open(f"news.json",'w')
# sources = newsapi.get_sources()
# f.write(str(all_articles)+'\n'+str(sources))# /v2/sources
print(news)