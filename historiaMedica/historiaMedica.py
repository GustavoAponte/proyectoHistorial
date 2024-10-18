import tkinter  as tk
from paciente.gui import Frame

def main():
    root = tk.Tk()
    root.title('HISTORIA MEDICA')
    root.resizable(0,0) #Instruct the window manager whether this width 
                        #can be resized in WIDTH or HEIGHT. Both values are boolean values
                        #en este caso 0,0 no permite cambiar
    app = Frame(root)
    app.mainloop()

if __name__ == '__main__':
    main()
