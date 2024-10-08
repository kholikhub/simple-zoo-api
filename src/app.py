from flask import Flask
from blog.routes.post_routes import post_routes
from animals.animal_routes import animal_routes
from flasgger import Swagger

app = Flask(__name__)
app.register_blueprint(post_routes)
app.register_blueprint(animal_routes)
swagger = Swagger(app)

@app.route("/")
def home():
    return "This is ZOO API"


@app.errorhandler(404)
def page_not_found(e):
    return {'message': 'The requested URL was not found on the server.'}, 404

if __name__ == '__main__':
    app.run(debug=True, port=8080)