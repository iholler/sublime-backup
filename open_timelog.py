import sublime, sublime_plugin, re

class OpenTimeLogCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.active_window().run_command('open_file', {'file': '/C/Users/Stephen/Desktop/timelog.md'})