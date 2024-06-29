
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from datetime import datetime

def create_receipt(receipt_info, file_name='receipt.pdf'):
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Draw Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, height - 50, "Payment Receipt")

    # Draw Date
    c.setFont("Helvetica", 12)
    c.drawString(450, height - 50, f"Date: {datetime.now().strftime('%Y-%m-%d')}")

    # Draw Receipt Details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 100, "Receipt Details:")

    c.setFont("Helvetica", 12)
    receipt_y_position = height - 130

    # Draw a border
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.rect(48, receipt_y_position - 85, width - 120, 80)

    # Receipt Information
    for key, value in receipt_info.items():
        c.drawString(60, receipt_y_position, f"{key}: {value}")
        receipt_y_position -= 20

    # Draw Footer
    footer_y_position = 60
    c.setFont("Helvetica", 10)
    c.drawString(50, footer_y_position, "Thank you for your business!")

    # Save the PDF
    c.save()

# Example usage
receipt_info = {
    "Receipt No": "123456",
    "Customer Name": "John Doe",
    "Amount Paid": "$200.00",
    "Payment Method": "Credit Card",
    "Description": "Purchase of electronics"
}
create_receipt(receipt_info)
