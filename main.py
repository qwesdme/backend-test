from flask import Flask
from flask_restful import Api

from resources.posts import Posts
from resources.comments import Comments

app = Flask(__name__)
api = Api(app)

resources = [Posts, Comments]

for resource in resources:
    api.add_resource(resource, resource.route)

if __name__ == '__main__':
    app.run(debug=True)
