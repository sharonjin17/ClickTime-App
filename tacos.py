from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/test')
def test(query):
    return '<h1>You are on the test page.</h1>'

if __name__ == '__main__':
    app.run()
