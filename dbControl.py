from typeBook import *

import sqlite3 # built-in library (Python 2.x & 3.x)

#데이터베이스 조작 클래스
class dbControl :
    #데이터 베이스 설정
    dbpath = "BooksDB.db"
    con = sqlite3.connect(dbpath)
    cursor = con.cursor()

    #기본 생성자
    def __init__(self):
        return

    #db에서 모든 책 정보를 꺼내서 리스트로 만드는 메서드
    def makeListAll(self):

        #sql문
        script = " SELECT * FROM Books "

        #sql문 실행
        self.cursor.execute(script)

        #리스트에 sql문 실행 결과(=배열) 저장
        Books = self.cursor.fetchall()

        #typeBook클래스 배열이 될 예정
        book_list = []

        #실행결과 배열이 끝날때 까지 튜플을 하나씩
        for book in Books:
            #튜플의 멤버를 변수로
            title, author, age = book
            #책 타입의 인스턴스 생성
            book_instance = typeBook(title, author, age)
            #클래스 배열에 append
            book_list.append(book_instance)

        #클래스 배열 반환
        return book_list

    #작가 이름을 검색하여 리스트를 만드는 메서드
    def SearchAuthor(self, name):

        #sql문
        script = " SELECT * FROM Books WHERE author = ?"

        #sql문 실행
        self.cursor.execute(script, (name,))

        #리스트에 sql문 실행 결과(=배열) 저장
        Books = self.cursor.fetchall()

        #typeBook클래스 배열이 될 예정
        book_list = []

        #실행결과 배열이 끝날때 까지 튜플을 하나씩
        for book in Books:
            #튜플의 멤버를 변수로
            title, author, age = book
            #책 타입의 인스턴스 생성
            book_instance = typeBook(title, author, age)
            #클래스 배열에 append
            book_list.append(book_instance)


        #배열 반환
        return book_list


    #책 이름을 검색하여 리스트를 만드는 메서드
    def SearchTitle(self, name):

        #sql문
        script = " SELECT * FROM Books WHERE author = ?"

        #sql문 실행
        self.cursor.execute(script, (name, ))

        #리스트에 sql문 실행 결과(=배열) 저장
        Books = self.cursor.fetchall()

        #typeBook클래스 배열이 될 예정
        book_list = []

        #실행결과 배열이 끝날때 까지 튜플을 하나씩
        for book in Books:
            #튜플의 멤버를 변수로
            title, author, age = book
            #책 타입의 인스턴스 생성
            book_instance = typeBook(title, author, age)
            #클래스 배열에 append
            book_list.append(book_instance)


        #클래스 배열 반환
        return book_list
    
    def searchAge(self, tag):

        #sql문
        script = " SELECT * FROM Books WHERE age = ?"

        #sql문 실행
        self.cursor.execute(script, (tag, ))

        #리스트에 sql문 실행 결과(=배열) 저장
        Books = self.cursor.fetchall()

        #typeBook클래스 배열이 될 예정
        book_list = []

        #실행결과 배열이 끝날때 까지 튜플을 하나씩
        for book in Books:
            #튜플의 멤버를 변수로
            title, author, age = book
            #책 타입의 인스턴스 생성
            book_instance = typeBook(title, author, age)
            #클래스 배열에 append
            book_list.append(book_instance)


        #클래스 배열 반환
        return book_list




    

