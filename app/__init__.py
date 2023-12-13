from flask import Flask

# Create a SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    # Create an instance of the Flask application
    app = Flask(__name__)

    # Load configuration from a config file or set it directly
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the Flask app
    db.init_app(app)

    # Import and register blueprints (if used)
    from .routes import patient_routes, history_routes, appointment_routes
    app.register_blueprint(patient_routes.bp)
    app.register_blueprint(history_routes.bp)
    app.register_blueprint(appointment_routes.bp)

    return app
