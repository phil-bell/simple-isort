import subprocess

import sublime_plugin


class IsortFormat(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        if view.file_name().endswith(".py"):
            run = subprocess.run(
                f"isort '{view.file_name()}'", shell=True, capture_output=True
            )
            print(run.stdout.decode("utf-8"))
            print(run.stderr.decode("utf-8"))
