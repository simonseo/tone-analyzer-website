# Tone Analyzer

## Get it up and running

1. Make sure you have Python3 installed on your computer.
1. Create a virtual environment using `pipenv`, `venv`, or `virtualenv` -- whichever one you prefer
2. In terminal, either run `pipenv install -r requirements.txt` or `pip install -r requirements.txt`
3. cd into root directory and run `flask run`
4. Direct your browser to the address that flask tells you
5. Input either a Twitter handle, hashtags, or other text data to perform sentiment analysis

## Features
1. Has an API wrapper around Azure's Cognitive API and Twitter API
2. Defensive coding practices - use asserts to confirm assumptions, account for unexpected user input in forms by validating in front-end.
3. Use of Jinja2 templates to reduce time spent on writing HTML generation.
4. Clear folder structure
5. Version control using Git and GitHub
