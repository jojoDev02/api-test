from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.customer.customer_routes import customer_bp

from db.database import init_db
app = Flask(__name__)


app.register_blueprint(customer_bp)

init_db()
app.run(debug=True)
