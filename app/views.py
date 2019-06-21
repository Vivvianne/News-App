from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'News app'
    
    return render_template('index.html',message = message)

@app.route('/news/<int:news_id>')
def movie(news_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = news_id)