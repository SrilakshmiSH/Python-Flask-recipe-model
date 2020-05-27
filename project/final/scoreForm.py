"""
scoreForm presenter via MethodView
"""
from flask import render_template, redirect, request, url_for
from flask.views import MethodView
from google.cloud import language
from google.cloud.language import types
from google.cloud.language import enums
import six
import recipemodel
import sqlite3
DB_FILE = 'entries.db'

class ScoreForm(MethodView):		
	def get(self):
		"""
		This function fetches the recipe title for all the entries of the recipe model. It uses HTTP via get() method.
		The recipe titles are rendered on the 'scoreForm.html' web page using the render_template.  
		"""
		model = recipemodel.get_model()
		rpnames = [elements[0] for elements in model.select()]
		return render_template('scoreForm.html',rpnames=rpnames)
		
	def sentiment_text(self, text):
		"""
		This function performs sentiment analysis based on the text value.
		:param text: String - text is the skillset value for the selected recipe.
		Here, a client object is created for language services. 
		Using google cloud language, a document is created having the context as text and type as PLAIN_TEXT.
		Next, sentiment analysis is performed on this document. It returns score and magnitude.
		:return: the sentiment score calculated for the text value(skillset)
		"""
		self.client = language.LanguageServiceClient()
		self.document = types.Document(content=text,type=enums.Document.Type.PLAIN_TEXT)
		self.sentiment = self.client.analyze_sentiment(self.document).document_sentiment
		return(self.sentiment.score)
		
	def init_db(self, rtitle):
		"""
		This function establishes connection to the database(entries.db file) and obtains the skillset for the recipe.
		:param rtitle: String - is the recipe title which is selected by the user.
		First, a connection to the database file is made. 
		Using a cursor object, a sql query is executed to fetch the skillset.
		:return: the skillset value for the selected recipe. 
		"""
		self.connection = sqlite3.connect(DB_FILE)
		self.c = self.connection.cursor()
		self.query_result = self.c.execute("SELECT skillset FROM recipebook WHERE title = ?",[rtitle])
		answer = self.query_result.fetchone()
		self.connection.close()
		return(answer[0])
	 
	def post(self):
		"""
		This function accepts the POST requests and processes the form.
		Using the request object, the recipe title selected by the user is obtained. 
		To fetch the skillest for the recipe title, a connection to the database is established and the skillset is obtained.
		Based on the sentiment score for the text, condition check is performed and a boolean is assigned value.
		If score is less than 0.4, the recipe skillset is difficult, else the skillset is either easy or very easy.
		[Since sentiment analysis generates a lower score for negative words such as difficult]
		The boolean value and score are rendered on the web page using render_template object.
		"""
		self.recipetitle = request.form.get('rname1')
		self.recipeskill = self.init_db(self.recipetitle)
		self.score_result = self.sentiment_text(self.recipeskill)
		if (self.score_result < 0.4):
			return_bool = True
		else:
			return_bool = False
		return render_template('scoreForm.html',boolvalue=return_bool,score=self.score_result)
