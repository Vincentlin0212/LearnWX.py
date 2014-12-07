#! /usr/bin/env python

import wx
import time
import random

class TenButtonFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Ten Button Race")
		
		self.panel = wx.Panel(self)
		labels = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
		self.buttons = []
		for i in range (10):
			x=random.randint(0,50)
			y=random.randint(0,350)
			self.buttons.append(wx.Button(self.panel, label=labels[i], pos=(x,y),size=(100,20)))
			self.buttons[i].Bind(wx.EVT_BUTTON, self.OnClick)
			self.buttons[i].Show(False)
		#Bind all the buttons to their event handlers
		
		
		self.btnStart = wx.Button(self.panel, label="start", pos=(150,200))
		self.btnStart.Bind(wx.EVT_BUTTON, self.OnClickStart)
	
	
	def OnClickStart(self, e):
		self.btnStart.Show(False)
		self.buttons[0].Show(True)
		self.start_time=time.time()
		
	# Event handler for the start button
	def OnClick(self, e):
		clickedButton = e.GetEventObject()
		clickedIndex = self.buttons.index(clickedButton)
		self.buttons[clickedIndex].Show(False)
		if clickedIndex <= 8:
			self.buttons[clickedIndex + 1].Show(True)
		elif clickedIndex == 9:
			print(str(time.time()-self.start_time)+"s")
		
	#Other event handlers here
	
	#Remember the last event handler needs to print the final time.
	
	
# -------- Main Program Below ------------

app = wx.App(False)
frame = TenButtonFrame(None)
frame.Show()
app.MainLoop()
