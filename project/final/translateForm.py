"""
translateForm presenter via MethodView
"""
from flask import render_template, redirect, request, url_for
from flask.views import MethodView
from google.cloud import translate
import recipemodel

class TranslateForm(MethodView):
	def get(self):
		"""
		This function fetches the recipe title for all the entries of the recipe model. It uses HTTP via get() method.
		The recipe titles are rendered on the 'translateForm.html' web page using the render_template object.
		"""
		model = recipemodel.get_model()
		recipenames = [elements[0] for elements in model.select()]
		return render_template('translateForm.html', recipenames=recipenames)

	def translate_text(self, text, target):
		"""
		This function creates a translate client to perform translation. 
		:param text: String - text is the recipe title be translated. 
		:param target: String - target language into which the translation must be perfomed.
		Here, using the client object, google translate method is called by passing two arguments. 
		From the different return values of the translate method, we fetch the translated text.
		:return: the translation of the given text.
		"""
		self.translate_client = translate.Client()
		self.result = self.translate_client.translate(text, target_language=target)
		return self.result['translatedText']

	def post(self):
		"""
		This function accepts the POST requests and processes the form. 
		Using the request object, the recipe title selected by the user is obtained. 
		Here language name and its translations are stored as a list. A nested list is used to store all the items together.
		Different translations are made to french, german and hindi.
		The nested list is rendered on the webpage using render_template object. 
		"""
		self.selectedRecipe = request.form.get('rname')
		translatedRecipes=[]
		translatedRecipes.append(['English', self.selectedRecipe])
		translatedRecipes.append(['French', self.translate_text(self.selectedRecipe,'fr')])
		translatedRecipes.append(['Hindi', self.translate_text(self.selectedRecipe,'hi')])
		translatedRecipes.append(['German', self.translate_text(self.selectedRecipe,'de')])
		return render_template('translateForm.html', translatedRecipes=translatedRecipes)
