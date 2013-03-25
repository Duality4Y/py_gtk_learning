from gi.repository import Gtk

class GridWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Grid example")
		
		grid = Gtk.Grid()
		self.add(grid)
		
		button1 = Gtk.Button(label="button1")
		button2 = Gtk.Button(label="button2")
		button3 = Gtk.Button(label="button3")
		button4 = Gtk.Button(label="button4")
		button5 = Gtk.Button(label="button5")
		button6 = Gtk.Button(label="button6")
		
		grid.add(button1)
		grid.attach(button2, 1,0 ,2,1)
		grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM,1,2)
		grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
		grid.attach(button5, 1, 2, 1, 1)
		grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1 ,1)
win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
