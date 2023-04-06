from tkinter import*
from math import*
def click(event):
    root.title('Рівняння')
    a=float(zm_1.get())
    b=float(zm_2.get())
    c=float(zm_3.get())
    z_1=(-b+sqrt(b*b-4*a*c))/(2*a)
    z_2=(-b-sqrt(b*b-4*a*c))/(2*a)
    n_r_1=Label(text='x1 = '+str(z_1))
    n_r_2=Label(text='x2 = '+str(z_2))
    n_r_1.pack(pady=0)
    n_r_2.pack(pady=0) 
root =Tk()
root.title('Назва вікна')
root.geometry('600x800+200+300')
root['bg']='yellow'
napuc=Label(text='Для рішення квадратного рівння введіть коефіцієнти:')
napuc['font']=101
napuc['fg']='red'
napuc['bg']='black'
napuc.pack(pady=20)
n_a=Label(text='a =')
n_a.pack(pady=0)
zm_1=Entry(width=10)
zm_1.pack(pady=20)
n_b=Label(text='b =')
n_b.pack(pady=0)
zm_2=Entry(width=10)
zm_2.pack(pady=20)
n_c=Label(text='c =')
n_c.pack(pady=0)
zm_3=Entry(width=10)
zm_3.pack(pady=20)
button=Button(text='Розрахувати', width=30)
button.pack(pady=20)
button.bind('<1>',click)
