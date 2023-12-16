from django.shortcuts import render, HttpResponse
import random


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
    
    </body>
    </html>
    """


# Create your views here.
def index(request):
    global topics

    article = "<h2>welcome</h2> HelloDjango"
    return HttpResponse(HTMLTemplate(article))


def create(request):
    return HttpResponse("Create")


def read(request, id):
    global topics

    for topic in topics:
        if topic["id"] == int(id):
            article = f'<h2>{topic["title"]}</h2> {topic["body"]}'
    return HttpResponse(HTMLTemplate(article))
