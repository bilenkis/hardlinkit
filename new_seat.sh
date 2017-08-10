#!/bin/bash
project=$(basename "$PWD")
mkdir ../venv
virtualenv -p python3 ../venv/"$project"
source ../venv/"$project"/bin/activate
pip install -r requirements.txt
