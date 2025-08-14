# Import the necessary libraries
import PyPDF2
import os

def remove_password_from_pdf():
    """
    This function removes a password from a protected PDF file.
    It smartly handles file extensions for both input and output files.
    """
    try:
        # --- Get Input from User ---
        input_pdf_path = input("Enter the name of the protected PDF (e.g., protected_ABCD): ")

        # --- NEW: Smartly handle the INPUT .pdf extension ---
        if not input_pdf_path.lower().endswith('.pdf'):
            input_pdf_path += '.pdf'

        # --- Debugging/Error Handling ---
        # Check if the input file actually exists
        if not os.path.exists(input_pdf_path):
            print(f"Error: The file '{input_pdf_path}' was not found.")
            return

        # --- PDF Processing ---
        pdf_reader = PyPDF2.PdfReader(input_pdf_path)

        # Check if the PDF is actually encrypted
        if not pdf_reader.is_encrypted:
            print(f"Info: The file '{input_pdf_path}' is not encrypted. No action needed.")
            return

        # Attempt to decrypt the PDF
        password = input(f"Enter the password for '{input_pdf_path}': ")
        if pdf_reader.decrypt(password):
            # Password was correct
            print("Password accepted! Removing encryption...")
            pdf_writer = PyPDF2.PdfWriter()

            # Copy all pages to a new PDF writer object
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            # Get the desired name for the new, unprotected file
            output_pdf_path = input("Enter the name for the new unprotected PDF (e.g., unprotected_file): ")
            
            # Smartly handle the output .pdf extension
            if not output_pdf_path.lower().endswith('.pdf'):
                output_pdf_path += '.pdf'
            
            # Save the unprotected PDF
            with open(output_pdf_path, 'wb') as output_file:
                pdf_writer.write(output_file)

            print(f"✅ Success! Encryption removed. File saved as '{output_pdf_path}'.")
        else:
            # Password was incorrect
            print("❌ Error: Incorrect password. Please try again.")

    except PyPDF2.errors.PdfReadError:
        print(f"Error: Could not read '{input_pdf_path}'. It might be corrupted or not a valid PDF.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Run the main function ---
if __name__ == "__main__":
    remove_password_from_pdf()