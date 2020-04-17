from flask_api import FlaskAPI
from flask import Blueprint

theme = Blueprint(
    'flask-api', __name__,
    url_prefix='/flask-api',
    template_folder='templates', static_folder='static'
)


app = FlaskAPI(__name__)
app.blueprints['flask-api'] = theme


engineer = {
    'name': 'Takia Ross',
    'email': 't.l.ross@outlook.com',
    'github': 'https://github.com/TR-1000',
    'linkedin': 'http://linkedin.com/in/takia-ross',
    'location': 'San Antonio, TX',
    'interests': [
        'web scraping','data engineering','back-end development'
    ],

    'skill': [
        'Python','Pandas','Django','Flask','Beautiful Soup','PostgreSQL',
        'JavaScriipt','MEAN Stack'
    ],

    'projects': [
        {
            'name': 'GameScraper',
            'description': "Gaming news aggregation web scraper",
            'technologies': ['Python','Beautiful Soup','Django'],
            'url': 'https://mighty-oasis-10011.herokuapp.com',
            'repo': 'https://github.com/TR-1000/GameScraper',
            'group_project': False

        },
        {
            'name': 'What Are You Watching Tonight',
            'description': "OMBD movie app",
            'technologies': ['Ruby on Rails','React'],
            'url': 'https://blooming-headland-45308.herokuapp.com',
            'repo': 'https://github.com/TR-1000/probable-potato',
            'group_project': True

        },
        {
            'name': 'FireWatch',
            'description': "A web app for keeping track of major fires across the globe",
            'technologies': ['MongoDB','Express','Angular.js', 'Node'],
            'url': 'https://the-firewatch.herokuapp.com',
            'repo': 'https://github.com/TR-1000/Firewatch',
            'group_project': True

        },
        {
            'name': 'A Game of Phones',
            'description': "A full stack app for logging a smartphone collection",
            'technologies': ['Node','Express','MongoDB'],
            'url': 'https://the-phone-book.herokuapp.com',
            'repo': 'https://github.com/TR-1000/aGameOfPhones',
            'group_project': False

        },
        {
            'name': 'Did I Buy That/Have I Played It?',
            'description': "An app for quickly searching through your Steam library so you don't buy the same game twice.",
            'technologies': ['JavaScript', 'jQuery', 'HTML', 'CSS'],
            'url': 'https://tr-1000.github.io/steam-api-app',
            'repo': 'https://github.com/TR-1000/TR-1000.github.io/tree/master/steam-api-app',
            'group_project': False


        }
    ]
}

@app.route('/software_enginner/')
def software_engineer():
    return engineer


if __name__ == "__main__":
    app.run(debug=True)
