from flask import Flask, render_template
import requests

app = Flask(__name__)

def url_construct(id):
    return 'http://pokeapi.co/api/v2/' + id

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<int:id_number>')
def id_query(id_number):
    name = requests.get(url_construct('pokemon/' + str(id_number)))
    name = name.json()
    try:
        return '<h1>' + 'The Pokémon with id ' + str(id_number) + ' is ' + str(name["forms"][0]["name"]) + '</h1>'
    except KeyError:
        return '<h1>Not a valid Pokémon id</h1>'

@app.route('/pokemon/<string:name>')
def name_query(name):
    id = requests.get(url_construct('pokemon/' + name))
    id = id.json()
    name = name.capitalize()
    try:
        return '<h1>' + name + ' has id ' + str(id["id"]) + '</h1>'
    except KeyError:
        return '<h1>Not a valid Pokémon name</h1>'


if __name__ == '__main__':
    app.run()

