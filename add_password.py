# Import the library needed to work with PDF files
import PyPDF2
import os # We need this to check if a file exists

def add_password_to_pdf():
    """
    This function adds a user-specified password to a PDF file.
    It prompts the user for the input filename, output filename, and the password.
    It automatically ensures the output file has a .pdf extension.
    """
    try:
        # --- Get Input from User (Dynamic Part) ---
        input_pdf_path = input("Enter the name of the PDF file (e.g., ABCD.pdf): ")

        # --- Debugging/Error Handling ---
        # Check if the input file actually exists before doing anything else
        if not os.path.exists(input_pdf_path):
            print(f"Error: The file '{input_pdf_path}' was not found. Please make sure it's in the same folder.")
            return # Stop the function if the file doesn't exist

        output_pdf_path = input("Enter the name for the new protected PDF (e.g., protected_ABCD): ")
        
        # --- NEW: Smartly handle the .pdf extension ---
        # Check if the user's input already ends with .pdf (case-insensitive)
        if not output_pdf_path.lower().endswith('.pdf'):
            # If it doesn't, add the .pdf extension
            output_pdf_path += '.pdf'
            
        password = input("Enter the password you want to set: ")

        # --- PDF Processing ---
        pdf_reader = PyPDF2.PdfReader(input_pdf_path)
        pdf_writer = PyPDF2.PdfWriter()

        # Copy all pages from the original PDF to the new one
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

        # Encrypt the new PDF with the user's password
        print("Encrypting the file...")
        pdf_writer.encrypt(password)

        # Save the new, encrypted PDF to a file
        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f"✅ Success! Password added. The new file is saved as '{output_pdf_path}'.")

    except PyPDF2.errors.PdfReadError:
        print(f"Error: Could not read '{input_pdf_path}'. It might be corrupted or not a valid PDF.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# --- Run the main function ---
if __name__ == "__main__":
    add_password_to_pdf()