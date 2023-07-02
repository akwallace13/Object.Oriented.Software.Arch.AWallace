from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

#superclass
class Order(Base):
    def __init__(self, tax, discount, total, item_qty):
        self.tax = tax
        self.discount = discount
        self.total = total
        self.item_qty = item_qty
        
    __tablename__ = 'Order'
    
    id = Column(Integer, primary_key=True)
    tax = Column(Integer)
    discount = Column(Integer)
    total = Column(Integer)
    item_qty = Column(Integer)
    
    def __repr__(self):
        return "<Order(tax=(0), discount=(1), total=(2), item_qty=(3))>".format(self.tax, self.discount, self.total, self.item_qty)

#create database    
def main():
    cart = create_engine('sqlite:///assignment', echo=False)
    
    Base.metadata.create_all(cart)
    
    #add item
    order1 = Order(1.39, 0, 46.89, 6)
    print(order1)
    
    #create session
    Session = sessionmaker(bind=cart)
    session = Session()
    
    session.add(order1)
    
    #filter out
    newOrder1 = session.query(Order).filter_by(total=46.89).first()
    print(newOrder1)
    
    #add new data
    order1.discount = 1.5
    print(session.dirty)
    session.commit()
    
    print(order1.id)
    
    #add multiple
    session.add_all([
        Order(.89, 0, 4.86, 2),
        Order(1, 5, 9, 2)])
    session.commit()
    
    for row in session.query(Order).all():
        print (row.total, row.item_qty)
        
    
    
    
    
    
    
    
       
#subclass 1
# class Book (Order):
#     def __init__(self, title, author, bbarcode, bcost):
#         self.title = title
#         self.author = author
#         self.bbarcode = bbarcode
#         self.bookcost = bcost
        
#     #def Book_Total(x):
#     book_quantity = int(input("Enter number of books desired: "))
#     bcost = float(input("Enter cost of book: $"))
#     btotal = book_quantity*bcost
    
# #subclass 2
# class Journal (Order):
#     def __init__ (self, j_type, jbarcode, jcost):
#         self.j_type = j_type
#         self.jbarcode = jbarcode
#         self.journalcost = jcost
        
#     #def Journal_Total(y):
#     journal_quantity = int(input("Enter number of journals desired: "))
#     jcost = float(input("Enter cost of journal: $"))
#     jtotal = journal_quantity*jcost
       
# #subclass 3
# class Pens (Order):
#     def __init__(self, p_type, brand, packsize, pbarcode, pcost):
#         self.p_type = p_type
#         self.brand = brand
#         self.packsize = packsize
#         self.pbarcode = pbarcode
#         self.pencost = pcost
        
#     #def Pen_Total(z):
#     pen_total = int(input("Enter number of pens desired: "))
#     pcost = float(input("Enter cost of pens: $"))
#     ptotal = pen_total*pcost
    
# print()
# print()
# print("Total for books is $", Book.btotal)
# print("Total for journals is $", Journal.jtotal)
# print("Total for pens is $", Pens.ptotal)
# print()

# items = Book.book_quantity + Journal.journal_quantity + Pens.pen_total
# order_total = Book.btotal + Journal.jtotal + Pens.ptotal
# print("Total number of items is: ", items)
# print("Total before tax is $:", order_total)