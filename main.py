from fastapi import FastAPI, Query

app = FastAPI()
library = {
    "Ліна Костенко": [
        {"title": "Маруся Чурай", "pages": 352},
        {"title": "Берестечко", "pages": 288},
        {"title": "Записки українського самашедшого", "pages": 304}
    ],
    "Джордж Оруелл": [
        {"title": "1984", "pages": 328},
        {"title": "Animal Farm", "pages": 112}
    ],
    "Тарас Шевченко": [
        {"title": "Кобзар", "pages": 480},
        {"title": "Гайдамаки", "pages": 152}
    ],
    "Джоан Роулінг": [
        {"title": "Harry Potter and the Philosopher's Stone", "pages": 223},
        {"title": "Harry Potter and the Chamber of Secrets", "pages": 251},
        {"title": "Harry Potter and the Prisoner of Azkaban", "pages": 317}
    ]
}

@app.post("/add_book")
async def add_book(author: str = Query(..., min_length=2, max_length=1999, title="Author name"),
                title: str = Query(..., min_length=2, max_length=1999, title="Book title"),
                pages: int = Query(..., gt=0, title="Number of pages")):
    if author not in library:
        library[author] = []
    library[author].append({"title": title, "pages": pages})
    return {"message": "Book added successfully"}
@app.get('/all')
def get_all_books():
    return library
@app.get('/author/{author_name}')
async def get_books_by_author(author_name: str):
    if author_name in library:
        return {author_name: library[author_name]}
    else:
        return {"message": "Author not found"}