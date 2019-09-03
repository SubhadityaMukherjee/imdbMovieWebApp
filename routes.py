from flask import Flask
import main
from flask import Flask, redirect, url_for, request, render_template

import os

# print(os.getcwd())
name_movie = ''


app = Flask(__name__)
@app.route('/')
def getmovie():
    # movie_name=''
    return render_template('frontscreen.html')


@app.route('/', methods=['POST'])
def my_form_post():
    global name_movie
    text = request.form['inpt_search']
    processed_text = text.upper()
    name_movie = processed_text
    return redirect('/movie')

@app.route('/movie')
def gen_summary():
    # movie_name = 'avengers endgame'
    global name_movie
    print(name_movie)
    js = main.return_summary(name_movie)
    print(js.keys())
    act = js["actor"]
    try:
        act = ', '.join([x['name'] for x in act])
    except:
        pass

    direc = js['director']
    try:
        direc = ', '.join([x['name'] for x in direc])
    except:
        pass

    return render_template("table.html", image_link = js['image'],name=js["name"],genre=', '.join(js["genre"]),actor = act, datep = js["datePublished"])


if __name__ == '__main__':
   app.run(debug = True)

