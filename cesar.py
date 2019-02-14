from tkinter import *

myList=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
myList2=myList.copy()
myList2.append(myList[0])
myList2.append(myList[1])
myList2.append(myList[2])

del myList2[0:3]
print (myList2)

def getFunctionEncrypt():
    encryptedText=""
    test=Entry1.get()
    text.delete(1.0,END)
    for x in test:
        if x.upper() not in myList:
            encryptedText+=x
            print(x+" not in")
        elif x.isupper():
            encryptedText+=myList2[myList.index(x)]
        elif x.islower():
              tempString=myList2[myList.index(x.upper())]
              encryptedText+=tempString.lower()
    print(encryptedText)
    text.insert(END,encryptedText)   

def getFunctionDecrypt():
    encryptedText=""
    test=Entry1.get()
    text.delete(1.0,END)
    for x in test:
        if x.upper() not in myList2:
            encryptedText+=x
            print(x+" not in")
        elif x.isupper():
            encryptedText+=myList[myList2.index(x)]
        elif x.islower():
              tempString=myList[myList2.index(x.upper())]
              encryptedText+=tempString.lower()
    print(encryptedText)
    text.insert(END,encryptedText)          



      


top=Tk()
print()


Labelinput=Label(top, text="User name")
Labelinput.pack()

Entry1=Entry(top,bd=20)
Entry1.pack()

button=Button(top, text="Encrypt", command=getFunctionEncrypt)
button.pack()
button=Button(top, text="Decrypt", command=getFunctionDecrypt)
button.pack()

text=Text(top,height=5,width=50)
text.pack()

top.mainloop()

