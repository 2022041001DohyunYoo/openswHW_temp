from tkinter import *
import tkinter.ttk
import tkinter.font
from BookList import *



# 옵션 설정 페이지 클래스
class OptionPage(tkinter.Tk):

    def __init__(self, main_page, Book):
        super().__init__()
        self.geometry("650x450")
        self.resizable(width=FALSE, height=FALSE)
        self.title("Book Report Helper")
        self.configure(background="white")
        self.myFont=tkinter.font.Font(family="Pretendard Medium")

        #지정된 책
        self.Book = typeBook("임시", "임시", "임시")
        self.Book = Book

        #이전 페이지
        self.main_page = main_page

        # 맨 위 회색 타이틀 - 고른 책 제목+저자 출력
        Ltitle=Label(self, text="      <%s - %s>"% (self.Book.getTitle(), self.Book.getAuthor()), font=("Pretendard Medium", 14, "italic", "bold"), bg="gray90", anchor="w")
        Ltitle.pack(side="top", fill=X, ipadx=50 , ipady=14)

        Ltitle2=Label(self, text="[감상문 작성 옵션]", font=("Pretendard Medium", 13, "bold"), background="white")
        Ltitle2.place(x=325, y=100, anchor="n")

        Lword_limit=Label(self, text="글자 수 제한: ", font=("Pretendard Medium", 11), background="white")
        Lword_limit.place(x=210, y=150, anchor="n")

        # 글자 제한 입력 칸
        self.Eword_limit=Entry(self, width=35, background="white")
        self.Eword_limit.place(x=200, y=185)

        Lword_level=Label(self, text="어휘 수준: ", font=("Pretendard Medium", 11), background="white")
        Lword_level.place(x=200, y=225, anchor="n")

        #라디오 버튼 - 대학생 이상/어린이 중 택1
        self.wordLevel=IntVar()
        radioButton1=Radiobutton(self, text="대학생 이상 (기본값)", font=("Pretendard Medium", 10), variable=self.wordLevel, value=0, background="white")
        radioButton2=Radiobutton(self, text="어린이", font=("Pretendard Medium", 10), variable=self.wordLevel, value=1, background="white")
        radioButton1.place(x=200, y=270, anchor="w")
        radioButton2.place(x=200, y=300, anchor="w")


        Lkeyword=Label(self, text="키워드: ", font=("Pretendard Medium", 11), background="white")
        Lkeyword.place(x=189, y=320, anchor="n")

        # 키워드 입력 칸
        self.Ekeyword=Entry(self, width=35, background="white")
        self.Ekeyword.place(x=200, y=350)


        # 작성 시작 버튼
        Bwrite=Button(self, text="작성하기", bg="gray90", command=self.show_result)
        Bwrite.place(x=325, y=390, anchor="n")
        Bwrite.pack()

        #이전창으로 돌아가기
        Back=Button(self, text="돌아가기", bg="gray90", command=self.getBack)
        Back.place(x=100, y=100, anchor="n")
        Back.pack()


    # 다음 페이지로 넘어가기
    def show_result(self):


        # 옵션 창에서 입력된 값 저장
        self.keyword=self.Ekeyword.get() 
        self.word_limit=self.Eword_limit.get()
        self.word_level=self.wordLevel.get()

        if self.word_level==0:
            self.word_level="대학생 이상"
        else:
            self.word_level="어린이"

        # 다음 화면 호출
        from results_page import ResultPage
        result_page=ResultPage(self, self.keyword, self.word_level, self.word_limit, self.Book)
        self.destroy()

    def getBack(self):
        self.main_page.deiconify()
        self.destroy()
        
