from logging import root
from tkinter import*
import tkinter
import tkinter as tk
from BookList import *
from tkinter import ttk
import tkinter.font



class MainPage(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("650x450")
        self.resizable(width=FALSE, height=FALSE)
        self.title("Book Report Helper")
        self.configure(background="white")
        self.myFont=tkinter.font.Font(family="Pretendard Medium")

        

        photo = tkinter.PhotoImage(file = "logo.png")
        label1=Label(self, image=photo)
        label1.configure(bg='white')
        label1.pack()
        ent=Entry(self)
        ent.pack()
        self.configure(bg='white')
        listbox = tkinter.Listbox(self, selectmode='extended', height=0)
        listbox.pack(side="left", padx=160, pady=0)
        listbox.place(x=200, y=265)

        self.List = BookList()
        self.List.callDB()

        #각 버튼에 매핑되는 동작에서, book이 제대로 전달 x

        count = 0
        for Book in self.List :
            listbox.insert(count , Book.getTitle() + " / " + Book.getAuthor())
            count = count + 1
    
        listbox.place()

        #책 선택
        Select=Button(self, text="선택", bg="gray90", command=lambda: self.ChooseBook(listbox.curselection()))
        Select.place(x=100, y=100, anchor="n")
        Select.pack()
        
            

        self.mainloop()


    def ChooseBook(self,selected_indices):
        print("ChooseBook called")

        if selected_indices:
            click = int(selected_indices[0])
            ChosenBook = self.List.index(click)
            from options_page import OptionPage
            options_page= OptionPage(self, ChosenBook)
            self.withdraw()  # 현재 페이지 숨기기
            options_page.mainloop()  # 새로운 페이지 실행

   

if __name__ == "__main__":
    main_page=MainPage()
    
    main_page.mainloop()


