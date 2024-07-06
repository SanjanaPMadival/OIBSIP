from tkinter import *
from tkinter import messagebox

import customtkinter
from customtkinter import *
app=Tk()
app.title("BMI Calculator")
app.configure(bg="black")
app.geometry("475x650")

img=PhotoImage(file="C:/Users/User/OneDrive/Desktop/Images/meter2.png")
l1=Label(app,image=img)
l1.place(x=10.5,y=20)

font1=('Arial',18,'bold')
font2=('Arial',25,'bold')
font3=('Arial',30,'bold')


def calculate_BMI():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        if variable2.get() == 'ft':
            height *= 30.48
        if variable1.get() == 'ibs':
            weight *= 0.453592

        if height == 0:
            raise ValueError("Height cannot be 0!")
        if weight == 0:
            raise ValueError("Weight cannot be 0!")

        bmi = weight / ((height / 100) ** 2)
        result_label.configure(text='Your BMI is: {:.1f}'.format(bmi))
    except ValueError as e:
        if "Height cannot be 0!" in str(e):
            messagebox.showerror('Error', 'Height cannot be 0!')
        elif "Weight cannot be 0!" in str(e):
            messagebox.showerror('Error', 'Weight cannot be 0!')

        else:
            messagebox.showerror('Error', 'Enter a valid number!')


#weight label with entry box
l2=Label(app,text="WEIGHT",font=font2,bg="black",fg="white")
l2.place(x=23,y=150)
weight_entry=customtkinter.CTkEntry(app,font=font2,text_color='#000',fg_color='#fff',border_color="#fff",justify=CENTER)
weight_entry.place(x=26,y=200)

#height label with entry box
l2=Label(app,text="HEIGHT",font=font2,bg="black",fg="white")
l2.place(x=23,y=300)
height_entry=customtkinter.CTkEntry(app,font=font2,text_color='#000',fg_color='#fff',border_color="#fff",justify=CENTER)
height_entry.place(x=26,y=350)

#another entry box for weight and height options
weight_options = ['kg', 'ibs']
height_options = ['cm', 'ft']
variable1 = StringVar()
variable2 = StringVar()

weight_option=customtkinter.CTkComboBox(app,font=font2,text_color='#000',fg_color='#fff',dropdown_hover_color='#06911f',values=weight_options,variable=variable1,width=88)
weight_option.place(x=300,y=200)
weight_option.set('kg')

height_option=customtkinter.CTkComboBox(app,font=font2,text_color='#000',fg_color='#fff',dropdown_hover_color='#06911f',values=height_options,variable=variable2,width=88)
height_option.place(x=300,y=350)
height_option.set('cm')

#calculate button
calculate_button=customtkinter.CTkButton(app,command=calculate_BMI,font=font2,text_color='#fff',text='Calculate BMI',fg_color='#06911f',hover_color='#06911f',cursor='hand2',corner_radius=5,width=300)
calculate_button.place(x=85,y=475)

result_label=customtkinter.CTkLabel(app,text='',font=font3,text_color='#fff',bg_color='#000')
result_label.place(x=115,y=550)


app.mainloop()
