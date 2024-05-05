# Generic code for dynamic pdf generation
# Author: Anurag Ranjan

import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Placeholder machine learning model (replace with your model)
def get_predictions(data):
    # Simulate a classification model predicting two classes with probabilities
    probabilities = [0.7, 0.3]  # Replace with actual predictions
    class_labels = ["Class 1", "Class 2"]
    return probabilities, class_labels

def generate_pdf(data):
    # Get dynamic content (replace with your ML logic)
    predictions, class_labels = get_predictions(data)

    # Create a byte buffer to hold the PDF data
    buffer = io.BytesIO()

    # Create a SimpleDocTemplate object for PDF generation
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Define table properties
    col_widths = [180, 120, 100, 80]  # Adjust column widths

    # Extract data from your dictionary (assuming 'data' is a dictionary)
    customer_data = data.get("customers", [])

    # Add table data
    table_data = [["Customer Name", "Payment Mode", "Delivery Date", "Amount"]]
    for row in customer_data:
        table_data.append([row.get("Customer Name", ""), row.get("Payment Mode", ""), row.get("Delivery Date", ""), row.get("Amount", "")])

    # Create Table object
    table = Table(table_data, colWidths=col_widths)

    # Define style for table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    # Add table to the PDF document
    doc.build([table])

    # Save the PDF to a file or return the buffer for further processing
    return buffer.getvalue()

# Example usage with placeholder data
data = {
    "customers": [
        {"Customer Name": "Romona Heaslip", "Payment Mode": "Debit Card", "Delivery Date": "7/11/2015", "Amount": 8529.22},
        {"Customer Name": "John Doe", "Payment Mode": "Credit Card", "Delivery Date": "8/15/2015", "Amount": 1245.50},
        {"Customer Name": "Jane Smith", "Payment Mode": "Cash", "Delivery Date": "9/23/2015", "Amount": 325.75},
        {"Customer Name": "Alice Johnson", "Payment Mode": "Debit Card", "Delivery Date": "10/10/2015", "Amount": 1980.00},
        # Add more customer data here...
    ]
}  # Replace with your actual data structure

# Generate PDF and save it to a file
pdf_bytes = generate_pdf(data)
with open("customer_report.pdf", "wb") as f:
    f.write(pdf_bytes)
