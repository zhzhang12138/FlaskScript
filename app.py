# -*- coding:utf-8 -*-
# @FileName  :app.py
# @Time      :2022/8/31 10:29
# @Author    :John Doe
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["get"])
def get_demo():
    return "get success source"


@app.route('/', methods=['POST'])
def post_demo():
    return "post success source"


if __name__ == '__main__':
    app.run('0.0.0.0', port='8080')
