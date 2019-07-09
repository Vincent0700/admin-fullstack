#!/bin/sh

base_dir=$(cd `dirname $0`; pwd)
project_dir=$(dirname "$base_dir")

cd "$project_dir"

if [ ! -d "./venv" ]; then
  pip install virtualenv
  virtualenv venv
fi

source "./venv/bin/activate"
pip install -r requirements.txt

echo "Done!"

gunicorn -c ./gunicorn.conf wsgi:app