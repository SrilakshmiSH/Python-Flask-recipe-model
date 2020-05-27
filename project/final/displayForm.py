"""
displayForm presenter via MethodView
"""
from flask import render_template
from flask.views import MethodView
import recipemodel

class DisplayForm(MethodView):
	def get(self):
		"""This function gets all the entries of the recipe model. It uses HTTP GET via get() method.
		The recipe entries are rendered on the 'translateForm.html' web page using the render_template object.
		"""
		model = recipemodel.get_model()
		entries = [dict(title=elements[0],skillset=elements[1]) for elements in model.select()]
		return render_template('displayForm.html',entries=entries)