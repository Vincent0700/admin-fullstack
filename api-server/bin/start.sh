#!/bin/sh

base_dir=$(cd `dirname $0`; pwd)
project_dir=$(dirname "$base_dir")

cd "$project_dir"

if [ ! -d "./venv" ]; then
  pip install virtualenv -i https://pypi.tuna.tsinghua.edu.cn/simple
  virtualenv venv
fi

source "./venv/bin/activate"
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

echo "Done!"

gunicorn -c ./gunicorn.conf wsgi:app