#!/usr/bin/env python
# encoding: utf-8

import objc
from Foundation import *
from AppKit import *
import sys, os, re

import time, traceback

MainBundle = NSBundle.mainBundle()
path = MainBundle.bundlePath() + "/Contents/Scripts"
if not path in sys.path:
	sys.path.append( path )

import GlyphsApp
from toucheTool import ToucheTool

GlyphsPluginProtocol = objc.protocolNamed( "GlyphsPlugin" )

class TouchePlugin ( NSObject, GlyphsPluginProtocol ):
	
	def init( self ):
		"""
		You can add an observer like in the example.
		Do all initializing here.
		"""
		try:
			pass
		except Exception as e:
			self.logToConsole( "init: %s" % str(e) )
		return self
	
	def __del__( self ):
		"""
		Clean up
		"""
		pass
	
	def loadPlugin(self):
		mainMenu = NSApplication.sharedApplication().mainMenu()
		s = objc.selector(self.showWindow, signature='v@:')
		newMenuItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(self.title(), s, "" )
		newMenuItem.setTarget_(self)
		
		mainMenu.itemAtIndex_(2).submenu().addItem_(newMenuItem)
	
	def title(self):
		return "Touche"
	
	def interfaceVersion(self):
		return 1
	
	def showWindow(self):
		self.touche = ToucheTool()
	
	def logToConsole( self, message ):
		"""
		The variable 'message' will be passed to Console.app.
		Use self.logToConsole( "bla bla" ) for debugging.
		"""
		myLog = "%s:\n%s" % ( self.__class__.__name__, message )
		NSLog( myLog )
	