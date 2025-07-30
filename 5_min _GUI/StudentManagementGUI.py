#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import ttk, messagebox

class import tkinter as tk
from tkinter import ttk, messagebox

class StudentManagementGUI:
    """
    A GUI application for managing student records using Tkinter.
    """

    def __init__(self, root):
        """
        Initialize the application window and widgets.
        """
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x500")
        self.root.configure(bg="#f0f0f0")

        # In-memory storage for student data
        self.students = {}

        # --- Style Configuration ---
        style = ttk.Style()
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 11))
        style.configure("TButton", font=("Arial", 10, "bold"))
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        style.configure("Treeview", rowheight=25, font=("Arial", 10))

        # --- Frames for layout ---
        # Frame for input fields
        self.input_frame = ttk.LabelFrame(root, text="Student Details", padding=(20, 10))
        self.input_frame.pack(padx=20, pady=10, fill="x")
        
        # Frame for buttons
        self.button_frame = ttk.Frame(root, padding=(20, 10))
        self.button_frame.pack(fill="x")
        
        # Frame for the student list (Treeview)
        self.list_frame = ttk.LabelFrame(root, text="Student Records", padding=(20, 10))
        self.list_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # --- Input Widgets ---
        self.setup_input_widgets()

        # --- Button Widgets ---
        self.setup_button_widgets()

        # --- Treeview for Displaying Students ---
        self.setup_treeview()

        # Populate with some sample data
        self.add_sample_data()

    def setup_input_widgets(self):
        """Creates and places the labels and entry fields for student data."""
        ttk.Label(self.input_frame, text="Roll No:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.roll_no_entry = ttk.Entry(self.input_frame, width=30, font=("Arial", 11))
        self.roll_no_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.input_frame, text="Name:").grid(row=0, column=2, padx=15, pady=5, sticky="w")
        self.name_entry = ttk.Entry(self.input_frame, width=30, font=("Arial", 11))
        self.name_entry.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(self.input_frame, text="Marks 1:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.marks1_entry = ttk.Entry(self.input_frame, width=30, font=("Arial", 11))
        self.marks1_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.input_frame, text="Marks 2:").grid(row=1, column=2, padx=15, pady=5, sticky="w")
        self.marks2_entry = ttk.Entry(self.input_frame, width=30, font=("Arial", 11))
        self.marks2_entry.grid(row=1, column=3, padx=5, pady=5)

    def setup_button_widgets(self):
        """Creates and places the action buttons."""
        ttk.Button(self.button_frame, text="Add Student", command=self.add_student).pack(side="left", padx=10)
        ttk.Button(self.button_frame, text="Update Student", command=self.update_student).pack(side="left", padx=10)
        ttk.Button(self.button_frame, text="Delete Student", command=self.delete_student).pack(side="left", padx=10)
        ttk.Button(self.button_frame, text="Search Student", command=self.search_student).pack(side="left", padx=10)
        ttk.Button(self.button_frame, text="Clear Fields", command=self.clear_fields).pack(side="left", padx=10)

    def setup_treeview(self):
        """Creates the Treeview widget to display the list of students."""
        columns = ("roll_no", "name", "marks1", "marks2")
        self.tree = ttk.Treeview(self.list_frame, columns=columns, show="headings")
        
        # Define headings
        self.tree.heading("roll_no", text="Roll No")
        self.tree.heading("name", text="Name")
        self.tree.heading("marks1", text="Marks 1")
        self.tree.heading("marks2", text="Marks 2")

        # Set column widths
        self.tree.column("roll_no", width=100)
        self.tree.column("name", width=250)
        self.tree.column("marks1", width=100)
        self.tree.column("marks2", width=100)
        
        self.tree.pack(fill="both", expand=True)
        
        # Add a scrollbar
        scrollbar = ttk.Scrollbar(self.list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Bind the selection event to a handler function
        self.tree.bind("<<TreeviewSelect>>", self.on_student_select)

    def populate_treeview(self):
        """Clears and re-populates the treeview with current student data."""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add new items from the dictionary
        for roll_no, details in self.students.items():
            self.tree.insert("", "end", values=(roll_no, details['name'], details['marks1'], details['marks2']))

    def add_student(self):
        """Adds a new student record."""
        roll_no = self.roll_no_entry.get()
        name = self.name_entry.get()
        marks1 = self.marks1_entry.get()
        marks2 = self.marks2_entry.get()

        if not all([roll_no, name, marks1, marks2]):
            messagebox.showerror("Error", "All fields are required.")
            return

        if roll_no in self.students:
            messagebox.showerror("Error", f"Student with Roll No {roll_no} already exists.")
            return

        try:
            self.students[roll_no] = {'name': name, 'marks1': int(marks1), 'marks2': int(marks2)}
            messagebox.showinfo("Success", "Student added successfully.")
            self.populate_treeview()
            self.clear_fields()
        except ValueError:
            messagebox.showerror("Error", "Marks must be valid numbers.")

    def update_student(self):
        """Updates an existing student's record."""
        roll_no = self.roll_no_entry.get()
        if not roll_no in self.students:
            messagebox.showerror("Error", f"No student found with Roll No {roll_no}.")
            return

        name = self.name_entry.get()
        marks1 = self.marks1_entry.get()
        marks2 = self.marks2_entry.get()
        
        try:
            self.students[roll_no] = {'name': name, 'marks1': int(marks1), 'marks2': int(marks2)}
            messagebox.showinfo("Success", "Student record updated.")
            self.populate_treeview()
            self.clear_fields()
        except ValueError:
            messagebox.showerror("Error", "Marks must be valid numbers.")

    def delete_student(self):
        """Deletes a student record."""
        roll_no = self.roll_no_entry.get()
        if not roll_no in self.students:
            messagebox.showerror("Error", f"No student found with Roll No {roll_no}.")
            return
        
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete student {roll_no}?"):
            del self.students[roll_no]
            messagebox.showinfo("Success", "Student deleted successfully.")
            self.populate_treeview()
            self.clear_fields()

    def search_student(self):
        """Searches for a student and displays their data in a message box."""
        roll_no = self.roll_no_entry.get()
        if not roll_no:
            messagebox.showwarning("Warning", "Please enter a Roll No to search.")
            return
        
        if roll_no in self.students:
            details = self.students[roll_no]
            info = (f"Roll No: {roll_no}\n"
                    f"Name: {details['name']}\n"
                    f"Marks 1: {details['marks1']}\n"
                    f"Marks 2: {details['marks2']}")
            messagebox.showinfo("Student Found", info)
        else:
            messagebox.showerror("Error", f"No student found with Roll No {roll_no}.")

    def clear_fields(self):
        """Clears all the entry fields."""
        self.roll_no_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.marks1_entry.delete(0, "end")
        self.marks2_entry.delete(0, "end")
        self.tree.selection_remove(self.tree.selection()) # Deselect any item in the list

    def on_student_select(self, event):
        """Populates entry fields when a student is selected from the list."""
        selected_item = self.tree.selection()
        if not selected_item:
            return

        item = self.tree.item(selected_item)
        values = item['values']
        
        self.clear_fields()
        self.roll_no_entry.insert(0, values[0])
        self.name_entry.insert(0, values[1])
        self.marks1_entry.insert(0, values[2])
        self.marks2_entry.insert(0, values[3])

    def add_sample_data(self):
        """Adds a few sample records to get started."""
        sample_data = {
            "101": {'name': 'Alice Johnson', 'marks1': 88, 'marks2': 92},
            "102": {'name': 'Bob Williams', 'marks1': 76, 'marks2': 81},
            "103": {'name': 'Charlie Brown', 'marks1': 95, 'marks2': 89}
        }
        self.students = sample_data
        self.populate_treeview()

if __name__ == "__main__":
    app_root = tk.Tk()
    app = StudentManagementGUI(app_root)
    app_root.mainloop()
:
    """
    A GUI application for managing student records using Tkinter.
    """

    def __init__(self, root):
        """
        Initialize the application window and widgets.
        """
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x500")
        self.root.configure(bg="#f0f0f0")

        # In-memory storage for student data
        self.students = {}

        # --- Style Configuration ---
        style = ttk.Style()
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 11))
        style.configure("TButton", font=("Arial", 10, "bold"))
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        style.configure("Treeview", rowheight=25, font=("Arial", 10))

        # --- Frames for layout ---
        # Frame for input fields
        self.input_frame = ttk.LabelFrame(root, text="Student Details", padding=(20, 10))
        self.input_frame.pack(padx=20, pady=10, fill="x")
        
        # Frame for buttons
        self.button_frame = ttk.Frame(root, padding=(20, 10))
        self.button_frame.pack(fill="x")
        
        # Frame for the student list (Treeview)
        self.list_frame = ttk.LabelFrame(root, text="Student Records", padding=(20, 10))
        self.list_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # --- Input Widgets ---
        self.setup_input_widgets()

        # --- Button Widgets ---
        self.setup_button_widgets()

        # --- Treeview for Displaying Students ---
        self.setup_treeview()

        # Populate with some sample data
        self.add_sample_data()

    def setup_input_widgets(self):
        """Creates and places the labels and entry fields for student data."""
        ttk.Label(self.input_frame, text="Roll No:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.roll_no_entry = ttk.Entry(self.input_frame, width=30, font=("Arial", 11))
        self.roll_no_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.input_frame, text="Name:").grid(row=0, column=2, padx=15, pady=5, sticky="w")
        self.name_entry = ttk.Entry(self.input_frame, width=30, font=("Arial", 11))
        self.name_entry.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(self.input_frame, text="Marks 1:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.marks1_entry = ttk.Entry(self.input_frame, width=30, font=("Arial", 11))
        self.marks1_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.input_frame, text="Marks 2:").grid(row=1, column=2, padx=15, pady=5, sticky="w")
        self.marks2_entry = ttk.Entry(self.input_frame, width=30, font=("Arial", 11))
        self.marks2_entry.grid(row=1, column=3, padx=5, pady=5)

    def setup_button_widgets(self):
        """Creates and places the action buttons."""
        ttk.Button(self.button_frame, text="Add Student", command=self.add_student).pack(side="left", padx=10)
        ttk.Button(self.button_frame, text="Update Student", command=self.update_student).pack(side="left", padx=10)
        ttk.Button(self.button_frame, text="Delete Student", command=self.delete_student).pack(side="left", padx=10)
        ttk.Button(self.button_frame, text="Search Student", command=self.search_student).pack(side="left", padx=10)
        ttk.Button(self.button_frame, text="Clear Fields", command=self.clear_fields).pack(side="left", padx=10)

    def setup_treeview(self):
        """Creates the Treeview widget to display the list of students."""
        columns = ("roll_no", "name", "marks1", "marks2")
        self.tree = ttk.Treeview(self.list_frame, columns=columns, show="headings")
        
        # Define headings
        self.tree.heading("roll_no", text="Roll No")
        self.tree.heading("name", text="Name")
        self.tree.heading("marks1", text="Marks 1")
        self.tree.heading("marks2", text="Marks 2")

        # Set column widths
        self.tree.column("roll_no", width=100)
        self.tree.column("name", width=250)
        self.tree.column("marks1", width=100)
        self.tree.column("marks2", width=100)
        
        self.tree.pack(fill="both", expand=True)
        
        # Add a scrollbar
        scrollbar = ttk.Scrollbar(self.list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Bind the selection event to a handler function
        self.tree.bind("<<TreeviewSelect>>", self.on_student_select)

    def populate_treeview(self):
        """Clears and re-populates the treeview with current student data."""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add new items from the dictionary
        for roll_no, details in self.students.items():
            self.tree.insert("", "end", values=(roll_no, details['name'], details['marks1'], details['marks2']))

    def add_student(self):
        """Adds a new student record."""
        roll_no = self.roll_no_entry.get()
        name = self.name_entry.get()
        marks1 = self.marks1_entry.get()
        marks2 = self.marks2_entry.get()

        if not all([roll_no, name, marks1, marks2]):
            messagebox.showerror("Error", "All fields are required.")
            return

        if roll_no in self.students:
            messagebox.showerror("Error", f"Student with Roll No {roll_no} already exists.")
            return

        try:
            self.students[roll_no] = {'name': name, 'marks1': int(marks1), 'marks2': int(marks2)}
            messagebox.showinfo("Success", "Student added successfully.")
            self.populate_treeview()
            self.clear_fields()
        except ValueError:
            messagebox.showerror("Error", "Marks must be valid numbers.")

    def update_student(self):
        """Updates an existing student's record."""
        roll_no = self.roll_no_entry.get()
        if not roll_no in self.students:
            messagebox.showerror("Error", f"No student found with Roll No {roll_no}.")
            return

        name = self.name_entry.get()
        marks1 = self.marks1_entry.get()
        marks2 = self.marks2_entry.get()
        
        try:
            self.students[roll_no] = {'name': name, 'marks1': int(marks1), 'marks2': int(marks2)}
            messagebox.showinfo("Success", "Student record updated.")
            self.populate_treeview()
            self.clear_fields()
        except ValueError:
            messagebox.showerror("Error", "Marks must be valid numbers.")

    def delete_student(self):
        """Deletes a student record."""
        roll_no = self.roll_no_entry.get()
        if not roll_no in self.students:
            messagebox.showerror("Error", f"No student found with Roll No {roll_no}.")
            return
        
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete student {roll_no}?"):
            del self.students[roll_no]
            messagebox.showinfo("Success", "Student deleted successfully.")
            self.populate_treeview()
            self.clear_fields()

    def search_student(self):
        """Searches for a student and displays their data in a message box."""
        roll_no = self.roll_no_entry.get()
        if not roll_no:
            messagebox.showwarning("Warning", "Please enter a Roll No to search.")
            return
        
        if roll_no in self.students:
            details = self.students[roll_no]
            info = (f"Roll No: {roll_no}\n"
                    f"Name: {details['name']}\n"
                    f"Marks 1: {details['marks1']}\n"
                    f"Marks 2: {details['marks2']}")
            messagebox.showinfo("Student Found", info)
        else:
            messagebox.showerror("Error", f"No student found with Roll No {roll_no}.")

    def clear_fields(self):
        """Clears all the entry fields."""
        self.roll_no_entry.delete(0, "end")
        self.name_entry.delete(0, "end")
        self.marks1_entry.delete(0, "end")
        self.marks2_entry.delete(0, "end")
        self.tree.selection_remove(self.tree.selection()) # Deselect any item in the list

    def on_student_select(self, event):
        """Populates entry fields when a student is selected from the list."""
        selected_item = self.tree.selection()
        if not selected_item:
            return

        item = self.tree.item(selected_item)
        values = item['values']
        
        self.clear_fields()
        self.roll_no_entry.insert(0, values[0])
        self.name_entry.insert(0, values[1])
        self.marks1_entry.insert(0, values[2])
        self.marks2_entry.insert(0, values[3])

    def add_sample_data(self):
        """Adds a few sample records to get started."""
        sample_data = {
            "101": {'name': 'Alice Johnson', 'marks1': 88, 'marks2': 92},
            "102": {'name': 'Bob Williams', 'marks1': 76, 'marks2': 81},
            "103": {'name': 'Charlie Brown', 'marks1': 95, 'marks2': 89}
        }
        self.students = sample_data
        self.populate_treeview()

if __name__ == "__main__":
    app_root = tk.Tk()
    app = StudentManagementGUI(app_root)
    app_root.mainloop()

