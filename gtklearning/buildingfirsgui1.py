import pygtk
pygtk.require('2.0')
import gtk

class MyWindow(object):
	def __init__(self):
		window = gtk.Window()
		window.connect("destroy", self.quit_gui)
		window.set_title("My Window")
		
		mainVbox = gtk.VBox(False, 0)
		window.add(mainVbox)
		mainVbox.show()
		
		mainMenuBox = gtk.VBox(False, 0)
		mainVbox.add(mainMenuBox)
		mainMenuBox.show()
		
		textBox = gtk.VBox(False, 0)
		mainVbox.add(textBox)
		textBox.show()
		
		loggerBox = gtk.VBox(False, 0)
		mainVbox.add(loggerBox)
		loggerBox.show()
		
		#split the main menu box in to two
		upperMenuBox = gtk.VBox(False, 0)
		lowerMenuBox = gtk.HBox(False, 0)
		mainMenuBox.add(upperMenuBox)
		mainMenuBox.add(lowerMenuBox)
		upperMenuBox.show()
		lowerMenuBox.show()
		
		#create a menu add it to the upperMenu box
		#create the menu bar that holds every thing
		menubar = gtk.MenuBar()
		#create a menu in the menu bar
		menu_file = gtk.Menu()
		#create a item that wil bee hold by the menu
		item_open = gtk.MenuItem("Open")
		#add the item to the menu
		menu_file.append(item_open)
		#create and item for the menu.
		item_file = gtk.MenuItem("File")
		#add the item to the menubar
		item_file.set_submenu(menu_file)
		#add the actual menu, to the menu bar
		menubar.append(item_file)
		
		upperMenuBox.add(menubar)
		
		#add buttons to the lowerMenuBox
		for i in range(6):
			if i == 5:
				button = gtk.Button("button 6")
				lowerMenuBox.pack_end(button, False, False, 0)
			else:
				button = gtk.Button("button %i" % (i))
				lowerMenuBox.pack_start(button, False, False, 0)
				button.show()
		
		window.show_all()
		
		
	def quit_gui(self, widget):
		gtk.main_quit()
	def run_gui(self):
		gtk.main()

if __name__ == "__main__":
	app = MyWindow()
	app.run_gui()
