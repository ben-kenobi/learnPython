import tkinter as t
from PIL import Image,ImageTk
import requests as req
from bs4 import BeautifulSoup as bs

def onclick():
    print("clicl")
#root = t.Tk()
#root.title("title")
#root.geometry("400x500")
#path = "/Users/hui/Desktop/1.png"
#img = Image.open(path)
#photo = ImageTk.PhotoImage(img)
#lab = t.Label(root,text="hfffhh",bg="red",compound="center",image=photo,width=300,height=200,font=("黑体",20))
#lab.pack(side='left')
#btn = t.Button(root,text="hahah",fg="red",compound="center",image=photo,width=300,height=200,command=onclick)
#btn.pack(side='bottom')

#title = t.Entry(root,text="title")
#title.place(relx=0.2,rely=0.5,relwidth=0.4,relheight=0.7)



#root.mainloop()
resp = req.get("http://www.weather.com.cn/weather/101210101.shtml")
resp.encoding = 'utf-8'
print(resp.status_code)
print(resp.headers)


bsparsed = bs(resp.text,'html.parser')
print(bsparsed.find_all(attrs={'id':"7d"}))
a = bsparsed.find('div',attrs={'id':"7d"})
lis = a.find('ul').find_all('li')
with open('aa.py','w+') as f:
    for li in lis:
        print(li.find('h1').string)
        f.write(li.find('h1').string)
        print(li.find('p',attrs={'class':'wea'}).string)
        f.write(li.find('p',attrs={'class':'wea'}).string)
        tem = li.find('p',attrs={'class':'tem'})
        high = tem.find('span')
        low = tem.find('i')
        if high is not None:
            print(high.string)
            f.write(high.string)
        if low is not None:
            print(low.string)
            f.write(low.string)
        

print(len(a))


