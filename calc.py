from tkinter import *
v=""
def inp(n,E):
	global v
	v=v+str(n)
	E.set(v)
	
def EV(E):#new
	global v
	try:
		r=str(eval(v))
		E.set(r)
		v=""
	except:
		v=""#new
w=Tk()
E=StringVar()
t1=Entry(w,justify="right",textvariable=E)
t1.grid(columnspan=4,ipadx=200,ipady=50)

b1=Button(w,text="1",width=5,height=3,command=lambda : inp(1,E))
b1.grid(row=2,column=0)

b2=Button(w,text="2",width=5,height=3,command=lambda : inp(2,E))
b2.grid(row=2,column=1)

b3=Button(w,text="3",width=5,height=3,command=lambda : inp(3,E))
b3.grid(row=2,column=2,)

b4=Button(w,text="4",width=5,height=3,command=lambda : inp(4,E))
b4.grid(row=3,column=0)

b5=Button(w,text="5",width=5,height=3,command=lambda : inp(5,E))
b5.grid(row=3,column=1)

b6=Button(w,text="6",width=5,height=3,command=lambda : inp(6,E))
b6.grid(row=3,column=2)

b7=Button(w,text="7",width=5,height=3,command=lambda : inp(7,E))
b7.grid(row=4,column=0)

b8=Button(w,text="8",width=5,height=3,command=lambda : inp(8,E))
b8.grid(row=4,column=1)

b9=Button(w,text="9",width=5,height=3,command=lambda : inp(9,E))
b9.grid(row=4,column=2)

b=Button(w,text="0",width=5,height=3,command=lambda : inp(0,E))
b.grid(row=5,column=1)

b10=Button(w,text="+",width=5,height=3,command=lambda : inp("+",E),fg="blue")
b10.grid(row=3,column=3)

b11=Button(w,text="-",width=5,height=3,fg="blue",command=lambda : inp("-",E))
b11.grid(row=2,column=3)

b12=Button(w,text="x",width=5,height=3,fg="blue",command=lambda : inp("*",E))
b12.grid(row=1,column=2)

b13=Button(w,text="÷",width=5,height=3,fg="blue",command=lambda : inp("÷",E))
b13.grid(row=1,column=1)

b14=Button(w,text="clear",width=5,height=3,fg="blue",)
b14.grid(row=1,column=3)

b15=Button(w,text="=",width=5,height=3,bg="blue",fg="white",command=lambda:EV(E))#new 
b15.grid(row=5,column=3)

b16=Button(w,text="%",width=5,height=3,fg="blue",command= lambda : inp("%",E))
b16.grid(row=1,column=0)

b17=Button(w,text=".",width=5,height=3,command=lambda : inp(".",E))
b17.grid(row=5,column=2)

b18=Button(w,text="x^2",width=5,height=3,command=lambda:inp("**2",E))
b18.grid(row=5,column=0)

b19=Button(w,text="x^y",width=5,height=3,command=lambda:inp("**",E))
b19.grid(row=4,column=3)
w.mainloop()