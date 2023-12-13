# app/routes/__init__.py

from patient_router import patient_bp

# Optionally, you can define a list of blueprints to be used elsewhere
__all__ = ['patient_bp']