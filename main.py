from flask_api import FlaskAPI
from mongoengine import connect
import mongoengine as mongo
import json

connect('myapi')

# from flask import Blueprint
# theme = Blueprint(
#     'flask-api', __name__,
#     url_prefix='/flask-api',
#     template_folder='templates', static_folder='static'
# )
# app.blueprints['flask-api'] = theme


app = FlaskAPI(__name__)



class Project(mongo.EmbeddedDocument): # Embedded document class
    name = mongo.StringField()
    description = mongo.StringField()
    url = mongo.StringField()
    repo = mongo.StringField()
    technologies = mongo.ListField()
    group_project = mongo.BooleanField()




class Engineer(mongo.Document):
    last_name = mongo.StringField(required=True)
    first_name = mongo.StringField(required=True)
    email = mongo.StringField(required=True)
    github = mongo.StringField(required=True)
    linkedin = mongo.StringField(required=True)
    location = mongo.StringField(required=True)
    interests = mongo.ListField()
    skills = mongo.ListField()
    projects = mongo.EmbeddedDocumentListField(Project)

    def as_dict(self):
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
        }

engineer = {
    'last_name': 'Ross',
    'first_name': 'Takia',
    'email': 't.l.ross@outlook.com',
    'github': 'https://github.com/TR-1000',
    'linkedin': 'http://linkedin.com/in/takia-ross',
    'location': 'San Antonio, TX',
    'interests': [
        'web scraping','data engineering','back-end development'
    ],

    'skills': [
        'Python','Pandas','Beautiful Soup','Django','Flask','PostgreSQL',
        'JavaScriipt','MEAN Stack'
    ],

    'projects': [
        {
            'name': 'GameScraper',
            'description': "Gaming news aggregation web scraper",
            'url': 'https://mighty-oasis-10011.herokuapp.com',
            'repo': 'https://github.com/TR-1000/GameScraper',
            'technologies': ['Python','Beautiful Soup','Django'],
            'group_project': False

        },
        {
            'name': 'What Are You Watching Tonight',
            'description': "OMBD movie app",
            'url': 'https://blooming-headland-45308.herokuapp.com',
            'repo': 'https://github.com/TR-1000/probable-potato',
            'technologies': ['Ruby on Rails','React'],
            'group_project': True

        },
        {
            'name': 'FireWatch',
            'description': "A web app for keeping track of major fires across the globe",
            'url': 'https://the-firewatch.herokuapp.com',
            'repo': 'https://github.com/TR-1000/Firewatch',
            'technologies': ['MongoDB','Express','Angular.js', 'Node'],
            'group_project': True

        },
        {
            'name': 'A Game of Phones',
            'description': "A full stack app for logging a smartphone collection",
            'url': 'https://the-phone-book.herokuapp.com',
            'repo': 'https://github.com/TR-1000/aGameOfPhones',
            'technologies': ['Node','Express','MongoDB'],
            'group_project': False

        },
        {
            'name': 'Did I Buy That/Have I Played It?',
            'description': "An app for quickly searching through your Steam library so you don't buy the same game twice.",
            'url': 'https://tr-1000.github.io/steam-api-app',
            'repo': 'https://github.com/TR-1000/TR-1000.github.io/tree/master/steam-api-app',
            'technologies': ['JavaScript', 'jQuery', 'HTML', 'CSS'],
            'group_project': False

        }
    ]
}


for me in Engineer.objects:
    print(me.as_dict())


@app.route('/')
def software_engineer():


    return json.loads(me.to_json())

if __name__ == "__main__":
    app.run(debug=True)
