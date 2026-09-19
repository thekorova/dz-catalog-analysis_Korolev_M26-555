import math

movies = [
    {
        "title": "The Dune Chronicles", 
        "year": 2021, 
        "genres": {"sci-fi", "drama"},
        "rating": 8.6, 
        "duration_min": 155, 
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]
    },
    {
        "title": "Kitchen Stories", 
        "year": 2019, 
        "genres": {"comedy", "drama"},
        "rating": 7.1, 
        "duration_min": 98, 
        "actors": ["A. Novak", "M. Ferguson"]
    },
    {
        "title": "silent hours", 
        "year": 2016, 
        "genres": {"thriller", "drama"},
        "rating": 6.4, 
        "duration_min": 112, 
        "actors": ["J. Bloom", "K. Lee"]
    },
    {
        "title": "Comet Racers", 
        "year": 2023, 
        "genres": {"sci-fi", "action"},
        "rating": 5.9, 
        "duration_min": 101, 
        "actors": ["O. Isaac", "P. Diaz"]
    },
    {
        "title": "The Last Bakery", 
        "year": 2014, 
        "genres": {"comedy"},
        "rating": 7.8, 
        "duration_min": 89, 
        "actors": ["A. Novak", "T. Chalamet"]
    },
    {
        "title": "midnight in oslo", 
        "year": 2020, 
        "genres": {"thriller", "mystery"},
        "rating": 8.9, 
        "duration_min": 124, 
        "actors": ["K. Lee", "R. Ferguson"]
    },
    {
        "title": "Garden of Static", 
        "year": 2022, 
        "genres": {"drama"},
        "rating": 4.8, 
        "duration_min": 137, 
        "actors": ["P. Diaz", "J. Bloom"]
    },
    {
        "title": "The Quiet Algorithm", 
        "year": 2024, 
        "genres": {"sci-fi", "drama"},
        "rating": 9.2, 
        "duration_min": 118, 
        "actors": ["M. Ferguson", "O. Isaac"]
    },
    {
        "title": "Two Left Shoes", 
        "year": 2011, 
        "genres": {"comedy"},
        "rating": 6.0, 
        "duration_min": 95, 
        "actors": ["A. Novak", "K. Lee"]
     },
    {
        "title": "Red Harbor", 
        "year": 2018, 
        "genres": {"action", "thriller"},
        "rating": 7.3, 
        "duration_min": 129, 
        "actors": ["P. Diaz", "T. Chalamet"]
    },
]


def average_rating(movies):
    """Возвращает средний рейтинг фильма, округленный до 1 знака"""
    sum_rating = 0
    for i in movies:
        sum_rating += i['rating']
    return round(sum_rating / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Возвращает возраст самого старого, нового фильма и средний возраст фильмов"""
    oldest = current_year - min(movies, key=lambda i: i["year"])["year"]
    newest = current_year - max(movies, key=lambda i: i["year"])["year"]
    average = math.ceil(sum(current_year - i["year"] for i in movies) / len(movies))
    return oldest, newest, average


def duration_in_hours(minutes):
    """Переводит минуты в формат '2ч 35м'"""
    hour = minutes // 60
    minute = minutes % 60
    return f'{hour}ч {minute}м'


def rating_tier(rating):
    """Возвращает категорию по рейтингу фильма"""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    """Возвращает категорию фильма по году выпуска фильма"""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


for i in movies:
    if "comedy" in i["genres"]:
        continue
    print(i["title"])


index  = 0
while index < len(movies):
    movie = movies[index]
    if movie["rating"] > 9.0:
        print(movie)
        break
    index += 1
else:
    print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Возвращает количество фильмов с длительность большем threshold"""
    count = 0
    for i in movies:
        if i["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    """Возвращает строку форматом Title Case (каждое слово с заглавной буквы)"""
    words = title.lower().split()
    full_words = []
    for word in words:
        full_words.append(word[0].upper() + word[1:])
    return " ".join(full_words)


def make_slug(title):
    """Возвращает нормализованное название в «слаг» вида 'the-quiet-algorithm'"""
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Возвращает единую строку с описанием фильма"""
    return (
        f'"{movie["title"]}" ({movie["year"]}) — {movie["rating"]}/10, ' 
        f'{duration_in_hours(movie["duration_min"])}, '
        f'жанры: {", ".join(sorted(movie["genres"]))}')


def titles_sorted_by_rating(movies):
    """Возвращает список названий фильмов, отсортированных по убыванию рейтинга"""
    sorted_movies = sorted(movies, key=lambda i: i["rating"], reverse=True)
    return [i["title"] for i in sorted_movies]


def top_n_by_rating(movies, n=3):
    """Возвращает список из n кортежей (title, rating) — топ по рейтингу"""
    sorted_movies = sorted(movies, key=lambda i: i["rating"], reverse=True)
    return [(i["title"], i["rating"]) for i in sorted_movies[:n]]


def count_by_genre(movies):
    """Возвращает словарь {жанр: количество фильмов}"""
    genre_count = {}
    for i in movies:
        for x in i["genres"]:
            genre_count[x] = genre_count.get(x, 0) + 1
    return genre_count


def actor_filmography(movies):
    """Возвращает словарь {актер: [список названий фильмов]}"""
    filmography = {}
    for i in movies:
        for x in i["actors"]:
            filmography[x] = filmography.get(x, [])
            filmography[x].append(i["title"])
    return filmography


result = {i["title"]: i["rating"]
for i in movies if i["rating"] > average_rating(movies)}


def all_genres(movies):
    """Возвращает множество всех уникальных жанров"""
    set_genres = set()
    for i in movies:
        set_genres.update(i["genres"])
    return set_genres


def common_actors(movie1, movie2):
    """Возвращает множество актеров, снимавшихся в обоих фильмах"""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """Возвращает жанры, встречающиеся в movies_a, но не встречающиеся в movies_b"""
    set_a = all_genres(movies_a)
    set_b = all_genres(movies_b)
    return set_a - set_b




