from flask_api import FlaskAPI
from mongoengine import connect
import mongoengine as mongo
import json
import dns # install dnspython to use mongodb connection string
# load envirinment variabless
from dotenv import load_dotenv
import os

load_dotenv()
connection_string = os.environ.get('MONGODB_URI')
connect(host=connection_string)


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
            'email': self.email,
            'githud': self.github,
            'linkedin': self.linkedin,
            'location': self.location,
            'interests': self.interests,
            'skills': self.skills,
            'projects': self.projects,
        }



@app.route('/')
def software_engineer():
    # get engineer with matching id string and jsonify it
    me = json.loads(Engineer.objects(id='5eaf9af9c9b2042506ebd784').to_json())[0]
    # remove the id key with pop and return
    me.pop('_id')
    return me



if __name__ == "__main__":
    app.run(debug=True)
