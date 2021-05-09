import requests
from bs4 import BeautifulSoup
from flask import *

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/functionalities')
def functionalities():
    return render_template('functionalities.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/livedemo')
def livedemo():
    return render_template('livedemo.html')

@app.route('/webscrape')
def dummy():

    url ="https://www.educba.com/types-of-trees-in-data-structure/"
    html = requests.get(url)
    htmlParse = BeautifulSoup(html.content, 'html.parser')
    head = htmlParse.find_all('h4')
    para = htmlParse.find_all('p')

    paralis = para[10:21]
    del paralis[3]
    del paralis[4]
    del paralis[5]
    del paralis[6]

    headlis = head[:6]
    main_lis = []
    main_lis.append(paralis[0])
    del paralis[0]
    for i in range(6):
        main_lis.append(headlis[i])
        main_lis.append(paralis[i])
    
    return str(main_lis)


    
    
if __name__=='__main__':
    app.run(debug=True)