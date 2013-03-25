#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class BasicTreeViewExample:
	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		return False
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Basic treeview example")
		self.window.set_size_request(200,200)
		self.window.connect("delete_event", self.delete_event)
		
		self.treestore = gtk.TreeStore(str)
		for parent in range(4):
			piter = self.treestore.append(None, ['parent %i'%parent])
			for child in range(3):
				self.treestore.append(piter,['child %i of parent %i'%(child, parent)])
		self.treeview = gtk.TreeView(self.treestore)
		self.tvcolumn = gtk.TreeViewColumn('column 0')
		self.treeview.append_column(self.tvcolumn)
		self.cell = gtk.CellRendererText()
		self.tvcolumn.pack_start(self.cell, True)
		
		self.tvcolumn.add_attribute(self.cell, 'text', 0)
		self.treeview.set_search_column(0)
		self.tvcolumn.set_sort_column_id(0)
		
		self.treeview.set_reorderable(True)
		self.window.add(self.treeview)
		self.window.show_all()
def main():
	gtk.main()
	return 0

if __name__ == "__main__":
	tvexample = BasicTreeViewExample()
	main()
