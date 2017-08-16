from kivy.uix.screenmanager import Screen

from menuinterface import SoundSettings

class MainMenuScreen(Screen):

	audio_mainmenu_sound = SoundSettings.audio_mainmenu_sound

	def on_enter(self,*args):
		SoundSettings.playMusic(self.audio_mainmenu_sound)

	def on_leave(self, *args):
		self.audio_mainmenu_sound.stop()




