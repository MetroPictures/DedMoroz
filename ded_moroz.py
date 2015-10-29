import os, logging
from sys import argv, exit
from time import sleep

from core.api import MPServerAPI

class DedMoroz(MPServerAPI):
	def __init__(self):
		MPServerAPI.__init__(self)
		logging.basicConfig(filename=self.conf['d_files']['module']['log'], level=logging.DEBUG)

	def play_voiceover(self):
		#loops!
		return self.play(os.path.join("prompts", "DED_MOROZ.wav"))

	def run_script(self):
		super(DedMoroz, self).run_script()
		self.play_voiceover()

if __name__ == "__main__":
	res = False
	dm = DedMoroz()

	if argv[1] in ['--stop', '--restart']:
		res = dm.stop()
		sleep(5)

	if argv[1] in ['--start', '--restart']:
		res = dm.start()

	exit(0 if res else -1)