from Tkinter import *

from PIL import ImageTk,Image  

root = Tk()

root.title("Image Viewer App")

# make sure the location of your image files is in the same folder with this python file

my_img1 = Image.open("images/Awoyelu.jpeg")
my_img1 = my_img1.resize((300,300), Image.ANTIALIAS)
my_img1 = ImageTk.PhotoImage(my_img1)


my_img2 = Image.open("images/Oladimeji.jpeg")
my_img2 = my_img2.resize((300,300), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(my_img2)

my_img3 = Image.open("images/Smile.jpeg")
my_img3 = my_img3.resize((300,300), Image.ANTIALIAS)
my_img3 = ImageTk.PhotoImage(my_img3)


my_img4 = Image.open("images/Tommy.jpeg")
my_img4 = my_img4.resize((300,300), Image.ANTIALIAS)
my_img4 = ImageTk.PhotoImage(my_img4)


image_list = [my_img1, my_img2, my_img3, my_img4] 


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
	global my_label
	global button_forward
	global button_back

	# To get rid of the old image
	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda:forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda:back(image_number-1))
	
	if image_number == 4:
		button_forward = Button(root, text=">>", state=DISABLED)


	my_label.grid(row=0, column=0, columnspan=3)

	button_back.grid(row=1, column=0)	
	button_forward.grid(row=1, column=2) 

	

def back(image_number):
	global my_label
	global button_forward
	global button_back
	

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda:forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda:back(image_number-1))

	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)
 
	
	my_label.grid(row=0, column=0, columnspan=3)

	button_back.grid(row=1, column=0)	
	button_forward.grid(row=1, column=2) 



button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command= root.quit)
button_forward = Button(root, text=">>", command=lambda:forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()

