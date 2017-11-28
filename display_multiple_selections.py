import sublime
import sublime_plugin
import os
import json
import threading
import copy
import logging
import traceback
import sys

class DisplayMultipleSelections(sublime_plugin.WindowCommand):
  def run(self, edit):
    self.generate_output_quick_panel()

  def generate_text(self, edit):
      content = ''
      # add content here..
      return content

  def generate_output_quick_panel(self, edit):
      self.window.show_quick_panel("Hello, World!")

  def quick_panel_callback(self, index):
      if index == -1:
          return