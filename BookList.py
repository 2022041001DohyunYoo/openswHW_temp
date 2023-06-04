from dbControl import *

class BookList :

    BookList = []

    def __init__(self):
        openai.api_key = "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"

    def __iter__(self):
        return iter(self.BookList)

    def callDB(self) :
        DB = dbControl()
        self.BookList = DB.makeListAll()

    def searchAuthor(self, author_name) :
        DB = dbControl()
        self.BookList = DB.SearchAuthor(author_name)

    def searchTitle(self,title_name) :
        DB = dbControl()
        self.BookList = DB.SearchTitle(title_name)

    def searchAge(self, age_tag) :
        DB = dbControl()
            
        if(age_tag == 0):
                age_string = "기본"
                self.BookList = DB.searchAge(age_string)
        elif(age_tag == 1):
                age_string = "어린이"
                self.BookList = DB.searchAge(age_string)

    def index(self, num):
         return self.BookList[num]
         
