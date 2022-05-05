from flask import Flask, render_template, url_for, redirect
import requests
from bs4 import BeautifulSoup
import lxml
from form import LinkForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '1'



@app.route('/', methods=['GET', 'POST'])
def MainPage():
    return render_template('main_page.html', form=LinkForm)


def user_link():
    form = LinkForm()



def get_total_likes():
    dict = []
    reque = requests.get(link).text
    soup = BeautifulSoup(reque, 'lxml')
    actions = soup.find('ol', class_='notes')
    posts = actions.find_all('span', class_='action')
    for each in actions:
        like = each.text
        validation = str.isascii(like)
        if validation == True:
            dict.append(like)
    return render_template('link_req.html', title='Likes')



if __name__ == '__main__':
    app.run()
