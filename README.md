# Film API

This is a simple Flask API that provides information about films. The data is loaded from a JSON file and can be filtered and sorted based on user queries.

## Features

- Get a list of films
- Get a specific film by ID
- Filter films by genre and release year
- Sort films by one or more fields

## Endpoints

- `GET /`: Returns a list of films. You can filter and sort the films by adding query parameters:
  - `filter_by_genre`: Filters the films by genre. The value should be the genre you want to filter by.
  - `filter_by_release_year`: Filters the films by release year. The value should be the year you want to filter by.
  - `sort_by`: Sorts the films by one or more fields. The value should be the field name you want to sort by. You can add a `-` before the field name to sort in descending order. You can sort by multiple fields by providing the field names separated by commas.
  - `number`: Limits the number of films returned. The value should be the number of films you want to get.

- `GET /films/<film_id>`: Returns a specific film by ID. The `film_id` should be the ID of the film you want to get.

## Setup

1. Clone the repository
2. Install the dependencies: `pip install flask`
3. Run the server: `python main.py`

[Link to hosted API](https://ziad03.pythonanywhere.com/)