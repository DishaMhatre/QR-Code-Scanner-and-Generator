# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:32:23 2020

@author: Admin
"""

import cv2
import pyqrcode
import pyzbar.pyzbar as pyzbar
from tkinter import *
def mainpage():
	root=Tk()
	root.geometry('1000x1000')
	f=Frame(root,height=1000,width=1000)
	f.propagate(0)
	f.pack()
	option=IntVar()
	font=cv2.FONT_HERSHEY_PLAIN
	def scan():
    	f1.forget()
    	global f2
    	f2=Frame(root,height=1000,width=1000)
    	f2.propagate(0)
    	f2.pack()
    	opt=option2.get()
    	i=0
    	if opt==2:
        	img=cv2.imread('man.png')
        	decoded=pyzbar.decode(img)
        	Label(f2,text='QR code scanned ').place(x=10,y=20)
        	Label(f2,text='Data :').place(x=50,y=30)
        	for obj in decoded:
            	Label(f2,text=obj.data).place(x=30,y=40+40*i)
            	i=i+1
    	else:
        	cap=cv2.VideoCapture(0)	#open camera
        	while True:
            	_,frame=cap.read()
            	decodedObjects=pyzbar.decode(frame)
            	for obj in decodedObjects:
                	cv2.putText(frame,str(obj.data),(50,50),font,3,(255,0,0),3)
                	cv2.imshow('Frame',frame)
                	key=cv2.waitKey(1)
                	if key ==27  :   #press esc to escape
                    	break
	def back():
    	f1.forget()
    	mainpage()
	def create():
    	b=data.get()
    	q=pyqrcode.create(b)
    	q.png('man.jpg',scale=6)
    	Label(f1,text='QR code generated').place(x=50,y=100)
    	img=cv2.imread('man.jpg')
    	cv2.imshow('image',img)
    	cv2.waitKey(0)
    	cv2.destroyAllWindows()
    	Button(f1,height=2,width=3,text=back,command=back).place(x=50,y=350)
	def enter():
    	f.forget()
    	global f1
    	f1=Frame(root,height=1000,width=1000)
    	f1.propagate(0)
    	f1.pack()
    	a=option.get()
    	global data
    	data=StringVar()
    	global option2
    	option2=IntVar()
    	if a==1:
        	Label(f1,text='Enter the data:').place(x=0,y=10)
        	Entry(f1,textvariable=data).place(x=60,y=10)
        	Button(f1,text='Enter',height=2,width=3,command=create).place(x=20,y=30)
      	#scan
    	elif a==2:
        	Label(f1,text='1.From Camera').place(x=10,y=10)
        	Label(f1,text='2.From Image').place(x=10,y=30)
        	Label(f1,text='Enter ur choice').place(x=20,y=100)
        	Entry(f1,width=20,textvariable=option2).place(x=60,y=100)
        	Button(f1,text='Enter',height=2,width=3,command=scan).place(x=30,y=150)
    	elif a==3:
        	root.destroy()
    	else:
        	Label(f1,text='Not a valid option').place(x=10,y=30)
	Label(f,text='*****QR CODE SCANNER AND GENERATOR*****').place(x=0,y=0)
	#while(True):
	Label(f,text='1.CREATE').place(x=50,y=50)
	Label(f,text='2.SCAN').place(x=50,y=100)
	Label(f,text='3.EXIT').place(x=50,y=150)
	Label(f,text='Enter ur choice').place(x=50,y=200)
	Entry(f,width=20,textvariable=option).place(x=50,y=250)
	Button(f,text='Enter',height=2,width=3,command=enter).place(x=60,y=350)
   	#generate
	root.mainloop()
mainpage()


