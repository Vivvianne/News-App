# News App
Author: Vivvianne Kimani

## Description
News Highlights is a web appliction that displays a list of news sources from around the world. A user is able to click on a news source and get a brief of the particular news article. Clicking on the news article will redirect you to the news source's web page.
This app has been tailor made for someone with the particular news sources he/she like to catch up on.
so this person will be able to click on the news sources in the categories he /she wishes to update him/herslf with. The person will be able to:
*See their various news category preferences.
*See the various news articles.
*Be able to click on the news articles and read them from the news sources.

## BDD

| Behaviour | Input | Output |
|:----------|-------|--------|
| Display the chosen news sources | Load on page | List the prefered news sources displayed per cartegory |
| Display articles from a news source |Click a news source | Redirected to news source page to view the articles |
| Display the preview of an article | On page load | Article displays an image, title, description and publication date|
|Read an entire article | Click an article | Redirected to the news source's site to read the entire article |

## Prerequisites

You need the following to start working on the project on your local computer:
-Python version 3.6
-Flask
-Pip
-virtualenv
-A text  Editor

## Getting Started

*Clone this repository to your local computer.
*Ensure you have python3.6 installed in your computer.
*From the terminal navigate to the cloned project folder.
*Create a virtual environment and access the folder via your virtual amchine.
*Visit https://newsapi.org/ and register for an API key.
*Create start.sh file and in it write the following lines:

export NEWS_API_KEY='<Your-Api-Key>'
 python3.6 manage.py server

*Run chmod +x start.sh follwoed by ./start.sh while in the project folder to start the project.
*Once started, the project can be accessed on your localhost using the address: http://127.0.0.1:5000/

## Live server
You can get the link to the live server here 

## Technologies Used

*Python v3.6
*Boostrap
*Flask

## Licence

MIT Licence
You can get the licence from this link 





