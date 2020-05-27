"""
Base class for recipe model
"""
class Model():
    def select(self):
        """
        This function returns all the records in the recipe model.
        :return: python list containing all the elements. 
        """
        pass

    def insert(self, title, skillset):
        """
        Inserts entry into the database
        :param title: String
        :param skillset: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass

        