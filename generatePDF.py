import os
from fpdf import FPDF

# Ensure the data/ directory exists
os.makedirs("data", exist_ok=True)

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, "System Documentation: E-Commerce SysOrder", new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(5)

content = """1. System Overview
SysOrder is the central order and customer management system. The primary database is relational (PostgreSQL).

2. Main Table Structure
- Table customers: customer_id (INT), name (VARCHAR), email (VARCHAR), registration_date (DATE).
- Table orders: order_id (INT), customer_id (INT), total_value (DECIMAL), status (VARCHAR), order_date (TIMESTAMP).
- Table order_items: item_id (INT), order_id (INT), product_id (INT), quantity (INT), unit_price (DECIMAL).

3. SQL Query Examples

Example 1: Find a customer by email
SELECT customer_id, name, registration_date 
FROM customers 
WHERE email = 'example@email.com';

Example 2: Calculate total revenue per month (paid orders only)
SELECT DATE_TRUNC('month', order_date) AS month, SUM(total_value) AS revenue
FROM orders
WHERE status = 'paid'
GROUP BY month
ORDER BY month DESC;

Example 3: Identify customers with pending orders older than 7 days
SELECT c.name, c.email, o.order_id, o.total_value
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'pending' 
AND o.order_date < NOW() - INTERVAL '7 days';
"""

pdf = PDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)
pdf.multi_cell(0, 7, text=content)

output_path = "data/sysorder_docs.pdf"
pdf.output(output_path)
print(f"File '{output_path}' generated successfully!")