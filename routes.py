from flask import Flask
import main
from flask import Flask, redirect, url_for, request, render_template

import os

# print(os.getcwd())



app = Flask(__name__)
@app.route('/')
def getmovie():
    # movie_name=''
    return render_template('frontscreen.html')


@app.route('/', methods=['POST'])
def my_form_post():
    print(request.args['inpt_search'])
    return request.args['inpt_search']

@app.route('/movie')
def gen_summary():
    movie_name = 'avengers endgame'
    js = main.return_summary(movie_name)
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
