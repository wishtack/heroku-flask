#!/usr/bin/env bash

set -o errexit

TOOLS_PATH="$(dirname $0)"

export DEBUG=True
export FLASK_APP="${TOOLS_PATH}/../src/app.py"
export FLASK_ENV=development

pipenv run flask run
