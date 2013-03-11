#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import sys, string

def make_box(homogeneous, spacing, expand, fill, padding):
	box = gtk.HBox(homogeneous, spacing)
	button = gtk.Button("box.pack")
	box.pack_start(button, expand, fill, padding)
	button.show()
	button = gtk.Button("(buton,")
	box.pack_start(button, expand, fill, padding)
	button.show()
	if expand == True:
		button = gtk.Button("True,")
	else:
		button = gtk.Button("False,")
	box.pack_start(button,expand,fill,padding)
	button.show()
	button = gtk.Button(("False,","True")[fill==True])
	box.pack_start(button, expand, fill, padding)
	button.show()
	
	padstr = "%d)" % padding
	
	button = gtk.Button(padstr)
	box.pack_start(button, expand, fill, padding)
	button.show()
	return box

class PackBox1:
	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		return False
	def __init__(self, which):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("delete_event",self.delete_event)
		box1 = gtk.VBox(False, 0)
		if which == 1:
			label = gtk.Label("HBox(False, 0)")
			label.set_alignment(0,0)
			box1.pack_start(label, False, False, 0)
			label.show()
			
			box2 = make_box(False, 0, False, False, 0)
			box1.pack_start(box2, False, False, 0)
			box2.show()
			
			box2 = make_box(False,0,True, False, 0)
			box1.pack_start(box2, False,False, 0)
			box2.show()
			
			box2 = make_box(False, 0 , True, True, 0)
			box1.pack_start(box2, False, False, 0)
			box2.show()
			
			separator = gtk.HSeparator()
			
			box1.pack_start(separator, False, True, 5)
			separator.show()
			
			label = gtk.Label("HBox(True, 0)")
			label.set_alignment(0,0)
			box1.pack_start(label,False,False,0)
			label.show()
			box2 = make_box(True, 0, True, False, 0)
			box1.pack_start(box2,False, False, 0)
			box2.show()
			
			box2 = make_box(True, 0, True, True, 0)
			box1.pack_start(box2, False, False, 0)
			box2.show()
			
			separator = gtk.HSeparator()
			box1.pack_start(separator, False, True, 5)
			separator.show()
		elif which == 2:
			label = gtk.Label("HBox(False, 10)")
			label.set_alignment(0,0)
			box1.pack_start(label, False, False, 0)
			label.show()
			
			box2 = make_box(False, 10, True, False, 0)
			box1.pack_start(box2, False, False, 0)
			box2.show()
			
			box2 = make_box(False, 10, True, True, 0)
			box1.pack_start(box2, False, False, 0)
			box2.show()
			
			separator = gtk.HSeparator()
			box1.pack_start(separator, False, True, 5)
			separator.show()
			
			label = gtk.Label("HBox(False, 0)")
			label.set_alignment(0,0)
			box1.pack_start(label, False, False, 0)
			label.show()
			
			box2 = make_box(False, 0, True, False, 10)
			box1.pack_start(box2, False, False, 0)
			box2.show()
			
			separator = gtk.HSeparator()
			box1.pack_start(separator, False, True, 5)
			separator.show()
		elif which == 3:
			box2 = make_box(False, 0, False, False, 0)
			label = gtk.Label("end")
			box2.pack_end(label, False, False, 0)
			label.show()
			
			box1.pack_start(box2, False, False, 0)
			box2.show()
			
			separator = gtk.HSeparator()
			separator.set_size_request(400,5)
			box1.pack_start(separator, False, True, 5)
			separator.show()
			
		quitbox = gtk.HBox(False,0)
		button = gtk.Button("Quit")
		button.connect("clicked", lambda w: gtk.main_quit())
		quitbox.pack_start(button, True, False, 0)
		box1.pack_start(quitbox, False, False, 0)
		self.window.add(box1)
		button.show()
		quitbox.show()
		box1.show()
		self.window.show()
def main():
	gtk.main()
	return 0
if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.stderr.write("usage: packbox.py num, where num is 1, 2, or 3.\n")
		sys.exit(1)
	PackBox1(string.atoi(sys.argv[1]))
	main()
			
	
