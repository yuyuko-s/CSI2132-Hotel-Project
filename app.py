from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://admin:admin@localhost/hoteldb'

db = SQLAlchemy(app)

from src.controllers.customers import customers_bp
from src.controllers.employees import employees_bp
from src.controllers.hotel_chains import hotel_chains_bp
from src.controllers.hotels import hotels_bp
from src.controllers.rentings import rentings_bp
from src.controllers.rooms import rooms_bp

app.register_blueprint(hotel_chains_bp, url_prefix='/api')
app.register_blueprint(hotels_bp, url_prefix='/api')
app.register_blueprint(rooms_bp, url_prefix='/api')
app.register_blueprint(customers_bp, url_prefix='/api')
app.register_blueprint(rentings_bp, url_prefix='/api')
app.register_blueprint(employees_bp, url_prefix='/api')


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run()

