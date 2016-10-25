import sublime, sublime_plugin, re

class StripspaceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for sel in self.view.sel():
			# Get the selected text
			selection = sel
			# e.g., selection = '<span>           There's way too much extra space             </span>'
			text = self.view.substr(sel)
			# Transform it
			pattern = re.compile(r'(\s{2,})')
			output = re.sub(pattern, r' ', text)
			# Replace the selection with transformed text
			self.view.replace(edit, selection, output)