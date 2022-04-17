import subprocess

import sublime
import sublime_plugin


class IsortFormat(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        subprocess.check_call("isort '%s'" % view.file_name(), shell=True)
