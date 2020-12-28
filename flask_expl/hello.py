from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text_align: center">Hellooooo!</h1> ' \
           '<p>This is a paragraph.<p>' \
           '<img src="https://media.giphy.com/media/6RuhlzSdhIAqk/giphy.gif">'


def make_bold(function):
    def wrapper():
        result = function()
        return f"<b>{result}</b>"

    return wrapper


def make_emphasize(function):
    def wrapper():
        result = function()
        return f"<em>{result}</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        result = function()
        return f"<u>{result}</u>"

    return wrapper


@app.route('/bye')
@make_bold
@make_emphasize
@make_underlined
def hello():
    return 'Bye'


if __name__ == "__main__":
    app.run(debug=True)
