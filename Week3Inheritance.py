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
        self.bookcost = bcost
        
    #def Book_Total(x):
    book_quantity = int(input("Enter number of books desired: "))
    bcost = float(input("Enter cost of book: $"))
    btotal = book_quantity*bcost
    
#subclass 2
class Journal (Order):
    def __init__ (self, j_type, jbarcode, jcost):
        self.j_type = j_type
        self.jbarcode = jbarcode
        self.journalcost = jcost
        
    #def Journal_Total(y):
    journal_quantity = int(input("Enter number of journals desired: "))
    jcost = float(input("Enter cost of journal: $"))
    jtotal = journal_quantity*jcost
       
#subclass 3
class Pens (Order):
    def __init__(self, p_type, brand, packsize, pbarcode, pcost):
        self.p_type = p_type
        self.brand = brand
        self.packsize = packsize
        self.pbarcode = pbarcode
        self.pencost = pcost
        
    #def Pen_Total(z):
    pen_total = int(input("Enter number of pens desired: "))
    pcost = float(input("Enter cost of pens: $"))
    ptotal = pen_total*pcost
    
print()
print()
print("Total for books is $", Book.btotal)
print("Total for journals is $", Journal.jtotal)
print("Total for pens is $", Pens.ptotal)