import tkinter as tk
from tkinter import ttk
from random import sample
from Cache_Algorithm import Cache_Algorithm

class Cache_GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cache Simulator")
        self.geometry("800x600")
        self.configure(bg='black')

        self.create_widgets()

    def validate_integer(self, new_value):
        if not new_value: 
            return True
        try:
            int(new_value)
            return True
        except ValueError:
            return False

    def create_widgets(self):
        label = tk.Label(self, text="Cache Simulator", font=("Arial", 20, 'bold'), fg='white', bg='black')
        label.pack(pady=20)

        input_frame = tk.Frame(self, bg='black')
        input_frame.pack(side=tk.TOP, padx=20, pady=20)

        cache_blocks_label = tk.Label(input_frame, text="Input # of Cache Blocks:", font=("Arial", 10, 'bold'), fg='white',  bg='black')
        cache_blocks_label.pack()

        validate_command = (self.register(self.validate_integer), '%P')
        self.cache_blocks_entry = tk.Entry(input_frame, validate='key', validatecommand=validate_command)
        self.cache_blocks_entry.pack(pady=10)

        test_case_label = tk.Label(input_frame, text="Choose Test Case:", font=("Arial", 10, 'bold'), fg='white',  bg='black')
        test_case_label.pack()
        self.test_case_var = tk.StringVar()
        test_case_options = ['Sequential', 'Random', 'Mid-Repeat']
        self.test_case_dropdown = ttk.Combobox(input_frame, textvariable=self.test_case_var, values=test_case_options)
        self.test_case_dropdown.set(test_case_options[0])
        self.test_case_dropdown.pack(pady=10)

        step_by_step_var = tk.BooleanVar()
        step_by_step_checkbox = tk.Checkbutton(input_frame, text="Step-by-Step", variable=step_by_step_var, bg='lightgrey')
        step_by_step_checkbox.pack(pady=10)

        run_button = tk.Button(input_frame, text="  Simulate  ", command=lambda: self.run_simulation(step_by_step_var.get()))
        run_button.pack(side=tk.LEFT, padx=10, pady=10)

        reset_button = tk.Button(input_frame, text="  Reset  ", command=self.reset_display)
        reset_button.pack(side=tk.LEFT, padx=10, pady=10)

        result_frame = tk.Frame(self, bg='lightgrey')
        result_frame.pack(side=tk.BOTTOM, padx=20, pady=20)

        scrollbar = tk.Scrollbar(result_frame, orient=tk.VERTICAL)
        self.result_text = tk.Text(result_frame, height=20, width=55, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.pack()

    def run_simulation(self, step_by_step):
        try:
            num_cache_blocks = int(self.cache_blocks_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid number of cache blocks.")
            return

        self.result_text.delete(1.0, tk.END)

        simulator = Cache_Algorithm(num_cache_blocks, 64, 'load-through', num_cache_blocks, 4)

        test_case = self.test_case_var.get()
        simulator.run_simulation(test_case, step_by_step)

        if step_by_step:
            for cache_snapshot in simulator.trace:
                self.result_text.insert(tk.END, cache_snapshot)
        else:
            self.result_text.insert(tk.END, "".join(simulator.trace))

        self.result_text.insert(tk.END, "Simulation Completed!\n")


    def reset_display(self):
        self.result_text.delete(1.0, tk.END)
        self.cache_blocks_entry.delete(0, tk.END)
        self.test_case_var.set('')
        self.cache_blocks_entry.focus()


if __name__ == "__main__":
    app = Cache_GUI()
    app.mainloop()
