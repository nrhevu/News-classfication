from tkinter import *
from tkinter import messagebox
import requests
from pyvi import ViTokenizer, ViPosTagger

#Giao dien 
tk = Tk()
lblNhap = Label(tk, text="Nhap link Website", font =("Times New Roman",14), fg = "green")
lblNhap.pack()
tbUser = Entry(tk, width = 30, font = ("Times New Roman",14))
tbUser.pack()

##############################################################################################################

#boc tach du lieu
#lay du lieu dang text tu file html
#def get_page_text(url):
#return requests.get(url).text
def get_text():
    url = tbUser.get()
    #lay code html
    page_text = requests.get(url).text
    #list tag can tach text
    list_text_tag = ['<p', '<i', '<b', '<h1', '<h2', '<h3', '<h4', '<h5', '<h6','<title']
    texts = []
    while True:
        try:
            start_point = page_text.index("<")
            # get tag nameprint(page_text[start_point:])
            end_point = page_text[start_point:].index(">") + start_point            
            # print(start_point, "--" ,end_point)
            opend_tag = page_text[start_point: end_point + 1]            
            tag_name = opend_tag.split(' ')
            if len(tag_name) > 1:
                tag_name = tag_name[0]
            else:
                tag_name = tag_name[0][:-1]
            # tag_name = opend_tag[0:2]            
            care_tag = False
            for tag in list_text_tag:
                if tag == tag_name:                    
                    try:
                        # print("---------------------------------------------------------")
                        close_tag = tag_name[0] + "/" + tag_name[1:] + ">"
                        close_tag_position = page_text.index(close_tag)
                        # print(close_tag_postion, "**")
                        text = page_text[end_point + 1 : close_tag_position].replace("\n", " ")
                        # post processing                      
                        while True:
                            try:
                                t1 = text.index("<")
                                t2 = text.index(">")
                                
                                text = text[:t1] + text[t2+1:]
                                
                            except Exception as e:
                                break
                        
                        texts.append(text)
                        page_text = page_text[close_tag_position +1:]
                        care_tag = True
                        break
                    except Exception as e:
                        
                        pass                    
            if not care_tag:
                page_text = page_text[end_point +1:]

        except Exception as e:
            # print("BBBB", e)
            break
    return texts

##############################################################################################################
#ham click button
def btnShow_click():

#ghi du lieu vao file data.txt
    texts = get_text()
    with open("./Text.txt","w", encoding="utf-8") as f:
        for text in texts:
            for e in text:
                try:
                    f.write(e)
                except:
                    pass
            f.write("\n-------------------\n")
    print(texts)

##############################################################################################################
#thuc hien nut button            
btn = Button(tk,text = "Submit", command = btnShow_click)
btn.pack()
tk.mainloop()
# https://vnexpress.net/cac-chuoi-pizza-burger-kinh-doanh-the-nao-4164734.html

