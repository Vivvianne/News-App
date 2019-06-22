from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import Sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to The best Movie Review Website Online'
    message = 'News app'
    
    return render_template('index.html',title = title)

@app.route('/news/<int:news_id>')
def movie(news_id):

    '''
    View movie page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        #description= news_item.get('description')
        image = news_item.get('image_path')
    

        if image:
            news_object = News(id,title,image)
            news_results.append(news_object)

    return news_results

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting  cnn news
    cnn_news = get_news('cnn')
    print(cnn_news)
    title = 'Home - Welcome to CNN news'
    return render_template('index.html', title = title,cnn = cnn_news)
