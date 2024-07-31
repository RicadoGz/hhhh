from flask import Flask
# the two things need for the web script
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
def craw_website(url):
    # make sure the response was the valid
    response=requests.get(url)
    if response.status_code==200:
        # get the content of the page
        html_content = response.content
        # to make sure the contect been get
        soup=BeautifulSoup(html_content,'html.parser')
        name=soup.find()


@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
