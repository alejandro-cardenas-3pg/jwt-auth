from flask import Flask


def create_flask_app():

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, World"

    return app


def main():
    print("Started")
    print("Hello world")
    app = create_flask_app()
    app.run(port=7888)


if __name__ == '__main__':
    main()
