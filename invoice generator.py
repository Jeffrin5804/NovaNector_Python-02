# Function to generate an invoice
def generate_invoice(customer_info, items, invoice_number, invoice_date):
    # Header of the invoice
    invoice = f"""
====================================================
|                INVOICE                          |
====================================================
| Invoice Number: {invoice_number: <28} |
| Date: {invoice_date: <35} |
====================================================
| Customer Information:                            |
----------------------------------------------------
{customer_info}
----------------------------------------------------
| Items:                                           |
----------------------------------------------------
| Description            | Quantity | Price   | Total |
----------------------------------------------------"""

    subtotal = 0

    # Add each item to the invoice
    for item in items:
        description, quantity, price = item
        total_item_price = quantity * price
        subtotal += total_item_price
        invoice += f"\n| {description: <22} | {quantity: ^8} | ${price: <7.2f} | ${total_item_price: <5.2f} |"

    # Calculate total amount due
    tax_rate = 0.08  # Example tax rate of 8%
    tax_amount = subtotal * tax_rate
    total_amount = subtotal + tax_amount

    # Add totals section to the invoice
    invoice += f"""
----------------------------------------------------
| Subtotal:                                ${subtotal: <29.2f} |
| Tax ({tax_rate*100}%):                     ${tax_amount: <29.2f} |
| Total Amount Due:                        ${total_amount: <29.2f} |
----------------------------------------------------
| Thank you for your business!                      |
====================================================
"""

    return invoice

# Example usage:
if __name__ == "__main__":
    # Example data
    customer_info = "John Doe\n123 Main St, Anytown, CA\nEmail: john.doe@example.com"
    items = [
        ("Product A", 2, 25.00),
        ("Product B", 1, 50.00),
        ("Product C", 3, 10.00)
    ]
    invoice_number = "INV-001"
    invoice_date = "2024-07-17"

    # Generate and print the invoice
    generated_invoice = generate_invoice(customer_info, items, invoice_number, invoice_date)
    print(generated_invoice)
