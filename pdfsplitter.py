import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def split_pdf(input_pdf, output_dir):
    """Splits a PDF into individual pages."""
    try:
        with open(input_pdf, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            for page_num in range(len(pdf_reader.pages)):
                pdf_writer = PyPDF2.PdfWriter()
                pdf_writer.add_page(pdf_reader.pages[page_num])

                output_filename = os.path.join(output_dir, f'page_{page_num + 1}.pdf')
                with open(output_filename, 'wb') as output_file:
                    pdf_writer.write(output_file)
        messagebox.showinfo("Success", "PDF successfully split into individual pages!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_pdf():
    """Opens a file dialog to select the PDF."""
    pdf_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    pdf_path.set(pdf_file)

def select_output_folder():
    """Opens a folder dialog to select the output directory."""
    folder = filedialog.askdirectory()
    output_path.set(folder)

def start_splitting():
    """Starts the PDF splitting process."""
    input_pdf = pdf_path.get()
    output_dir = output_path.get()

    if not input_pdf or not output_dir:
        messagebox.showwarning("Input Error", "Please select both a PDF file and an output folder.")
        return

    split_pdf(input_pdf, output_dir)

# Create the main application window
root = tk.Tk()
root.title("PDF Splitter")

# Variables to store the paths
pdf_path = tk.StringVar()
output_path = tk.StringVar()

# PDF File selection
tk.Label(root, text="Select PDF File:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
tk.Entry(root, textvariable=pdf_path, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_pdf).grid(row=0, column=2, padx=10, pady=10)

# Output Folder selection
tk.Label(root, text="Select Output Folder:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
tk.Entry(root, textvariable=output_path, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_output_folder).grid(row=1, column=2, padx=10, pady=10)

# Split PDF button
tk.Button(root, text="Split PDF", command=start_splitting, width=20).grid(row=2, column=1, padx=10, pady=20)

# Start the main event loop
root.mainloop()
