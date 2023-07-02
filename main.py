from flask import Flask, request, jsonify
import json
with open("films.json") as f:
    data = f.read()
    films = json.loads(data)
app = Flask(__name__)



@app.route("/")
def index():
    number = request.args.get("number")
    if number:
        number = int(number)
    else:
        number = len(films)
    filmss = films[0:number]
    return jsonify(filmss), 200




if __name__ == "__main__":
    app.run(debug=True)