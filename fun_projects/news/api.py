
from newsapi import NewsApiClient

newsap = NewsApiClient(api_key='51c538c30dc04107ad2b40c082402386')

# /v2/top-headlines

# /v2/everything
all_articles = newsap.get_everything(q='White House repeats no Taiwan policy change',
                                      
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
print(all_articles)