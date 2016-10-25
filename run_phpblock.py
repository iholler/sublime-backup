# ******************************************************************************
# >> PHP Block Commenter for HTML
# ******************************************************************************
#	Description:
# 	RECEIVE user's selected text
# 	STORE the current indention level at the beginning of the selection as '$initial_indention_lvl'
#	INSERT beginning php statement && starts block comment tag '<?php /*'
#	REGEX REPLACE the following in user selection pattern='(\n^\s*)' replacement='\1\t'
#	RETURN processed user selection
# 	INSERT closing block comment && closing php tag '\n{$initial_indention_lvl}*/ ?>'

# import sublime, sublime_plugin

# class PhpblockCommand(sublime_plugin.TextCommand):
# 	def run(self, edit):
# 		self.view.insert(edit, 0, "Hello, World!")
