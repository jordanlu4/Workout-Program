import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")
        

        self.entry = tk.Entry(root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.add_button_click_func()

    def add_button_click_func(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 1),
            ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
            ('C', 4, 0), ('=', 4, 2)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=10, height=2, command=lambda text=text: self.on_button_click(text))
            button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                self.entry.insert(tk.END, f" = {eval(self.entry.get())}")
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, char)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
