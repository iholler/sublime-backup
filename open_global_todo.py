import sublime, sublime_plugin, re

class OpenGlobalTodoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.active_window().run_command('open_file', {'file': '/c/wamp/www/notes/global-todo.md'})