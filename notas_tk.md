# NOTAS DE USO PARA TKINTER
## Elementos fundamemtales
1. import tkinter as tk y crear una ventana
2. ejecutar al final mainloop sobre la ventana
3. para que los widgets se muestre se les debe pasar un argumento master y ejecutar su metodo pack(),place() o grid.
## acciones
1. definir propiedades:
	- Desde la ejecucion de la clase: widget(args)
	- Desde el metodo .config = instancia.config(args)
	- Mapeando: instancia["arg"] = valor
2. posicionamiento de elementos:
	- por defecto, los elementos se posicionan en forma de columna dentro de la ventana
	- pack:
		+ se le pueden pasar los argumentos side cuyos valores por defecto son tk.TOP, .BOTTOM, .LEFT y .RIGHT al metodo pack para indicar donde quieres poner el elementos
		+ se le puede pasar el metodo before o after a pack y de argumento un elemento para indicar que el elemento posicionado debe de estar antes o despues del pasado como argumento
		+ padx y pady para los margenes
		+ ipadx e ipady para los padding
		+ expand = bool y fill = tk.X o tk.Y o tk.BOTH para indicar a donde quieres que se expanda
	- metodo grid de cualquier elemento: 
		+ recibe grow y column que son enteros que representan indexes en una matriz de posicion relativa del contenedor 
		+ usa rowspam o columnspan para inndicar cuantas columnas o filas quieres que ocupe
		+ sticky; recibe "nsew" o separados o en pares para indicar como quieres que se expanda el control en relacion al tamaño de la celda que lo contiene
	- rowconfigure o columnconfigure: reciben un indice de fila o columna y una proporcion de expansion en relacion el contenedor grilla (width)
	- Absoluta : widget.place(x,y,width,height)
	- Relativa (porcentajes del 0 al 1) : widget.place(relx,rely,relwidth,relheight)
3. Para dimensionar la ventana usa su metodo ventana.geometry("WIDTHxHEIGHT")
4. eventos
	- a los botones se les asigna eventos on_click con el argumento command
	- metodo texto.get() para extraer el valor de un campo de texto
	- metodo Entry.insert(index,string) para concatenar un valor a el valor actual de un campo
	- metodo Entry.delete(inicio, fin) para borrar e texto dentro de un campo desde un punto a otro (los argumentos pueden ser textos como 'end' para fin )
5. widgets
	- boton: Button
	- Campo de texto: Entry 
	- Texto cualquiera: Label
	- contenedor: Frame
6. estiizado
	- bg y fg : color de fondo y del texto para cualquier widget
	- Frame.config / argumentos :
		+	cursor : estio de cursor
		+ relief : estilo del borde
		+ bd : grosor del borde
		+ width y height
