from flask_app import app
from burger import Burger
from flask_app.controllers import burgers


if __name__=="__main__":
    app.run(debug=True)