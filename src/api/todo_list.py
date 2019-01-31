# -*- coding: utf-8 -*-
#
# (c) 2013-2019 Wishtack
#
from flask import Blueprint
from flask_restful import Resource, Api

todo_blueprint = Blueprint('todos', __name__)


class TodoListResource(Resource):

    def get(self):
        return [
        ]


api = Api(todo_blueprint)
api.add_resource(TodoListResource, '/todos')
