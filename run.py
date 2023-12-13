from flask import Flask
from app.routes.patient_router import patient_bp

app = Flask(__name__)

# Register the patient blueprint
app.register_blueprint(patient_bp)

if __name__ == '__main__':
    app.run(debug=True)