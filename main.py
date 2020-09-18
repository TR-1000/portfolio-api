# Thank's for checking out my api/portfolio!



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


class Experience(mongo.EmbeddedDocument): # Embedded document class
    company = mongo.StringField()
    start_date = mongo.StringField()
    end_date = mongo.StringField()
    description = mongo.StringField()



class School(mongo.EmbeddedDocument):
    school = mongo.StringField()
    credential = mongo.StringField()
    field_of_study = mongo.StringField()
    location = mongo.StringField()
    year = mongo.StringField()


class Engineer(mongo.Document):
    last_name = mongo.StringField(required=True)
    first_name = mongo.StringField(required=True)
    location = mongo.StringField(required=True)
    interests = mongo.ListField()
    skills = mongo.ListField()
    experience = mongo.EmbeddedDocumentListField(Experience)
    education = mongo.EmbeddedDocumentListField(School)

    def as_dict(self):
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'location': self.location,
            'interests': self.interests,
            'skills': self.skills,
            'experience': self.projects,
            'education': self.projects
        }


@app.route('/')
def software_developer():
    # get engineer with matching id string and jsonify it
    me = json.loads(Engineer.objects.to_json())[0]
    # remove the id key with pop and return
    me.pop('_id')
    return me



if __name__ == "__main__":
    app.run(debug=True)
