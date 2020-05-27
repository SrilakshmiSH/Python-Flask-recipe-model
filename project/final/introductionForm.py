"""
Introduction form presenter via MethodView
"""
from flask import render_template
from flask.views import MethodView
import recipemodel

class IntroductionForm(MethodView):
    def get(self):
        """This function renders the landing page with introduction.
        The introductionForm.html is rendered on Jinja2 template using render_template
        """
        return render_template('introductionForm.html')