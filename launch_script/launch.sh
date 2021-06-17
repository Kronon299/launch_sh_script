#!/bin/bash

echo "*****cleaning directory*****"
rm -r $(ls | grep -v launch.sh)

REPO=$1

echo "*****cloning repo*****"
git clone $REPO
cd $(ls | grep -v launch.sh)
pwd
#repodir=$(ls | grep -v launch.sh) ; cd $repodir

echo "*****install pip*****"
sudo apt install python3-pip

echo "*****create venv*****"
python3 -m pip install virtualenv
python3 -m virtualenv venv

echo "*****activete venv*****"
. venv/bin/activate

echo "*****install requirements*****"
venv/bin/pip install -r requirements.txt

echo "*****runing flask app*****"
export FLASK_APP=app.py
flask run
#python3 main.py

