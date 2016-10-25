import sublime
import sublime_plugin
import re


class PhpCommenterPlusCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print("========================================")
		for sel in self.view.sel():
			# Get the selected text
			selection = sel
			# selection = '<input id="txtBrandName" class="ng-pristine ng-valid" type="text" name="BrandName" ng-model="BrandName" ng-init="BrandName=\"<?php echo $ng_name; ?>\"" value="<?php echo $results[\'details\'][\'BrandName\']; ?>" maxlength="100" />'
			text = self.view.substr(sel)
			# print('input: \n',text)


			(row, col) = self.view.rowcol(sel.begin())
			indent_region = self.view.find('^\s+', self.view.text_point(row, 0))

			print("indent level: " + str(self.view.rowcol(indent_region.begin())[1]))

			startLine = self.view.rowcol(selection.a)
			endLine = self.view.rowcol(selection.b)
			indentLevel = startLine
			if endLine < startLine:
				indentLevel = endLine

			print(indentLevel[1])

			tabsToInclude=""
			if indentLevel[1] > 0:
				for x in range(indentLevel[1]):
					tabsToInclude += "\t"

			print("tabs:"+tabsToInclude+"|||endtabs")
			# Transform it
			# pattern = re.compile(r'(\n\n\t*)')
			# modifiedText = re.sub(pattern, r'\n\n', text)
			modifiedText = tabsToInclude + "<?php /* ?>\n" + tabsToInclude + text + "\n" + tabsToInclude + "<?php //*/ ?>"

			output = modifiedText
			# print(output)
			# Replace the selection with transformed text
			self.view.replace(edit, selection, output)
