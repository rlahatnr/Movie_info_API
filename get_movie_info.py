import requests
from Movie_info.models import Movie_data_list


def get_info():
    databox = []
    for n in range(1, 11):
        res = requests.get(f'https://yts.mx/api/v2/list_movies.json?limit=10&page={n}').json()
        movie_data = res['data']['movies']
        for i in movie_data:
            data = {
                'movie_id': i['id'],
                'movie_title': i['title'],
                'movie_year' : i['year'],
                'movie_rate' : i['rating'],
                'movie_genres' : ", ".join(i['genres']),
                'movie_summary' : i['summary']
            }
            databox.append(data)

    return databox

if __name__ == '__main__':
    movie_data = get_info()
    for i in movie_data:
        Movie_data_list(id=i['movie_id'], title=i['movie_title'], year=i['movie_year'],
                   rating=i['movie_rate'], genres=i['movie_genres'], summary=i['movie_summary']).save()
