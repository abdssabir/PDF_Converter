from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

def image_to_pdf(image_path, pdf_path):
    # Open the image file
    img = Image.open(image_path)

    # Create a PDF file
    pdf_canvas = canvas.Canvas(pdf_path, pagesize=letter)

    # Set the dimensions of the PDF page to match the image
    pdf_canvas.setPageSize((img.width, img.height))

    # Draw the image on the PDF
    pdf_canvas.drawImage(image_path, 0, 0, width=img.width, height=img.height)

    # Save the PDF file
    pdf_canvas.save()

# Example usage:
image_path = r'C:\Users\ali\Documents\repos\PDF_Converter/image.jpg'  # Replace with the path to your image
pdf_path = r'C:\Users\ali\Documents\repos\PDF_Converter/file.pdf'    # Replace with the desired output PDF file path

image_to_pdf(image_path, pdf_path)
