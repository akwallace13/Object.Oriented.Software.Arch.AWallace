#standards
TAX = 0.08
discount = 0
tax_amount = 0
quantity = 0
pretax_sale = 0
saletotal = 0

#user interaction
Menu = '''Register Functions

1: Print the Sale (Pretax, No Discounts)
2: Add Discount
3: Calculate Tax
4: Items Sold
5: Total Sale
6: Print Receipt
6: New Transaction
7: Average Sales
8: Total Items Sold

'''


#superclass
class Order:
    def __init__(self, tax, discount, total, item_qty):
        self.tax = tax
        self.discount = discount
        self.total = total
        self.item_qty = item_qty
        
#subclass 1
class Book (Order):
    def __init__(self, title, author, bbarcode, bcost):
        self.title = title
        self.author = author
        self.bbarcode = bbarcode
        self.bcost = bcost
        
    #book total
    book_quantity = int(input("Enter the number of books: "))
    bcost = float(input("Enter cost of book: $"))
    btotal = book_quantity * bcost
    
#subclass 2
class Journal(Order):
    def __init__(self, j_type, jbarcode, jcost):
        self.j_type = j_type
        self.jbarcode = jbarcode
        self.journalcost = jcost
        
    #journal total
    journal_quantity = int(input("Enter the number of journals: "))
    jcost = float(input("Enter cost of journal: $"))
    jtotal = journal_quantity * jcost
    
#subclass 3
class Pens(Order):
    def __init__(self, p_type, pbrand, ppacksize, pbarcode, pcost):
        self.p_type = p_type
        self.pbrand = pbrand
        self.ppacksize = ppacksize
        self.pbarcode = pbarcode
        self.pcost = pcost
        
    #pen total
    pen_total = int(input("Enter the number of pens: "))
    pcost = float(input("Enter cost of pens: $"))
    ptotal = pen_total * pcost
  
  
  
  
print(Menu)
sale_option_text = input("Please select the option you want: ")
sale_option = int(sale_option_text)

while sale_option <1 or sale_option >8:
    print("There is no option with that number.")
    
    sale_option_text = input("Enter the selection you want: ")
    sale_option = int(sale_option_text)
    
print("You have selected option: ", sale_option)
    
    

#option 1: print sales before discounts and tax
def print_sales():
    pretax_sale = Book.btotal + Journal.jtotal + Pens.ptotal
    print("Total for items before tax: $", pretax_sale)
    return pretax_sale

#option 2: add discount
def add_discount():
    discount = float(input("Enter the discount amount: $"))
    discount_pretax_sale = Book.btotal + Journal.jtotal + Pens.ptotal - discount
    pretax_sale = Book.btotal + Journal.jtotal + Pens.ptotal
    print()
    print("The total before discounts is: $", pretax_sale)
    print()
    print("Total discounts: $", discount)
    print("Total after discounts: $", discount_pretax_sale)
    return discount
    
#option 3: calculate tax
def calculate_tax():
    pretax_sale = Book.btotal + Journal.jtotal + Pens.ptotal - discount
    tax_amount = pretax_sale * TAX
    print("Tax rate: ", TAX)
    print("Tax amount: $", tax_amount)
    return tax_amount

#option 4: number of items sold
def items_sold():
    quantity = Book.book_quantity + Journal.journal_quantity + Pens.pen_total
    print("Total number of items sold: ", quantity)
    return quantity

#option 5: total out sale
def total_sale():
    saletotal = Book.btotal + Journal.jtotal + Pens.ptotal - discount - tax_amount
    print("Total for sale: $", saletotal)
    return saletotal

#option 6: print receipt
def print_receipt():
    quantity = Book.book_quantity + Journal.journal_quantity + Pens.pen_total
    pretax_sale = Book.btotal + Journal.jtotal + Pens.ptotal
    tax_amount = pretax_sale * TAX
    saletotal = pretax_sale - discount + tax_amount
    print()
    print()
    print("Total number of items: ", quantity)
    print("Discounts applied: $", discount)
    print("Pretax total: $", pretax_sale)
    print("Calculated tax: $", tax_amount)
    print()
    print("Total for sale: $", saletotal)


#react to user selection
#sale_option = read_int_ranged(menu, 1, 8)
if sale_option == 1:
    print_sales()
else:
    if sale_option == 2:
        add_discount()
    if sale_option == 3:
        calculate_tax()
    if sale_option == 4:
        items_sold()
    if sale_option == 5:
        total_sale()
    if sale_option == 6:
        print_receipt()    
#     if sale_option == 7:
#       new_transaction()   
#     if sale_option == 8:
#       average_sales
 #   if sale_option == 9:
#         total_items_sold