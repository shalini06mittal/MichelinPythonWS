
'''
dictionary will have foll data
invoiceno
date when invoice was generated => python date format or use string
customer name
total amount
status -> any of the below
ORDERED
DELIVERED
PENDING

# BEGINNERS
Create a function count that takes list of dictionary as input 
Display the count of orderers, pending and delivered invoices

# STEP AHEAD
Create a function count that takes list of dictionary as input and date
Display the count of orderers, pending and delivered invoices on that date
'''
def count_invoices(invoices):

    ordered_count = 0

    delivered_count = 0

    pending_count = 0

    for invoice in invoices:

        status = invoice.get('status', '').upper()

        if status == 'ORDERED':

            ordered_count += 1

        elif status == 'DELIVERED':

            delivered_count += 1

        elif status == 'PENDING':

            pending_count += 1

    print(f"Ordered: {ordered_count} invoices")

    print(f"Delivered: {delivered_count} invoices")

    print(f"Pending: {pending_count} invoices")

 
invoices_data = [

    {'invoiceno': '123', 'date': '2023-01-01', 'customer_name': 'John Doe', 'total_amount': 100, 'status': 'ORDERED'},

    {'invoiceno': '124', 'date': '2023-01-02', 'customer_name': 'Jane Smith', 'total_amount': 150, 'status': 'DELIVERED'},

    {'invoiceno': '125', 'date': '2023-01-03', 'customer_name': 'Bob Johnson', 'total_amount': 120, 'status': 'PENDING'},

    {'invoiceno': '126', 'date': '2023-01-02', 'customer_name': 'Elvish Doe', 'total_amount': 200, 'status': 'ORDERED'}

]

print(invoices_data) 

count_invoices(invoices_data)