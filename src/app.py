# -*- coding: utf-8 -*-
#
# (c) 2013-2019 Wishtack
#

from flask import Flask

from src.api.todo_list import todo_blueprint

app = Flask(__name__)
app.register_blueprint(todo_blueprint)
