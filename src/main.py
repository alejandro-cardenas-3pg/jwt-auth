from flask import Flask
from blueprints.root_blueprint import root_blueprint


def create_flask_app():

    app = Flask(__name__)

    app.register_blueprint(root_blueprint)

    return app


def main():
    print("Started")
    app = create_flask_app()
    app.run(port=7888)


if __name__ == '__main__':
    main()
