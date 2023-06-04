from tkinter import *
import tkinter.ttk
import tkinter.font
import clipboard
import bookGPT
from typeBook import *
import multiprocessing as mp


# 해결할 문제: 1. 결과 텍스트 영역 스크롤  2. 화면 전환 후 이전 윈도우 창 안 사라짐


# 결과 페이지 클래스
class ResultPage(tkinter.Toplevel):

    def __init__(self, master, keyword, word_level, word_limit, Book): # 책 제목, 저자, 글자 제한, 키워드, 어휘 수준 전달 필요??
        super().__init__(master)

        self.keyword=keyword
        self.word_level=word_level
        self.word_limit=word_limit
        #지정된 책
        self.Book = typeBook("임시", "임시", "임시")
        self.Book = Book

        #api 키
        openai.api_key = "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"

        def Copy(text):
            clipboard.copy(text)

        rpage=Tk()
        rpage.geometry("650x800")
        rpage.resizable(width=FALSE, height=FALSE)
        rpage.configure(background="white")
        rpage.title("Book Report Helper")


        # 폰트 설치
        myFont=tkinter.font.Font(family="Pretendard Medium")
        myFont2=tkinter.font.Font(family="Pretendard")

        # 맨 위 회색 음영 타이틀
        Ltitle=Label(rpage, text="      <제목 - 저자>  작성 완료!", font=("Pretendard Medium", 14, "italic", "bold"), bg="gray90", anchor="w")
        Ltitle.pack(side="top", fill=X, ipady=14)

        ## 테스트용 문장
        review_fromGPT= self.Book.Review()
        summary_fromGPT= self.Book.Summary()
        quote_fromGPT=self.Book.Quote()
        debate_fromGPT=self.Book.Debate()

        ############### 전체 화면 스크롤 ##############
        base_frame=Frame(rpage, bg="white")
        base_frame.pack(side=TOP, fill=BOTH, expand=1)

        base_canvas=Canvas(base_frame, bg="white")
        base_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        base_scrollbar=Scrollbar(base_frame, orient=VERTICAL, command=base_canvas.yview)
        base_scrollbar.pack(side=RIGHT, fill=Y)
        base_canvas.configure(yscrollcommand=base_scrollbar.set)
        base_canvas.bind("<Configure>", lambda e: base_canvas.configure(scrollregion=base_canvas.bbox("all")))

        ############## 위젯 들어가는 프레임 ############
        box_frame=Frame(base_canvas, bg="white")
        base_canvas.create_window((53,30), window=box_frame, anchor="nw")


        ### 감상문 결과 영역 ###

        Lt_review=Label(box_frame, text="     [감상문]", font=("Pretendard Medium", 13, "bold"), bg="white")
        Lt_review.grid(row=0, column=0, sticky="w", rowspan=2, columnspan=2, pady=28)

        # 감상문 텍스트 영역 스크롤 (미완성)
        review_base_frame=Frame(box_frame, bg="red")
        review_base_frame.grid()
        review_base_canvas=Canvas(review_base_frame, bg="black")
        review_base_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        review_scroll=Scrollbar(review_base_frame, orient=VERTICAL, command=review_base_canvas.yview)
        review_scroll.pack(side=RIGHT, fill=Y)
        review_base_canvas.configure(yscrollcommand=review_scroll.set)
        review_base_canvas.bind("<Configure>", lambda e: review_base_canvas.configure(scrollregion=review_base_canvas.bbox("all")))

        review_box=Frame(review_base_canvas, bg="white", width=66)
        review_base_canvas.create_window((0, 0), window=review_box, anchor="nw")

        Lreview=Label(review_box, text=review_fromGPT, justify="left", font=("Pretendard Medium", 10), width=66, height=15, relief="groove", borderwidth=2, bg="white", anchor="nw", wraplength=500)
        Lreview.pack(side=TOP, fill=BOTH, expand=1)

        Breview_copy=Button(box_frame, text="copy", font=("Pretendard", 10), bg="gray90", width=8, height=2, command=lambda:Copy(review_fromGPT))
        Breview_copy.grid(rowspan=3, columnspan=2, sticky="e", pady=15)

        ### 줄거리 요약 영역 ###

        Lt_summary=Label(box_frame, text="    [줄거리 요약]", font=("Pretendard Medium", 13, "bold"), bg="white")
        Lt_summary.grid(sticky="w", pady=32)

        Lsummary=Label(box_frame, text=summary_fromGPT, justify="left", font=("Pretendard Medium", 10), width=66, height=15, relief="groove", borderwidth=2, bg="white", anchor="nw", wraplength=500)
        Lsummary.grid()

        Bsummary_copy=Button(box_frame, text="copy", font=("Pretendard", 10), bg="gray90", width=8, height=2, command=lambda:Copy(summary_fromGPT))
        Bsummary_copy.grid(sticky="e", pady=15)

        ### 문장 인용 영역 ###

        Lt_quote=Label(box_frame, text="      [문장 인용 및 이유]", font=("Pretendard Medium", 13, "bold"), bg="white")
        Lt_quote.grid(sticky="w", pady=32)

        Lquote=Label(box_frame, text=quote_fromGPT, justify="left", font=("Pretendard Medium", 10), width=66, height=15, relief="groove", borderwidth=2, bg="white", anchor="nw", wraplength=500)
        Lquote.grid()

        Bquote_copy=Button(box_frame, text="copy", font=("Pretendard", 10), bg="gray90", width=8, height=2, command=lambda:Copy(quote_fromGPT))
        Bquote_copy.grid(sticky="e", pady=15)

        ### 토론 주제 영역 ###

        Lt_debate=Label(box_frame, text="     [토론 주제 및 의견]", font=("Pretendard Medium", 13, "bold"), bg="white")
        Lt_debate.grid(sticky="w", pady=32)

        Ldebate=Label(box_frame, text=debate_fromGPT, justify="left", font=("Pretendard Medium", 10), width=66, height=15, relief="groove", borderwidth=2, bg="white", anchor="nw", wraplength=500)
        Ldebate.grid()

        Bdebate_copy=Button(box_frame, text="copy", font=("Pretendard", 10), bg="gray90", width=8, height=2, command=lambda:Copy(debate_fromGPT))
        Bdebate_copy.grid(sticky="e", pady=15)




        # 테스트용
        ''' 
        self.geometry("650x450")
        self.resizable(width=FALSE, height=FALSE)
        self.title("Book Report Helper")
        self.configure(background="white")
        
        self.myFont=tkinter.font.Font(family="Pretendard Medium")
        self.myFont2=tkinter.font.Font(family="Pretendard")


        
        self.rpage=Label(self, text=f"word limit >> {self.word_limit}", width=100, bg="white", font=("Pretendard"))
        self.rpage.pack()
        self.rpage2=Label(self, text=f"keyword >> {self.keyword}", width=100, bg="white", font=("Pretendard"))
        self.rpage2.pack()
        self.rpage3=Label(self, text=f"word level >> {self.word_level}", width=100, bg="white", font=("Pretendard"))
        self.rpage3.pack()
        '''
        



