from bookGPT import *

#책 클래스
class typeBook :
    #클래스 멤버(제목, 저자, gpt 인스턴스)
    title = ""
    author = ""
    age = ""

    #생성자
    def __init__(self, title, author, age) :
        self.title = title
        self.author = author
        self.age = age

    def __init_subclass__(cls) -> None:
        pass

    #책 감상 생성 메서드
    def Review(self) :
        return bookGPT.review(self.title, self.author)

    #
    def Debate(self) :
        return bookGPT.debate(self.title, self.author)
    
    def Quote(self) :
        return bookGPT.quote(self.title, self.author)
    
    def Summary(self) :
        return bookGPT.summary(self.title, self.author)
    
    def setTitle(self, title) :
        self.title = title

    def getTitle(self) :
        return self.title

    def setAuthor(self, author) :
        self.author = author

    def getAuthor(self) :
        return self.author   
    
    def setAge(self, age):
        self.age = age

    def getAge(self, age):
        return self.age
