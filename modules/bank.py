from .account import Account


class Bank():
	accounts = []


	def __init__(self):
		self.accounts = [Account()]



	def load_accounts(self):
		try:
			self.accounts = Account.all_accounts()
		except Exception as e:
			print(e)
		except ValueError as e:
			print(e)
			return None

		return self.accounts