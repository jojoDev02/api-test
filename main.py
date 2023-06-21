from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.restaurante.restaurante_routes import restaurante_bp

from db.database import init_db
app = Flask(__name__)




app.register_blueprint(restaurante_bp)

init_db()
app.run(debug=True)
