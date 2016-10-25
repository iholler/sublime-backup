import sublime, sublime_plugin, re, pprint

class SplitCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for sel in self.view.sel():
			# Get the selected text
			selection = sel
			# selection = '<input id="txtBrandName" class="ng-pristine ng-valid" type="text" name="BrandName" ng-model="BrandName" ng-init="BrandName=\"<?php echo $ng_name; ?>\"" value="<?php echo $results[\'details\'][\'BrandName\']; ?>" maxlength="100" />'
			print('selection output: ',selection)
			text = self.view.substr(sel)
			# Transform it
			pattern = re.compile(r'\s+(((\w|-)+=(\"|\')|(\/>))|(\s*(?<!\?)>))')
			text = re.sub(pattern, r'\n\t\1', text)

			pattern = re.compile(r'(>)$')
			text = re.sub(pattern, r'\n\t\1', text)

			# Replace the selection with transformed text
			self.view.replace(edit, selection, text)

