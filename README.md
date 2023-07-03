# Language-Translator
A language translator created using an API with Python

## Development
Clone this repository
```bash
$ git clone https://github.com/Timmilytim/Language-Translator
```
Switch to project directly
```bash
$ cd Language-Translator
```
Install project dependencies with `pipenv`. If you don't have `pipenv` [See](#how-to-install-pipenv)
```bash
$ pipenv install
```
After successfull install switch to virtual env with
```bash
$ pipenv shell
```
Create a `.env` file in the project root. Provide the environmental variable `X-RapidAPI-Key` in it like so.
```dotenv
X_RAPID_API_KEY="your-key"
```

Run this project with
```bash
$ python main.py
```

### How to install `pipenv`
Install pipenv globally with
```bash
$ pip install pipenv
```
