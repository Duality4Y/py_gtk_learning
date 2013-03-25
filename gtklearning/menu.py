#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class MenuExample:
	def __init__(self):
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_size_request(200,100)
		window.set_title("GTK Menu Test")
		window.connect("delete_event", lambda w,e: gtk.main_quit())
		
		menu = gtk.Menu()
		
		for i in range(3):
			buf = "Test-undermenu - %d" % i
			menu_items = gtk.MenuItem(buf)
			menu.append(menu_items)
			menu_items.connect("activate", self.menuitem_response,buf)
			menu_items.show()
		
		root_menu = gtk.MenuItem("Root menu")
		root_menu.show()
		
		root_menu.set_submenu(menu)
		
		vbox = gtk.VBox(False, 0)
		window.add(vbox)
		vbox.show()
		
		menu_bar = gtk.MenuBar()
		vbox.pack_start(menu_bar, False, False, 2)
		menu_bar.show()
		
		button = gtk.Button("press me")
		button.connect_object("event", self.button_press, menu)
		vbox.pack_end(button, True, True, 2)
		button.show()
		
		menu_bar.append(root_menu)
		
		window.show()
		
	def button_press(self, widget, event):
		if event.type == gtk.gdk.BUTTON_PRESS:
			widget.popup(None, None, None, event.button, event.time)
			return True
		return False
	def menuitem_response(self, widget, string):
		print "%s" % string

def main():
	gtk.main()
	return 0

if __name__ == "__main__":
	MenuExample()
	main()
