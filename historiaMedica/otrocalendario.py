import tkinter as tk
from tkcalendar import DateEntry

def obtener_fecha():
	fecha_seleccionada = cal.get_date()
	texto =f"Fecha seleccionada: {fecha_seleccionada}"
	label_fecha.config(text=texto)

ventana = tk.Tk()
ventana.geometry("300x200")

cal = DateEntry(ventana, width=12, locale ='es_US',background='darkblue', foreground='white',borderwidth=2)

cal.pack(padx=10,pady=10)

btn = tk.Button(ventana, text="obtener fecha", command=obtener_fecha)
btn.pack(padx=10,pady=10)

label_fecha = tk.Label(ventana, text="")
label_fecha.pack(padx=10,pady=10)

ventana.mainloop()
