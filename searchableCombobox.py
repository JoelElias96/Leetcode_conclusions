import tkinter as tk
from tkinter import ttk

class SearchableCombobox(tk.Frame):
    def __init__(self, root, options, **kwargs):
        super().__init__(root, **kwargs)
        self.options = options
        self.filtered_options = options.copy()

        # StringVar to track changes in the Combobox's text
        self.var = tk.StringVar()

        # Create the Combobox and set it to use grid
        self.combo = ttk.Combobox(self, textvariable=self.var)
        self.combo.set("Select an option")
        self.combo['values'] = self.options  # Set initial values
        self.combo.grid(row=0, column=0, pady=10, sticky="ew")  # Use grid instead of pack

        # Track changes in the text entry of the ComboBox
        self.var.trace("w", self.update_options)
        
        # Bind selection event to handle when an option is selected
        self.combo.bind("<<ComboboxSelected>>", self.on_select)

    def update_options(self, *args):
        # Get the current text in the Combobox
        typed_text = self.var.get().lower()
        
        # Filter options based on typed text
        self.filtered_options = [item for item in self.options if typed_text in item.lower()]
        
        # Update Combobox dropdown values
        self.combo['values'] = self.filtered_options

        # Open the dropdown automatically if there are matches
        if self.filtered_options:
            self.combo.event_generate("<Down>")

    def on_select(self, event=None):
        # You can add any desired functionality here
        selected_item = self.combo.get()  # For example, retrieve the selected item
        print("Selected item:", selected_item)


    def get_selected_item(self):
        # Return the currently selected item
        return self.combo.get()
