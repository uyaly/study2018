from python.Flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Flask!'

@app.route('/H')
def H():
    return 'Hello Flask!'

if __name__ == '__main__':
    app.run()