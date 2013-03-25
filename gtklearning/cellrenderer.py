#!/usr/bin/env python

import pygtk
pygtk.require("2.0")
import gtk, gobject


tasks =  {
	"Buy groceries": "Go to Asda after work",
	"Do some programming": "Remember to update your software",
	"Power up systems": "Turn on the client but leave the server",
	"Watch some tv": "Remember to catch ER"
	}

class GUI_Controller:
	def __init__(self):
		self.root = gtk.Window(type = gtk.WINDOW_TOPLEVEL)
		self.root.set_title("Cellrendere Example")
		self.root.connect("destroy", self.destroy_cb)
		
		self.mdl = Store.get_model()
		self.view = Display.make_view(self.mdl)
		
		self.root.add(self.view)
		self.root.show_all()
		return
	def destroy_cb(self, *kw):
		gtk.main_quit()
		return
	def run(self):
		gtk.main()
		return
class InfoModel:
	def __init__(self):
		self.tree_store = gtk.TreeStore(gobject.TYPE_STRING, gobject.TYPE_BOOLEAN)
		for item in tasks.keys():
			parent = self.tree_store.append(None, (item, None))
			self.tree_store.append(parent, (tasks[item], None))
		return
	def get_model(self):
		if self.tree_store:
			return self.tree_store
		else:
			return None
class DisplayModel:
	def make_view(self, model):
		self.view = gtk.TreeView(model)
		
		self.renderer = gtk.CellRendererText()
		self.renderer.set_property('editable', True)
		self.renderer.connect('edited', self.col0_edited_cb, model)
		
		self.renderer1 = gtk.CellRendererToggle()
		self.renderer1.set_property('activatable', True)
		self.renderer1.connect('toggled', self.col1_toggled_cb, model)
		
		self.column0 = gtk.TreeViewColumn("Name", self.renderer, text=0)
		
		self.column1 = gtk.TreeViewColumn("Complete", self.renderer1)
		self.column1.add_attribute(self.renderer1, "active", 1)
		self.view.append_column(self.column0)
		self.view.append_column(self.column1)
		return self.view
	def col0_edited_cb(self, cell, path, new_text, model):
		print "change '%s' to '%s'"%(model[path][0], new_text)
		model[path][0] = new_text
		return
	def col1_toggled_cb(self, cell, path, model):
		model[path][1] = not model[path][1]
		print "toggle '%s' to: %s"%(model[path][0], model[path][1],)
		return

if __name__ == '__main__':
	Store = InfoModel()
	Display = DisplayModel()
	myGUI = GUI_Controller()
	myGUI.run()
