from tkinter import *
import tkinter as tk
import webbrowser
from tkinter import messagebox

root=tk.Tk()
root.title("Friendship Calculator | Manjunathan C")
root.geometry("1000x500")
ico=PhotoImage(file="icon.png")
root.iconphoto(True,ico)
root.config(bg="#0278ae")

def calculate():
	result=""
	a=nameField.get()
	b=friendNameField.get()
	if (a=="" and b==""):
		messagebox.showerror("Empty","Please Fill Your Name And Your Friend's Name")
	elif a=="":
		messagebox.showerror("Empty","Please Fill Your Name")
	elif b=="":
		messagebox.showerror("Empty","Please Fill Your Friend's Name")
	else:
		b=friendNameField.get()
		c=a+b
		alphabet='bcghjklmpqrtvwxyz'
		points=0
		for character in c:
			if character in "aeiou":
				points+=3
			if character in "friends":
				points+=4	
			if character in alphabet:
				points+=2

			else:
				points+=0
		if points > 100:
			result=Label(root,text="Congratulation ! You Got more than 100 Points\nYou both Are Best Friends Ever",fg="#d2e603",bg="#0278ae",font=("Comic Sans MS",30,"bold italic"))
			result.place(x=114,y=360)
		elif (points <= 100 and points>70):
			result=Label(root,text=("your friendship score is : "+str(points)+"\nCongratulation! You both are best friends"),fg="#d2e603",bg="#0278ae",font=("Comic Sans MS",30,"bold italic"))
			result.place(x=114,y=360)
		elif(points<=70 and points>50):
			result=Label(root,text=("your friendship score is : "+str(points)+"\nCongratulation! You both are Good friends"),fg="#d2e603",bg="#0278ae",font=("Comic Sans MS",30,"bold italic"))
			result.place(x=114,y=360)
		else:
			result=Label(root,text=("your friendship score is : "+str(points)+"\nYou Need to Understand Each Others"),fg="#d2e603",bg="#0278ae",font=("Comic Sans MS",30,"bold italic"))
			result.place(x=114,y=360)

name=Label(root,text="Enter Your Name :",fg="#d2e603",bg="#0278ae",font=("Comic Sans MS",22,"bold italic"))
name.place(x=114,y=40)

nameField=Entry(root,fg="#0278ae",bg="#d2e603",font=("Comic Sans MS",20,"bold italic"),width=28,borderwidth=6)
nameField.place(x=350,y=32)

friendName=Label(root,text="Enter Your Friend's Name :",fg="#d2e603",bg="#0278ae",font=("Comic Sans MS",22,"bold italic"))
friendName.place(x=12,y=95)

friendNameField=Entry(root,fg="#0278ae",bg="#d2e603",font=("Comic Sans MS",20,"bold italic"),width=28,borderwidth=6)
friendNameField.place(x=350,y=88)

buttonClearName=Button(root,text="Clear",fg="#0278ae",bg="#d2e603",font=("Comic Sans MS",15,"bold italic"),borderwidth=6,width=6,activebackground="#d2e603",command=lambda:nameField.delete(0,END))
buttonClearName.place(x=750,y=32)

buttonClearFriendName=Button(root,text="Clear",fg="#0278ae",bg="#d2e603",font=("Comic Sans MS",15,"bold italic"),borderwidth=6,width=6,activebackground="#d2e603",command=lambda:friendNameField.delete(0,END))
buttonClearFriendName.place(x=750,y=88)

buttonCalculate=Button(root,text="Calculate",fg="#0278ae",bg="#d2e603",font=("Comic Sans MS",20,"bold italic"),borderwidth=6,width=12,activebackground="#d2e603",command=calculate)
buttonCalculate.place(x=380,y=170)

buttonExit=Button(root,text="Exit",fg="#0278ae",bg="#d2e603",font=("Comic Sans MS",20,"bold italic"),borderwidth=6,width=12,activebackground="#d2e603",command=root.destroy)
buttonExit.place(x=380,y=230)

buttonContact=Button(root,text="Contact",fg="#0278ae",bg="#d2e603",font=("Comic Sans MS",20,"bold italic"),borderwidth=6,width=12,activebackground="#d2e603",command=lambda:webbrowser.open("https://www.github.com/cmanjunathan45/"))
buttonContact.place(x=380,y=290)


root.mainloop()