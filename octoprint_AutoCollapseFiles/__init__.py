# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin

class AutocollapsefilesPlugin(octoprint.plugin.AssetPlugin):

	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/AutoCollapseFiles.js"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		return dict(
			AutoCollapseFiles=dict(
				displayName="Autocollapsefiles Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="AngryBananer",
				repo="OctoPrint-Autocollapsefiles",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/AngryBananer/OctoPrint-Autocollapsefiles/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "Autocollapsefiles Plugin"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = AutocollapsefilesPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

