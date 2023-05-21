# News Sentiment Analyzer

This project aims to gather news data using the [NewsAPI](https://newsapi.org/), perform sentiment analysis on news articles, and display the results in an interactive dashboard built with Plotly Dash.

## Project Description

The News Sentiment Analyzer is a data pipeline project designed to fetch daily news data from various sources using the NewsAPI, store the data in an SQLite database, analyze the sentiment of the news articles, and present the analyzed data on an interactive dashboard.

The dashboard will allow users to filter news by topic and sentiment. This will give users a quick overview of the top reported news stories of the day and their sentiment (positive, negative, neutral).

## Planned Features

- **Data Collection**: A script will run daily to fetch news data from the NewsAPI and store it in an SQLite database.
- **Data Processing**: The raw news data will be cleaned and processed. This step will include performing sentiment analysis on the news articles.
- **Interactive Dashboard**: A web application will display the analyzed news data. The dashboard will include features for filtering the news by topic and sentiment.

## Tech Stack

- **Python**: The primary programming language for this project.
- **NewsAPI**: The API used to fetch news data.
- **SQLite**: The database used to store the news data.
- **TextBlob**: A Python library used to perform sentiment analysis.
- **Plotly Dash**: A Python framework used to create the interactive dashboard.

## Project Structure

The project repository is structured as follows:

/news-sentiment-analyzer
|-- /data
| |-- /raw
| |-- /processed
|-- /scripts
| |-- data_collection.py
| |-- data_processing.py
| |-- sentiment_analysis.py
|-- /dashboard
| |-- app.py
| |-- /assets
|-- .gitignore
|-- README.md
|-- requirements.txt

## Author

Grant Hicks
