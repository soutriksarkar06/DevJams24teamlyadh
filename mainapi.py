from flask import Flask, request, jsonify
import random

app = Flask(__name__)

movies_data = {
    1: {'imdb_id': 'tt1375666', 'title': 'Inception', 'genre': 'sci-fi'},
    2: {'imdb_id': 'tt0133093', 'title': 'The Matrix', 'genre': 'sci-fi'},
    3: {'imdb_id': 'tt0816692', 'title': 'Interstellar', 'genre': 'sci-fi'},
    4: {'imdb_id': 'tt0468569', 'title': 'The Dark Knight', 'genre': 'action'},
    5: {'imdb_id': 'tt0111161', 'title': 'The Shawshank Redemption', 'genre': 'drama'},
    6: {'imdb_id': 'tt0109830', 'title': 'Forrest Gump', 'genre': 'drama'},
    7: {'imdb_id': 'tt0137523', 'title': 'Fight Club', 'genre': 'drama'},
    8: {'imdb_id': 'tt0068646', 'title': 'The Godfather', 'genre': 'crime'},
    9: {'imdb_id': 'tt0110912', 'title': 'Pulp Fiction', 'genre': 'crime'},
    10: {'imdb_id': 'tt0167260', 'title': 'The Lord of the Rings: The Return of the King', 'genre': 'fantasy'},
    11: {'imdb_id': 'tt0088763', 'title': 'Back to the Future', 'genre': 'sci-fi'},
    12: {'imdb_id': 'tt0099685', 'title': 'Goodfellas', 'genre': 'crime'},
    13: {'imdb_id': 'tt0082971', 'title': 'Raiders of the Lost Ark', 'genre': 'adventure'},
    14: {'imdb_id': 'tt0120737', 'title': 'The Lord of the Rings: The Fellowship of the Ring', 'genre': 'fantasy'},
    15: {'imdb_id': 'tt0110357', 'title': 'The Lion King', 'genre': 'animation'},
    16: {'imdb_id': 'tt0245429', 'title': 'Spirited Away', 'genre': 'anime'},
    17: {'imdb_id': 'tt0107290', 'title': 'Jurassic Park', 'genre': 'sci-fi'},
    18: {'imdb_id': 'tt0993846', 'title': 'The Wolf of Wall Street', 'genre': 'comedy'},
    19: {'imdb_id': 'tt0361748', 'title': 'Inglourious Basterds', 'genre': 'war'},
    20: {'imdb_id': 'tt6751668', 'title': 'Parasite', 'genre': 'thriller'}
}

genres = [
    'action', 'adventure', 'animation', 'anime', 'comedy', 'crime', 
    'drama', 'fantasy', 'horror', 'mystery', 'romance', 'sci-fi', 
    'sport', 'thriller', 'war'
]

@app.route("/reccwatched", methods=['GET'])
def recc_watched():
    param = request.args.get("param")
    if not param:
        return jsonify({'error': 'No movie IDs provided'}), 400
    
    movie_ids = param.split(',')
    watched_movies = [int(movie_id) for movie_id in movie_ids if int(movie_id) in movies_data]

    if not watched_movies:
        return jsonify({'error': 'No valid movie IDs found'}), 404

@app.route('/reccgenre', methods=['GET'])
def recc_genre():
    genre = request.args.get('param')

    if genre not in genres:
        return jsonify({'error': 'Invalid genre'}), 400
    
    # Filter movies based on the genre
    genre_movies = [movie for movie in movies_data.values() if movie['genre'] == genre]
    
    if genre_movies:
        recommended_movie = random.choice(genre_movies)
        return jsonify({'recommended': recommended_movie})
    else:
        return jsonify({'error': f'No movies found in genre: {genre}'}), 404
    

if __name__ == "__main__":
    app.run(debug = True)
