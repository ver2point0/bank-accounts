
from modules.owner import Owner
import csv

class Account():
	def __init__(self, id, balance, open_date, owner = None):

		if id == 666:
			raise Exception("Incorrect accound id.")
		self.id = id

		if balance < 0:
			raise Exception("Insufficient balance! Please set a positive amount.")
		self.balance = balance

		self.open_date = open_date
		self.owner = owner

	def __str__(self):
		owner_name = self.owner.name if self.owner is not None else "[no name]"
		return f"This account is owned by {owner_name} and the current balance is {self.get_balance()}"


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


	@classmethod
	def all_accounts(cls):
		accounts = []
		with open("./support/accounts.csv") as accounts_file:
			data = csv.readr(accounts_file)
			for line in data:
				print(line)
				id = int(line[0])
				balance = int(line[1]) / 100
				open_date = line[2]

				account = cls(id, balance, open_date)
				accounts.append(account)
