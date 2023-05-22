import requests
import json
import sqlite3

def store_data(id, name, author, title, description, url, urlToImage, publishedAt, content, source_id):
    conn = sqlite3.connect('data/news_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS news_data
        (id TEXT PRIMARY KEY, name TEXT, author TEXT, title TEXT, description TEXT, 
        url TEXT, urlToImage TEXT, publishedAt DATE, content TEXT, source_id TEXT)
        ''')
    # Check if the news article is already in the database
    c.execute("SELECT * FROM news_data WHERE id = ?", (id,))
    result = c.fetchone()
    if result:
        print("Article already exists in the database")
    else:
        c.execute("INSERT INTO news_data (id, name, author, title, description, url, urlToImage, publishedAt, content, source_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
        (id, name, author, title, description, url, urlToImage, publishedAt, content, source_id))
        print("Article added to the database")
    conn.commit()
    conn.close()


def get_news():
    url = 'http://newsapi.org/v2/top-headlines?country=us'
    with open('config.json') as json_file:
        data = json.load(json_file)
    api_key = data['API_KEY']
    headers = {'Authorization': api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        articles = response.json()['articles']
        for article in articles:
            store_data(article['source']['id'], article['source']['name'], article['author'], article['title'], article['description'], article['url'], article['urlToImage'], article['publishedAt'], article['content'], article['source']['id'])
    else:
        print(f'Error: {response.status_code}')

if __name__ == "__main__":
    get_news()