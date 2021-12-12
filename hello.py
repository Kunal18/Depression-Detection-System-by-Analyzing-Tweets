from flask import Flask, url_for, request
from flask import render_template as rt
from twitter import proceed
from flask_cors import CORS, cross_origin
from flask import jsonify

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
tid = ''

# Test
# @app.route('/')
# @app.route('/cj')
# def hello_world():
#     return rt('home.html')

# @app.route('/about')
# def about():
#     return "<h1>Hello About</h1>"

@app.route('/')
def index_page():
    return rt('index.html')


@app.route('/main', methods=['POST', 'GET'])
def dashboard():
    if request.method:
        return rt('main.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        t_id = request.form['twitterid']
        t_snt = proceed(t_id)
        return rt('result.html', id=t_id, values=t_snt, iurl='/static/images/new_plot.png')


@app.route('/processid', methods=['POST'])
def processid():
        t_id = eval(request.data)["id"]
        print(t_id)
        t_snt = proceed(t_id) #actual method
        #t_snt = [{"t":"ab","r":"happy"},{"t":"cd","r":"happy"},{"t":"abd","r":"happy"},{"t":"bcd","r":"happy"}] #testing
        #t_snt = [{"a":"b","c":"d","e":"f"}] #testing
        return jsonify(t_snt)


if __name__ == "__main__":
    app.run(debug=True)
