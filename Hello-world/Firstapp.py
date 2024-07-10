from flask import Flask

app = Flask(__name__)

@app.route('/') # to configure the default path for the application

def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)