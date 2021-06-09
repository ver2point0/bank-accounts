
from .modules import Owner

class Account():
	def __init__(self, id, balance, owner = None):
		self.id = id

		if balance < 0:
			raise Exception("Insufficient balance! Please set a positive amount.")
		self.balance = balance

		self.owner = owner


	def set_owner(self, owner):
		if self.owner is not None:
			raise Exception("Cannon change an owner once one has been set.")
		self.owner = owner
	
	def withdraw(self, amount):
		if self.balance - amount < 0:
			raise ValueError("Cannot withdraw amount specified.")

		self.balance = self.balance - amount
		return self.balance

	
	def deposit(self, amount):
		self.balance = self.balance + amount
		return self.balance


	def get_balance(self):
		return self.balance