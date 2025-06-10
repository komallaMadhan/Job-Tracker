from flask import Flask
from routes import routes
import os

app = Flask(__name__)
app.register_blueprint(routes)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        from models import db
        db.init_app(app)
        db.create_all()
    app.run(debug=True, port=8000)
