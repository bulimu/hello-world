# -*- coding: utf-8 -*-
"""
@author: Fang
@file: application.py
@time: 17.09.2019 12:42
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"

