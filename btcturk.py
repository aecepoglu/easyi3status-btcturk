from statusModule import EasyI3StatusModule
from requests import get
from threading import Thread

class Module(EasyI3StatusModule):
	def _setValue(self):
		self.isBusy = True

		resp = get('https://btcturk.com/api/ticker')

		if resp.status_code == 200:
			jsonobj = [x for x in resp.json() if x["pair"] == "BTCTRY"][0]
			self.values[0]['full_text'] = u'B⃦/₺ ' + str(jsonobj['average'])

		self.isBusy = False


	def setValue(self):
		if not self.isBusy:
			Thread(target=self._setValue).start()

	def __init__(self, config):
		self.values = [{
			'full_text': u'btcturk',
			'separator_block_width': 40
		}]
		self.validDuration = 900
		self.isBusy = False
		self.setValue()

	def update(self):
		self.setValue()
