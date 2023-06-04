import sqlite3 

#txt 파일에서 책 정보를 읽어서 db 파일로 만들어주는 프로그램
#한번 db파일을 만들었으면 수정사항 있지 않은 이상 재실행 필요 x

#sql 정보
dbpath = "BooksDB.db"
con = sqlite3.connect(dbpath)
cursor = con.cursor()

#파일 열기
f = open("책목록.txt", 'r', encoding='UTF8')

#제목과 작가라는 두가지 속성을 가지는 Books라는 테이블을 생성

script = "CREATE TABLE Books(Title text, Author text, Age text);"
cursor.execute(script)

while (1):

    #txt파일에서 한줄씩 읽어서 (파일에서 제목과 작가는 두줄 단위로 묶여 있음)
    title = f.readline()
    if not title : break
    author = f.readline()
    if not author : break
    age = f.readline()
    if not age : break

    # 개행 문자 제거
    title = title.strip()
    author = author.strip()
    age = age.strip()


    #제목과 작가의 정보를 가진 튜플 생성
    script = "INSERT INTO Books VALUES(?, ?, ?);"
  
    cursor.execute(script, (title, author, age))

#커밋
con.commit()


script = "SELECT * FROM Books;"
cursor.execute(script)

result = cursor.fetchall()

for n in result :
    print(n)

f.close()
