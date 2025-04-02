class Author:
    def __init__(self, name, biography):
        self.name = name 
        self.biography = biography 

    def view_author_details(self):
        return {
            "Name": self.name,
            "Biography": self.biography
        }




       

