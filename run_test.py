import sublime
import sublime_plugin

class PyTestCommand(sublime_plugin.TextCommand):
  def run(self, edit, **args):

    for region in self.view.sel():
      if region.empty():
        line = self.view.line(region)
        # line_contents = self.view.substr(line) + '\n'
        # self.view.insert(edit, line.begin(), line_contents)
      else:
        # line = self.view.substr(region)
        print("fire!")
        print(self.view.substr(region))
        # self.view.insert(edit, region.begin(), self.view.substr(region))
