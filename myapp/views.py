from django.shortcuts import render, HttpResponse
import random
from django.views.decorators.csrf import csrf_exempt


topics = [
    {"id": 1, "title": "roting", "body": "Routing is ..."},
    {"id": 2, "title": "view", "body": "View is ..."},
    {"id": 3, "title": "moel", "body": "Model is ..."},
]


def HTMLTemplate(article):
    ol = ""
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f"""
    <html>
    <body>
        <h1><a href= "/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {article}
        <ul>
            </li><a href="/create/">create</a></li>
        </ul>
    
    </body>
    </html>
    """


# Create your views here.
def index(request):
    global topics

    article = "<h2>welcome</h2> HelloDjango"
    return HttpResponse(HTMLTemplate(article))


@csrf_exempt
def create(request):
    article = """
        <form action="/create/" method="post">
            <p><input type="text" placeholder="title" name="title"></p>
            <p><textarea name="body" placeholder="body" ></textarea></p>
            <p><input type="submit"></p>
        </form>
    """
    return HttpResponse(HTMLTemplate(article))


def read(request, id):
    global topics

    for topic in topics:
        if topic["id"] == int(id):
            article = f'<h2>{topic["title"]}</h2> {topic["body"]}'
    return HttpResponse(HTMLTemplate(article))
