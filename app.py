from flask import Flask
from kinduct.utils import factory

app = Flask(__name__)
factory.root_app(app,prefix="kinduct")
# @app.route('/')
# def index():
#     return "hello world"

if __name__ == '__main__':
    app.run(debug=True)