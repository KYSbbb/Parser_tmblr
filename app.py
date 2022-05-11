from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from form import LinkForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '1'


@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = LinkForm()
    if form.validate_on_submit():
        linkk = LinkForm().data
        linkkk = linkk.get("link_example")
        return get_total_likes(linkkk)
    return render_template('main_page.html', form=form)


def get_total_likes(link):
    likes = []
    reque = requests.get(link).text
    soup = BeautifulSoup(reque, 'lxml')
    actions = soup.find('ol', class_='notes')
    posts = actions.find_all('span', class_='action')
    for each in posts:
        like = each.text
        validation = str.isascii(like)
        if validation == True:
            likes.append(like)
    get_likes = soup.find('div', class_='meta-item post-notes').text
    prepared_data = (likes[0] + "& " + likes[1] + "in total there is " + get_likes)
    print(prepared_data)
    return render_template('link_req.html', prepared_data=prepared_data)


if __name__ == '__main__':
    app.run(debug=True)
