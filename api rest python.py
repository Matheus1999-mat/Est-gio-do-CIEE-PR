

from flask import Flask, jsonify, request
import json

games_title = input("Escreva o título do jogo:")

if len(games_title)<8:
    print("Título de tamanho insuficiente.")
games_description = input("Escreva a descrição do jogo:")
games_release = input("Escreva a data de lançamento do jogo:")
games_genre = input("Escreva o gênero do jogo:")
games_developer = input("Escreva o nome da desenvolvedora do jogo:")
if len(games_developer)<8:
    print("Nome de tamanho insuficiente.")


app = Flask(__name__)
games = [
    {
        "id": 1,
        "title": games_title,
        "description": games_description,
        "release_date": games_release,
        "genres": [games_genre],
        "developer": games_developer
    }
]

genres = [
    {
        "id": 1,
        "name": games_genre
    }
]

@app.route('/games', methods=['GET', 'POST'])
def handle_games():
    if request.method == 'GET':
        return jsonify(games)
    elif request.method == 'POST':
        new_game = request.json
        new_game["id"] = len(games) + 1
        games.append(new_game)
        return jsonify(new_game), 201

@app.route('/games/<int:game_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_game(game_id):
    game = next((g for g in games if g["id"] == game_id), None)
    if game is None:
        return jsonify({"error": "Game not found"}), 404
    if request.method == 'GET':
        return jsonify(game)


@app.route('/games/<int:game_id>',methods=['PUT'])
def game_put(game_id):
    game = next((g for g in games if g["id"] == game_id), None)

    if request.method=='PUT':
        data = request.json
        game.update(data)
        return jsonify(game), 200
@app.route('/games/<int:game_id>',methods=['DELETE'])
def game_delete(game_id):
    game = next((g for g in games if g["id"] == game_id), None)
    if request.method=='DELETE':

        games.remove(game)
        return "", 204




@app.route('/genres', methods=['GET'])
def genres_get():
    if request.method == 'GET':
        return jsonify(genres)


@app.route('/genres',methods=['POST'])
def genres_post():
    if request.method =='POST':
        new_genre = request.json
        new_genre["id"] = len(genres) + 1
        genres.append(new_genre)
        return jsonify(new_genre), 201

app.run(debug=True)






