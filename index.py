from tkinter import *

root = Tk()

root.title("Bem Vindo Ao GeekForGeeks! ")
root.geometry('350x200')

menu = Menu(root)
item = Menu(menu)
item.add_command(label='Novo')
menu.add_cascade(label='Arquivo', menu=item)
root.config(menu=menu)


lbl = Label(root, text="Você é  Geek ? ")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column=1, row=0)


def clicked():
    res = "Sua Resposta foi: "
    txt.get()
    lbl.configure(text=res)


btn = Button(root, text="Clique Aqui", fg="green", command=clicked)
btn.grid(column=2, row=0)

root.mainloop()
