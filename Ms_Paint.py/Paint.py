from tkinter import *
from tkinter import ttk, colorchooser, filedialog
import PIL
from PIL import ImageGrab


class main:
# Definição dos parâmetros iniciais
# Tais como: cor inicial da tela e do pincel
# E captura do botão esquerdo do mouse

    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.drawWidgets()
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)

# Definição de como vai ser o ponteiro do pincel
# Note que, existe o parametro 'smooth', ele faz com que não haja tanto ruido no desenho e o traço seja mais suave
    def paint(self,e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)

        self.old_x = e.x
        self.old_y = e.y

    def reset(self,e):
        self.old_x = None
        self.old_y = None

    def changeW(self,e):
        self.penwidth = e

# Definição do formato que será exportado
# Optei pelo formato JPEG por uma maior qualidade

    def save(self):
        file = filedialog.asksaveasfilename(filetypes=[('Joint Photographics Experts Group','*.jpg')])
        if file:
            x = self.master.winfo_rootx() + self.c.winfo_x()
            y = self.master.winfo_rooty() + self.c.winfo_y()
            x1 = x + self.c.winfo_width()
            y1 = y + self.c.winfo_height()

            PIL.ImageGrab.grab().crop((x,y,x1,y1)).save(file + '.png')



    def clear(self):
        self.c.delete(ALL)

    def change_fg(self):
        self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]

    def change_bg(self):
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg

# Definições de opções do pincel e como ele se portará

    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 5,pady = 5)
        Label(self.controls, text='Ponta do Pincel :',font=('',15)).grid(row=0,column=0)
        self.slider = ttk.Scale(self.controls,from_= 5, to = 100, command=self.changeW,orient=HORIZONTAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0,column=1,ipadx=30)
        self.controls.pack()

        self.c = Canvas(self.master,width=500,height=400,bg=self.color_bg,)
        self.c.pack(fill=BOTH,expand=True)

# Definições de opções e criação de uma pequena Toolbar
# E um menu interativo

        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='Arquivo',menu=filemenu)
        filemenu.add_command(label='Exportar',command=self.save)
        colormenu = Menu(menu)
        menu.add_cascade(label='Cores',menu=colormenu)
        colormenu.add_command(label='Cor do Pincel',command=self.change_fg)
        colormenu.add_command(label='Cor do Fundo',command=self.change_bg)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Opções',menu=optionmenu)
        optionmenu.add_command(label='Limpar Tela',command=self.clear)
        optionmenu.add_command(label='Sair',command=self.master.destroy)

if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Paint.py')
    root.mainloop()
