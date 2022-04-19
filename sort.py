import subprocess

import sublime_plugin


class IsortFormat(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        if view.file_name().endswith(".py"):
            subprocess.run(f"isort {view.file_name()}".split(), shell=True)
