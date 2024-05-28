
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/news-articles')
def news_articles():
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY'
    response = requests.get(url)
    articles = response.json()['articles']
    return render_template('news-articles.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY'
    response = requests.get(url)
    articles = response.json()['articles']
    article = next((a for a in articles if a['id'] == article_id), None)
    return render_template('article.html', article=article)

if __name__ == '__main__':
    app.run(debug=True)
