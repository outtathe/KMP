from search import *
import os
from flask import Flask, request, jsonify, render_template, url_for
# import requests


app = Flask(__name__)

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     return render_template('index.html', css_file=url_for('static', filename='style.css'))


@app.route('/search', methods=['POST'])
def Search():
    data = request.form
    text = data['text']
    substring = data['substring']
    Positions = kmp(text, substring)
    return jsonify({'positions': Positions})

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        data = request.form
        text = data['text']
        substring = data['substring']
        positions = kmp(text, substring)
        return render_template('results.html', positions=positions, css_file=url_for('static', filename='style.css'))
    else:
        return render_template('index.html', css_file=url_for('static', filename='style.css'))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port = int(os.getenv('PORT', 8080)))
