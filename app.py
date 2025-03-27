
from flask import Flask, render_template, request, flash, redirect, url_for

from src.database.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://admin:admin@localhost/hoteldb'

db.init_app(app)

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

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template("admin-dashboard.html")

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        address = request.form.get('address')
        registration_date = datetime.utcnow()

        if len(full_name) < 4:
            flash('Full name must be greater than 3 characters', category='error')
        elif len(address) < 6:
            flash('Must be a valid address', category='error')
        else:
            new_customer = customers_bp(full_name = full_name, address=address, registration_date=registration_date)
            db.session.add(new_customer)
            db.session.commit()
            flash('New customer profile created successfully!', category='success')
    
    return render_template("sign_up.html")

if __name__ == '__main__':
    app.run(debug=True)

