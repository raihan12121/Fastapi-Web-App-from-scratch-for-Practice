
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


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


@app.get("/",include_in_schema=False, name="home")
@app.get("/posts",include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request, 
        "home.html",
        {"posts": posts, "title": "Home"}
        )


app.get("/posts/{post_id}", include_in_schema=False)
def post_page(Request: Request, post_id: int):
    for posts in posts:
        if post.get("id")== post.id:
            title = posts["title"][:50]
            return templates.TemplateResponse(
                request,
                "post.html",
                {"post": post, "title": title},
            )
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")




@app.get("/api/posts")
def get_posts():
    return posts



@app.get("/api/posts/{post_id}")
def get_posts( post_id: int):
    for post in posts:
        if post.get("id")==post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
