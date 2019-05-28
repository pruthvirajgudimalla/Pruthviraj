from tkinter import *
import math



top = Tk()

text = StringVar()
operator=""

def get(number):
    global operator
    operator = operator + str(number)
    text.set(operator)


def clear():
	global operator
	operator = ""
	text.set(operator)
	
def equals():
	global operator
	global sumup
	sumup = str(eval (operator))
	text.set(sumup)
	operator=sumup
	
def back():
	txtbox.delete(0)
	global operator
	operator = text.get()
	text.set(operator)
		
def Exit():
	top.destroy()


#================================================Label===============================================

ban = Label(top , text = "Built Using Python"   , height = 3, width =31 , bg = 'light blue' , font = 'calibri 10 ' , fg ='black').grid()





head = Label( top , text = "MY CALCULATOR" ,height = 3, width = 32 ,fg ='white', font = 'courier 9' , bg = 'black' ,).grid()


#--------------------------------------------------------------------Text Box ---------------------------

display = Frame(top)
display.grid()

txtbox = Entry( display,  bd =15 ,width = 11, textvariable = text , font='calibri 25', justify=RIGHT )
txtbox.grid(row = 1 , column =1 ,columnspan = 5 )

#====================================================row 2==============================================

a = Frame(top)
a.grid()

butAC = Button( a , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'orange' , height =2 , width = 4 , command = clear ,
                text = 'AC' , bg='white').grid(row = 2 , column = 1)

butback = Button( a , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4,
                text = '<--' , bg='white' ,command = back).grid(row = 2 , column = 2)


butmod = Button( a , bd = 3 , font =('calibri',10, 'bold') , fg= 'black' , height =2 , width = 4 ,
                text = '%' , bg='white' , command=lambda:get('%')).grid(row = 2 , column = 3)


butdiv = Button( a , bd = 3 , font =('calibri',10, 'bold') , fg= 'black' , height =2 , width = 4  ,
                text = '/' , bg='white'  , command=lambda:get('/')).grid(row = 2 , column = 4)



#====================================================row 3==============================================

b = Frame(top)
b.grid()

but7 = Button( b , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4  ,
                text = '7' , bg='white'  , command=lambda:get('7')).grid(row = 3 , column =1)

but8 = Button( b , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4 ,
                text = '8' , bg='white' , command=lambda:get('8')).grid(row = 3 , column = 2)


butm9 = Button( b , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4 ,
                text = '9' , bg='white' , command=lambda:get('9')).grid(row = 3 , column = 3)


butmul = Button( b , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4  ,
                text = '×' , bg='white' , command=lambda:get('*')).grid(row = 3 , column = 4)




#====================================================row 4==============================================

c = Frame(top)
c.grid()

but4 = Button( c , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4  ,
                text = '4' , bg='white' , command=lambda:get('4')).grid(row = 4 , column = 1)

but5 = Button( c , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4  ,
                text = '5' , bg='white' , command=lambda:get('5')).grid(row = 4 , column = 2)


but6 = Button( c , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4    ,
                text = '6' , bg='white' , command=lambda:get('6')).grid(row = 4 , column = 3)


butsub = Button( c , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4  , 
                text = '-' , bg='white' , command=lambda:get('-')).grid(row = 4 , column = 4)




#====================================================row 5==============================================

d = Frame(top)
d.grid()


but1 = Button( d , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4  , 
                text = '1' , bg='white' , command=lambda:get('1')).grid(row = 5 , column = 1)

but2 = Button( d , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4  ,
                text = '2' , bg='white' , command=lambda:get('2')).grid(row = 5 , column = 2)


but3 = Button( d , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4 ,
                text = '3' , bg='white' , command=lambda:get('3')).grid(row = 5 , column = 3)


butadd = Button( d , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4  ,
                text = '+' , bg='white' , command=lambda:get('+')).grid(row = 5 , column = 4)




#====================================================row 6==============================================

e = Frame(top)
e.grid()


butexit = Button( e , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4  , command = exit , 
                text = 'Exit' , bg='white').grid(row = 6 , column = 1)

but0 = Button( e , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4  , 
                text = '0' , bg='white' , command=lambda:get('0')).grid(row = 6 , column = 2)


butdot = Button( e , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4 , 
                text = '.' , bg='white' , command=lambda:get('.')).grid(row = 6 , column = 3)


butequal = Button( e , bd = 3 , font =('calibri' ,10, 'bold') , fg= 'black' , height =2 , width = 4  , command = equals ,
                text = '=' , bg='orange').grid(row = 6 , column =4)




deli = 200   # milliseconds of delay per character
svar = StringVar()
ban = Label(top , textvariable = svar , height = 3 , width =37 , bg = 'light blue')

def shif():
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    top.after(deli, shif)

shif.msg = '                     -- Designed by ©Pruthviraj '
shif()
ban.grid()


top.mainloop()
