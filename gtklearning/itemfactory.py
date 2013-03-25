#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class ItemFactoryExample:
	def print_hello(self, w, data):
		print "hello, world!"
	def get_main_menu(self, window):
		accel_group = gtk.AccelGroup()
		item_factory = gtk.ItemFactory(gtk.MenuBar, "<main>", accel_group)
		item_factory.create_items(self.menu_items)
		window.add_accel_group(accel_group)
		self.item_factory = item_factory
		return item_factory.get_widget("<main>")
	def __init__(self):
		self.menu_items = (
			( "/_File",         None,         None, 0, "<Branch>" ),
			( "/File/_New",     "<control>N", self.print_hello, 0, None ),
			( "/File/_Open",    "<control>O", self.print_hello, 0, None ),
			( "/File/_Save",    "<control>S", self.print_hello, 0, None ),
			( "/File/Save _As", None,         None, 0, None ),
			( "/File/sep1",     None,         None, 0, "<Separator>" ),
			( "/File/Quit",     "<control>Q", gtk.main_quit, 0, None ),
			( "/_Options",      None,         None, 0, "<Branch>" ),
			( "/Options/Test",  None,         None, 0, None ),
			( "/_Help",         None,         None, 0, "<LastBranch>" ),
			( "/_Help/About",   None,         None, 0, None ),
			)
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.connect("destroy", lambda w: gtk.main_quit(), "WM destroy")
		window.set_title("Item Factory")
		window.set_size_request(300,200)
		
		main_vbox = gtk.VBox(False, 1)
		main_vbox.set_border_width(1)
		window.add(main_vbox)
		main_vbox.show()
		
		menubar = self.get_main_menu(window)
		main_vbox.pack_start(menubar, False, True, 0)
		
		menubar.show()
		window.show()

def main():
	gtk.main()
	return 0

if __name__ == "__main__":
	ItemFactoryExample()
	main()
