#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import operator
import time
import string

class DrawingAreaExample:
	def __init__(self):
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("Drawing area example")
		window.connect("destroy", lambda w: gtk.main_quit())
		self.area = gtk.DrawingArea()
		self.area.set_size_request(400, 300)
		self.pangolayout = self.area.create_pango_layout("")
		self.sw = gtk.ScrolledWindow()
		self.sw.add_with_viewport(self.area)
		self.tabel = gtk.Table(2,2)
		self.hruler = gtk.HRuler()
		self.vruler = gtk.VRuler()
		self.hruler_set_range(0,400,0,400)
		self.vruler.set_range(0,300,0,300)
		self.table.attach(self.hruler, 1, 2, 0, 1, yoptions=0)
		self.table.attach(self.vruler, 0,1,1,2, xoptions=0)
		self.table.attach(self.sw, 1, 2, 1, 2)
		window.add(self.table)
		self.area.set_events(gtk.gdk.POINTER_MOTION_MASK|gtk.gdk.POINTER_MOTION_HINT_MASK)
		self.area.connect("expose-event", self.area_expose_cb)
		def motion_notify(ruler, event):
			return ruler.emit("motion_notify_event", event)
		self.area.connect_object("motion_notify_event", motion_notify, self.hruler)
		self.area.connect_object("motion_notify_event", motion_notify, self.vruler)
		self.hadj = self.sw.get_hadjustment()
		self.vadj = self.sw.get_vadjustment()
		def val_cb(adj, ruler, horiz):
			if horiz:
				span = self.sw.get_allocation()[3]
			else:
				span = self.sw.get_allocation()[2]
			l,u,p,m = ruler.get_range()
			v = adj.value
			ruler.set_range(v, v+span, p, m)
			while gtk.events_pending():
				gtk.main_iteration()
		self.hadj.connect("value-changed", val_cb, self.hruler, True)
		self.vadj.connect("value-changed", val_cb, self.vruler, False)
		def size_allocate_cb(wid, allocation):
			x, y, w, h = allocation
			l,u,p,m = self.hruler.get_range()
			m = max(m, w)
			self.hruler.set_range(l, l+w, p, m)
			l,u,p,m = self.vruler.get_range()
			m = max(m, h)
			self.vruler.set_range(l,l+h, p, m)
		self.sw.connect("size-allocate", size_allocate_cb)
		self.area.show()
		self.hruler.show()
		self.vruler.show()
		self.sw.show()
		self.table.show()
		window.show()
	def area_expose_cb(self, area, event):
		self.style = self.area.get_style()
		self.gc = self.style.fg_gc[gtk.STATE_NORMAL]
		self.draw_point(10,10)
		self.draw_points(110,10)
		self.draw_line(210, 10)
		self.draw_lines(310, 10)
		self.draw_segments(10, 100)
		self.draw_rectagles(110, 100)
		self.draw_arcs(210, 100)
		self.draw_pixmap(310, 100)
		self.draw_polygon(10, 200)
		self.draw_rgb_image(110,200)
		return True
	def draw_point(self, x, y):
		self.area.window.draw_point(self.gc, x+30, y+30)
		self.pangolayout.set_text("Point")
		self.area.window.draw_layout(self.gc, x+5, y+50, self.pangolayout)
		return
	def draw_points(self, x, y):
		points = [(x+10,y+10),(x+40,y+30),
					(x+30,y+10),(x+50, y+10)]
		self.area.window.draw_points(self.gc, points)
		self.pangolayout.set_text("Points")
		self.area.window.draw_layout(self.gc, x+5, y+50, self.pangolayout)
		return
	def draw_line(self, x, y):
		self.area.window.draw_line(self.gc, x+10, y+10, x+20, y+30)
		self.pangolayout.set_text("Line")
		self.area.window.draw_layout(self.gc, x+5 y+50, self.pangolayout)
		return 
	def draw_lines(self, x, y):
		points = 
