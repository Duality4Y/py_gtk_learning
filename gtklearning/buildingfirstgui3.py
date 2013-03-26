import pygtk
pygtk.require('2.0')
import gtk

class MyWindow(object):
	def __init__(self):
		window = gtk.Window()
		window.connect("destroy", self.quit_gui)
		window.set_title("My Window")
		
		#create the main Vertical Stack box that holds every other box.
		mainVbox = gtk.VBox(False, 0)
		window.add(mainVbox)
		mainVbox.show()
		
		#create the main Menu box which will hold menu widgets and clicky buttons.
		mainMenuBox = gtk.VBox(False, 0)
		mainVbox.add(mainMenuBox)
		mainMenuBox.show()
		
		#create the middle box which holds the tabs and text view. (basicly the text editor part)
		textBox = gtk.VBox(False, 0)
		mainVbox.add(textBox)
		textBox.show()
		
		#create the bottom box which holds the terminal output, and progress bar.
		loggerBox = gtk.VBox(False, 0)
		mainVbox.pack_end(loggerBox,False,False,0)
		loggerBox.show()
		
		#split the main menu box in to two
		upperMenuBox = gtk.VBox(False, 0)
		lowerMenuBox = gtk.HBox(False, 0)
		mainMenuBox.pack_start(upperMenuBox, False, False, 0)
		mainMenuBox.pack_start(lowerMenuBox, False, False, 0)
		upperMenuBox.show()
		lowerMenuBox.show()
		
		#little test menu for upperMenuBox
		menubar = gtk.MenuBar()
		menuitem = gtk.MenuItem("item")
		menubar.append(menuitem)
		
		menu = gtk.Menu()
		menuitem.set_submenu(menu)
		
		submenuitem = gtk.MenuItem("sub")
		menu.append(submenuitem)
		
		upperMenuBox.add(menubar)
		
		#add buttons to the lowerMenuBox
		for i in range(6):
			if i == 5:
				button = gtk.Button("6")
				lowerMenuBox.pack_end(button, False, False, 0)
			else:
				button = gtk.Button("%i" % (i))
				lowerMenuBox.pack_start(button, False, False, 0)
			button.set_size_request(30,30)
			button.show()
		
		thisDict = {"File":["New","Open","Save","Close","Quit"],
					"Edit":["Undo","Redo","Cut","Copy","Paste"],}
		#upperMenuBox.add(self.create_menu(thisDict))
		
		window.show_all()
	def create_menu(self, box, menuItems):
		print "dict: >> %s" % menuItems
		menubar = gtk.MenuBar()
		for MenuItem in menuItems:
			for subMenuItem in menuItems[MenuItem]:
				print "MenuItem: %s | subMenuItem: %s" % (MenuItem, subMenuItem)
		return menubar
		
	def quit_gui(self, widget):
		gtk.main_quit()
	def run_gui(self):
		gtk.main()

if __name__ == "__main__":
	app = MyWindow()
	app.run_gui()
