model_backend = 'sqlite3'

if model_backend == 'sqlite3':
    from .model_sqlite3 import model
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
	"""Instantiates the model returned by get_model(). It is executed upon import from app.py.
	   raises Value error when no correct model is imported and databackend is not configured."""
	return appmodel
