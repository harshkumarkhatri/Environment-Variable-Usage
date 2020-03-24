from flask import Flask
import os

app = Flask(__name__)


app.config['secret_key']=os.environ.get('secret_key')

@app.route('/')
def hello_world():
    return app.config['secret_key']


if __name__ == '__main__':
    app.run()
