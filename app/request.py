from app import app
import urllib.request,json
from .models import news

News = news.NewsSource

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(source):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_movies_response['results']
            news_results = process_results(news_results_list)


    return movie_results