from tkinter import *
from tkinter import messagebox

import re
import sys
import requests

#Giao dien
tk = Tk()
lblNhap = Label(tk, text="Nhap link Website", font =("Times New Roman",14), fg = "green")
lblNhap.pack()
tbUser = Entry(tk, width = 30, font = ("Times New Roman",14))
tbUser.pack()

#boc tach du lieu
#lay du lieu dang text tu file html
def get_page_text(url):
    return requests.get(url).text

#lay tat ca the html
def get_text_by_tag(data, tag):
    pattern = '<{0}.*?>.+?</{0}>'.format(tag)
    p = re.compile(pattern)
    return p.findall(data)

#lay phan text trong the html
def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

#ham click button
def btnShow_click():
#lay du lieu trong tbUser khi nhap vao
    a = tbUser.get()
#lay du lieu trong link html
# url = "https://docs.python.org/3/howto/regex.html"
    page_text = get_page_text(a)
#nhap vao the can lay du lieu
    tag = sys.argv[1]
#lay phan text trong the
    text_list = get_text_by_tag(page_text, tag) 
#ghi du lieu vao file data.txt
    with open("data.txt","w") as file:
        for text in text_list:
            text = remove_html_tags(text)
            try:
                file.write(text)
            except:
                pass

#thuc hien nut button            
btn = Button(tk,text = "Submit", command = btnShow_click)
btn.pack()
tk.mainloop()

