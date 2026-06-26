from tkinter import *

class py:
	def __init__(self, width, height, title):
		self.window = Tk()
		self.window.geometry(f"{width}x{height}")
		self.window.title(title)

		self.window.protocol("WM_DELETE_WINDOW", self.py_off)

		self.canvas = Canvas(self.window, width=width, height=height)
		self.canvas.pack()

		self.WINDOW_HEIGHT = height
		self.WINDOW_WIDTH = width

		icon = PhotoImage(file="icona.png")
		self.window.iconphoto(True, icon)

		self.icon = icon
		self.objects = {}

	def py_background(self, background):
		self.window.configure(bg=background)
		self.canvas.configure(bg=background)
		return self
	
	def py_line(self, name, x1, y1, x2, y2, color="black"):
		obj_id = self.canvas.create_line(x1, y1, x2, y2, fill=color)
		self.objects[name] = obj_id
		return self
	
	def py_rect(self, x, y, w, h, color="black", outline="black", width=2):
		self.canvas.create_rectangle(
			x, y, x + w, y + h,
			fill=color,
			outline=outline,
			width=width
		)
		return self
	
	def py_circle(self, x, y, r, color="black"):
		self.canvas.create_oval(
			x - r, y - r,
			x + r, y + r,
			fill=color
		)
		return self
	
	def py_text(self, x, y, txt, color="black"):
		self.canvas.create_text(
			x, y,
			text=txt,
			fill=color,
			font=self.font
		)
		return self
	
	def py_entry(self, x, y, width=20, text=""):
		entry = Entry(self.window, width=width)

		if text != "":
			entry.insert(0, text)

		entry.place(x=x, y=y)

		return entry
	

	def py_triangle(self,
					x1, y1,
					x2, y2,
					x3, y3,
					color="black",
					outline="black",
					width=2):

		return self.canvas.create_polygon(
			x1, y1,
			x2, y2,
			x3, y3,
			fill=color,
			outline=outline,
			width=width
		)
	def py_update(self, name, function):
		def loop():
			function(self.canvas, self.objects[name])
			self.window.after(16, loop)

		loop()
		return self
	
	def py_set_font(self, font="Arial", size=12, bold=False):
		self.font = (font, size, "bold" if bold else "")
		return self
	
	def py_button(self, x, y, text, command=None):
		button = Button(self.window, text=text, command=command)
		button.place(x=x, y=y)
		return button
	
	def py_key(self, key, function):
		self.window.bind(f"<{key}>", function)
		return self
	
	def py_check_box(self, x, y, text="", checked=False, command=None):
		value = BooleanVar(value=checked)

		checkbox = Checkbutton(
			self.window,
			text=text,
			variable=value,
			command=command
		)

		checkbox.var = value
		checkbox.place(x=x, y=y, anchor="center")

		return checkbox

	def py_on(self):
		self.window.mainloop()
		return self

	def py_off(self):
		try:
			if self.window.winfo_exists():
				self.window.destroy()
		except:
			pass
