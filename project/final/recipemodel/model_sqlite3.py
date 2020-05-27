"""
Simple recipesbook flask app
"""

from .Model import Model
import sqlite3
#file for the database
DB_FILE = 'entries.db'

class model(Model):
    def __init__(self):
    	"""
    	Makes sure the connection to database is completed.
    	"""
    	connection = sqlite3.connect(DB_FILE)
    	cursor = connection.cursor()
    	try:
    		cursor.execute("select count(rowid) from recipebook")
    	except sqlite3.OperationalError:
    		cursor.execute("create table recipebook (title text, skillset text)")
    	cursor.close()

    def select(self):
        """
        Fetches all rows from the database
        Each row contains: title,skillset
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM recipebook")
        return cursor.fetchall()

    def insert(self, title, skillset):
        """
        Inserts entry into database
        :param title: String
        :param skillset: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'title':title, 'skillset':skillset}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into recipebook (title, skillset) VALUES (:title,:skillset)", params)
        connection.commit()
        cursor.close()
        return True


        