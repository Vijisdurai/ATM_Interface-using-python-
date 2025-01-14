import customtkinter as ctk
from tkinter import messagebox, simpledialog

class ATMInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine")
        self.root.geometry("500x400")  # Adjust window size
        self.accounts = {
            '1234': {'balance': 1000.0, 'transactions': []},
            '5678': {'balance': 500.0, 'transactions': []}
        }
        self.active_account = None
        self.show_login_screen()

    def show_login_screen(self):
        self.clear_screen()
        ctk.CTkLabel(self.root, text="Enter PIN:").pack(pady=10)
        self.pin_entry = ctk.CTkEntry(self.root, show='*')
        self.pin_entry.pack(pady=5)
        ctk.CTkButton(self.root, text="Login", command=self.login).pack(pady=5)

    def login(self):
        pin = self.pin_entry.get().strip()
        if pin in self.accounts:
            self.active_account = pin
            messagebox.showinfo("Login", "Login Successful!")
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid PIN.")

    def show_main_menu(self):
        self.clear_screen()
        ctk.CTkButton(self.root, text="Check Balance", command=self.check_balance, width=20).pack(pady=5)
        ctk.CTkButton(self.root, text="Deposit", command=self.deposit_funds, width=20).pack(pady=5)
        ctk.CTkButton(self.root, text="Withdraw", command=self.withdraw_funds, width=20).pack(pady=5)
        ctk.CTkButton(self.root, text="Transaction History", command=self.show_transactions, width=20).pack(pady=5)
        ctk.CTkButton(self.root, text="Logout", command=self.root.quit, width=20).pack(pady=5)

    def check_balance(self):
        balance = self.accounts[self.active_account]['balance']
        messagebox.showinfo("Balance", f"Your balance is ${balance:.2f}")

    def deposit_funds(self):
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
        if amount and amount > 0:
            self.accounts[self.active_account]['balance'] += amount
            self.accounts[self.active_account]['transactions'].append(f"Deposited ${amount:.2f}")
            messagebox.showinfo("Deposit", f"Deposited ${amount:.2f}")
        else:
            messagebox.showerror("Error", "Invalid amount entered.")

    def withdraw_funds(self):
        amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
        balance = self.accounts[self.active_account]['balance']
        if amount and 0 < amount <= balance:
            self.accounts[self.active_account]['balance'] -= amount
            self.accounts[self.active_account]['transactions'].append(f"Withdrew ${amount:.2f}")
            messagebox.showinfo("Withdraw", f"Withdrew ${amount:.2f}")
        else:
            messagebox.showerror("Error", "Invalid amount or insufficient funds.")

    def show_transactions(self):
        transactions = self.accounts[self.active_account]['transactions']
        history = "\n".join(transactions) if transactions else "No transactions yet."
        messagebox.showinfo("Transaction History", history)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    window = ctk.CTk()
    atm_gui = ATMInterface(window)
    window.mainloop()
