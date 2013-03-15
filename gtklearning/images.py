#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class ImagesExample:
	def close_application(self, widget, event, data=None):
		gtk.main_quit()
		return False
	def button_clicked(self, widget, data=None):
		print "button %s clicked" % data
	def __init__(self):
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.connect("delete_event", self.close_application)
		window.set_border_width(10)
		window.show()
		
		hbox = gtk.HBox()
		hbox.show()
		window.add(hbox)
		
		pixbufanim = gtk.gdk.PixbufAnimation("goalie.gif")
		image = gtk.Image()
		image.set_from_animation(pixbufanim)
		image.show()
		
		button = gtk.Button()
		button.add(image)
		button.show()
		hbox.pack_start(button)
		button.connect("clicked", self.button_clicked, "1")
		
		image = gtk.Image()
		image.set_from_file("apple-red.png")
		image.show()
		
		button = gtk.Button()
		button.add(image)
		button.show()
		hbox.pack_start(button)
		button.connect("clicked", self.button_clicked, "2")
		
		image = gtk.Image()
		image.set_from_file("chaos.jpg")
		image.show()
		
		button = gtk.Button()
		button.add(image)
		button.show()
		hbox.pack_start(button)
		button.connect("clicked", self.button_clicked, "3")
		
		image = gtk.Image()
		image.set_from_file("important.tif")
		image.show()
		
		button = gtk.Button()
		button.add(image)
		button.show()
		hbox.pack_start(button)
		button.connect("clicked", self.button_clicked, "4")
		
		image = gtk.Image()
		image.set_from_file("soccerball.gif")
		image.show()
		
		button = gtk.Button()
		button.add(image)
		button.show()
		hbox.pack_start(button)
		button.connect("clicked", self.button_clicked, "5")
def main():
	print "gtk main>> ",gtk.main()
	return 0

if __name__ == "__main__":
	ImagesExample()
	main()
