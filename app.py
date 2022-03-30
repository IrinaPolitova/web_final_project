from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from model import sent
from random import choice
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
db = SQLAlchemy(app)


class Answers(db.Model):
    __tablename__ = "answers"

    game_id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Text)


db.create_all()


@app.route('/')  # главная страница
def index():
    return render_template("index.html")


@app.route('/game')  # игра
def form():

    variants = ['real', 'create']
    variant = choice(variants)
    string = sent(variant)

    all_info = {}
    all_info['true'] = Answers.query.filter_by(value='true').count()
    all_info['false'] = Answers.query.filter_by(value='false').count()

    # Creating dataset
    labels = ['Правильные ответы', 'Неправильные ответы']
    data = [all_info['true'], all_info['false']]

    # Creating plot
    plt.figure(figsize=(10, 7))
    plt.pie(data, labels=labels)

    plt.savefig('static/figure.png')

    return render_template('game.html', string=string, variant=variant)


@app.route('/process', methods=['get'])  # процесс обработки результата
def answer_process():
    if not request.args:
        return redirect(url_for('startgame'))

    value = str(request.args.get('value'))

    if value == 'true':
        st = 'Ваш ответ верный!'
        im = 'https://www.pngkey.com/png/detail/85-852828_cat-friendly-properties-happy-cat.png'
    else:
        st = 'Ваш ответ неверный!'
        im = 'https://avatars.mds.yandex.net/i?id=37d4501a45275982513e5b51e925adaf-5288156-images-thumbs&n=13'

    new_answer = Answers(value=value)
    db.session.add(new_answer)
    db.session.commit()
    db.session.refresh(new_answer)

    return render_template('yourgameanswer.html', st=st, im=im)


@app.route('/listening')  # аудирование
def listening():
    f = pd.read_csv('french_poems.csv', encoding='utf-8')
    f = f.sample(1)

    title = f.iloc[0]['title']
    author = f.iloc[0]['author']
    audio = f.iloc[0]['audio']
    poem = f.iloc[0]['poem'].split('\n')

    all_text = ''
    for p in poem[:-4]:
        all_text += p + ' '

    words = list(map(str, all_text.split()))
    for e in words:
        if len(e) < 6:
            words.remove(e)
    list_word = choice(words)
    new_poem = []

    for i in poem:
        for j in i.split(' '):
            if j == list_word:
                i = i.replace(j, '______')
        new_poem.append(i)

    return render_template('listening.html', title=title, author=author, poem=new_poem, audio=audio, j=list_word)


if __name__ == '__main__':
    app.run()
