"""
insertForm presenter via MethodView
"""
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import recipemodel

class InsertForm(MethodView):
    def get(self):
        """This function renders the insert form.
        The insertForm.html is rendered on Jinja2 template using render_template
        """
        return render_template('insertForm.html')

    def post(self):
        """
        Accepts POST requests, and processes the form.
        Redirects to introduction form when completed.
        """
        model = recipemodel.get_model()
        model.insert(request.form['title'],request.form['skillset'])
        return redirect(url_for('introductionForm'))
        