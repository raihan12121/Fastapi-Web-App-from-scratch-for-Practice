
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


posts: list[dict] = [
    {
        "id": 1,
        "author": "Muhammad Raihan Molla",
        "title": "FastAPI is Awesome",
        "content": "This Framework is really easy to use and super fast.",
        "date_posted": "September 4, 2026",
    },
    {
        "id": 2,
        "author": "Muhammad Raihan",
        "title": "FastAPI is Awesomes",
        "content": "This Framework is really easy to use and super fasts.",
        "date_posted": "September 4, 2026",
    },
]


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse , include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts