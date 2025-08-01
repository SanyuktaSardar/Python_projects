from tkinter import *
from tkinter import ttk

FONT = ('Arial', 12)
COLOR = "#f0f8ff"

# Main window
root = Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.config(bg="#f0f8ff")

# Currency list
currency_list = {
    'USD': 86.0866,
    'INR': 1.0,
    'EUR': 99.48,
    'GBP': 116.963,
    'AUD': 56.2431,
    'CAD': 63.7131,
    'JPY': 0.6316,
    'CNY': 11.85,       # Chinese Yuan
    'CHF': 101.44,      # Swiss Franc
    'SGD': 63.72,       # Singapore Dollar
    'NZD': 52.31,       # New Zealand Dollar
    'SEK': 8.37,        # Swedish Krona
    'ZAR': 4.72,        # South African Rand
    'AED': 23.44,       # UAE Dirham
    'SAR': 22.96,       # Saudi Riyal
    'THB': 2.37,        # Thai Baht
    'MYR': 18.29,       # Malaysian Ringgit
    'KRW': 0.062,       # South Korean Won
    'RUB': 0.95         # Russian Ruble
}

# Label: Enter amount
Label(root, text="Enter amount:", font=FONT, bg=COLOR).pack(pady=5)
amount_entry = Entry(root)
amount_entry.pack(pady=5)

# Dropdown: From currency
Label(root, text="From Currency:", font=FONT, bg=COLOR).pack(pady=5)
from_currency = ttk.Combobox(root, values= list(currency_list.keys()), font=FONT)
from_currency.pack(pady=5)
from_currency.set('USD')  # default

# Dropdown: To currency
Label(root, text="To Currency:", font=FONT, bg=COLOR).pack(pady=5)
to_currency = ttk.Combobox(root, values= list(currency_list.keys()), font=FONT)
to_currency.pack(pady=5)
to_currency.set('INR')  # default

# Result label
result_label = Label(root, text="", font=('Arial', 14, 'bold'), bg=COLOR)
result_label.pack(pady=15)

# Convert function
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        result = (amount* currency_list[from_curr])/currency_list[to_curr]
        result_label.config(text=f"{to_curr} {round(result, 2)}")
    except Exception as e:
        result_label.config(text="Error: " + str(e))

# Button
Button(root, text="Convert", font=FONT, bg="#007acc", fg="white", command=convert_currency).pack(pady=10)

root.mainloop()
