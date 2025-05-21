# Write code below 💖
class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
      self.balance += amount
      print(f"Has depositado {amount} €. Tu saldo actual es: {self.balance} €.")

  def withdraw(self, amount):
      self.balance -= amount
      print(f"Has retirado {amount} €. Tu saldo actual es: {self.balance} €.")

  def display_balance(self):
      print(f"Tu saldo actual es: {self.balance} €")
      
account_1 = BankAccount("Peter", "Parker", 20999, "private", 7777, 899.87)
account_1.display_balance()
account_1.deposit(90)
account_1.withdraw(50)