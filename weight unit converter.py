# imports the Tkinter library
from tkinter import *

# Create the main window of the GUI application.
root  = Tk()
#This line sets the title of the main window.
root.title("Weight Unit converter")
#This line sets the geometry of the main window, which is its size and position on the screen.
root.geometry("500x300")

#This line creates a DoubleVar object, which is a variable that can store floating-point numbers.
weight_value = DoubleVar()
#This line creates a StringVar object, which is a variable that can store strings.
weight_unit = StringVar()
#creates the first label
first_label= Label(root, text= "enter the weight", fg="blue")
first_label.grid(row=0, column=0, padx=5, pady=10)
#creates the second label
second_label= Label(root, text= "enter the unit l for (lbs) k for (kilo) ", fg="blue")
second_label.grid(row=1, column=0, padx=5, pady=10)

# function to convert weight unit 
def get_weight_value():
# kilogram = 2.2 pound
    if weight_unit.get()=="L" or weight_unit.get()=="l" :
        kilogram = weight_value.get()/2.2
        emptylabel.config(text="weight in kilogram is " + str(    round(kilogram, 2) ))

    elif weight_unit.get()=="K" or weight_unit.get()=="k" :
        pound = weight_value.get()*2.2

        emptylabel.config(text="weight in pund is " + str(    round(pound, 2) ))

    

#widgets to allow the user to enter their weight
first_entry = Entry(root, textvariable = weight_value )
first_entry.grid(row=0,column=1)
#widgets to allow the user to enter their unit
second_entry = Entry(root, textvariable = weight_unit)
second_entry.grid(row=1,column=1)

emptylabel=Label(root,fg='green', font=('Arial',14))
emptylabel.grid(row=3,column=1)

#When the button is clicked, the get_weight_value() function will be called.
convert_button = Button(root , text="convert" , command=get_weight_value)
convert_button.grid(row=2,column=1)

root.mainloop()
