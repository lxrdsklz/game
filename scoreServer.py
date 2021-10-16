from flask import Flask
from dbtest import dbcounter

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/score')
def score():
    return dbcounter.sqlite()


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)