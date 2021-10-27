from flask import Flask, jsonify
import csv

all_movies = []

# Writing 'encoding='utf-8' is very necessary and important below
with open('movies.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch_movies = []

app = Flask(__name__)

@app.route('/get-movie')
def getMovie():
    return jsonify({
        "data": all_movies[0],
        "status": "Success"
    })

@app.route('/liked-movie', methods=["POST"])
def likedMovies():
    movie = all_movies[0]
    all_movie = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status": "Success"
    }), 201

@app.route('/unliked-movie', methods=["POST"])
def unlikedMovies():
    movie = all_movies[0]
    all_movie = all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status": "Success"
    }), 201

@app.route('/did-not-watch-movie', methods=["POST"])
def didNotWatchMovies():
    movie = all_movies[0]
    all_movie = all_movies[1:]
    did_not_watch_movies.append(movie)
    return jsonify({
        "status": "Success"
    }), 201

if __name__ == "__main__":
    app.run()
