import sublime
import sublime_plugin

class ViewModeCommand(sublime_plugin.TextCommand):
  def run(self, edit, **args):

    s = sublime.load_settings("Preferences.sublime-settings")
    current = s.get("font_size", 10)
    s.set("font_size", current)

    view = self.view;
    # "Focus: Writer"
    if (args['mode'] == "focus_writer"):
      s.set("wrap_width",         81)
      s.set("gutter",             False)
      s.set("draw_centered",      True)
      s.set("word_wrap",          True)
      s.set("line_numbers",       False)
      s.set("margin",             0)
      s.set("draw_indent_guides", True);

    # "Focus: Debug"
    if (args['mode'] == "php_debug"):
      s.set("wrap_width",         121)
      s.set("gutter",             True)
      s.set("draw_centered",      False)
      s.set("word_wrap",          False)
      s.set("line_numbers",       True)
      s.set("margin",             4)
      s.set("draw_indent_guides", True);

    # "Focus: JS"
    if (args['mode'] == "js_focus"):
      s.set("wrap_width",         81)
      s.set("draw_centered",      True)
      s.set("word_wrap",          True)
      s.set("gutter",             False)
      s.set("line_numbers",       False)
      s.set("margin",             0)
      s.set("draw_indent_guides", False);

    # "Focus: JS - Left"
    if (args['mode'] == "focus_left_gutter"):
      s.set("wrap_width",         0)
      s.set("draw_centered",      False)
      s.set("word_wrap",          True)
      s.set("gutter",             False)
      s.set("line_numbers",       False)
      s.set("margin",             10)
      s.set("draw_indent_guides", False);

    # dfSetting = s.get("fss_on_distraction_free")
    # print ("s.get('fss_on_distraction_free')")
    # print (dfSetting)

    if s.get("fss_on_distraction_free") == None:
      s.set("fss_on_distraction_free", sublime.active_window().settings().get('fss_on_distraction_free'));
      sublime.save_settings("Preferences.sublime-settings");

      # if sublime.active_window().settings().get('fss_on_full_screen'):
        # ST is running on full screen.
    if (args['distraction_free'] == False):
      if s.get("fss_on_distraction_free") == None or s.get("fss_on_distraction_free") == False:
        # ST is running on distraction free mode.
        sublime.active_window().run_command('toggle_distraction_free')
        sublime.active_window().settings().set('fss_on_distraction_free', True)
        s.set("fss_on_distraction_free", True);


    elif (args['distraction_free'] == True):
      # if sublime.active_window().settings().get('fss_on_distraction_free') != True:
      if s.get("fss_on_distraction_free") != True:
        print ("fss_on_distraction_free")
        print (s.get("fss_on_distraction_free") != True)
        print (s.get("fss_on_distraction_free"))
        # ST is running on distraction free mode.
        sublime.active_window().run_command('toggle_distraction_free')
        sublime.active_window().settings().set('fss_on_distraction_free', False)
        s.set("fss_on_distraction_free", False);

    sublime.save_settings("Preferences.sublime-settings")

