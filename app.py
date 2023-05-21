from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return 'Hello, World!'

@app.route('/contact')
def contact():
    return 'Hello, contact!'

if __name__ == '__main__':
    app.run()
