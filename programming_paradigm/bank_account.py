class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional initial balance (default: 0)."""
        self._account_balance = (
            initial_balance  # Encapsulation using a private attribute
        )

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deduct the specified amount from the account balance.
        Return True if successful, False if insufficient funds.
        """
        if amount > self._account_balance:
            return False
        self._account_balance -= amount
        return True

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")
