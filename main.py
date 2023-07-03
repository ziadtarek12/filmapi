from flask import Flask, request, jsonify
import json
from functools import wraps

app = Flask(__name__)

# Load films data from JSON file
with open("films.json") as f:
    data = f.read()
    films = json.loads(data)


def sort_and_filter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        films_copy = films.copy()
        filter_by_genre = request.args.get("filter_by_genre")
        filter_by_release_year = request.args.get("filter_by_release_year")
        sort_fields = request.args.getlist("sort_by")

        if filter_by_genre:
            films_copy = [film for film in films_copy if filter_by_genre.lower() in film.get("genre", "").lower()]

        if filter_by_release_year:
            films_copy = [film for film in films_copy if film.get("release_year") == int(filter_by_release_year)]

        if sort_fields:
            for sort_field in sort_fields:
                reverse = False
                if sort_field.startswith("-"):
                    reverse = True
                    sort_field = sort_field[1:]

                films_copy.sort(key=lambda x: x.get(sort_field, ""), reverse=reverse)

        kwargs['films'] = films_copy
        return func(*args, **kwargs)
    return wrapper



@app.route("/")
@sort_and_filter
def get_films(films):
    number = int(request.args.get("number", len(films)))
    films = films[:number]
    return jsonify(films)

@app.route("/films/<film_id>")
def get_film(film_id):
    if not film_id.isdigit():
        return jsonify({'error': 'Enter a number'}), 404
    film = next((film for film in films if film.get("id") == int(film_id)), None)
    if film:
        return jsonify(film)
    else:
        return jsonify({'error': 'Film not found'}), 404


if __name__ == "__main__":
    app.run(debug=True)
