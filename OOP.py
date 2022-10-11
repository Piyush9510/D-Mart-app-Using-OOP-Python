class DMart:
    cart = {}
    bill = 0
    def add_itms(self,choice,qty):
        DMart.cart.update({choice:qty})
    def remove_items(self,name):
        DMart.cart.pop(name)
    def Bill(self,rs):
        DMart.bill+=rs

    def remove_items(self):
        pass

nm = input('Please enter your name:')
print('==================================')
print('Hello',nm,'welcome to DMart app enjoy your shoping')
print('==================================')
while True:
    print('Please select the category you are want to purchase from the list below')
    print('1.Grocery\n2.Dairy and Bevarages\n3.remove items\n4.current cart\n5.Exit')
    n = int(input('Enter your choice number ='))
    print('==================================')
    c = DMart()
    if n == 1:
        print('1.Dals\n2.Pulse\n3.cooking oil\n4.Ghee and Vanaspati'
              '\n5.Rice\n6.Masala and spices\n7.Salt/Sugar/Jaggery')
        choice=int(input('Enter the choce number'))
        if choice==1:
            qty=int(input('select kg\n1.500gm\n2.1kg'))
            if qty==1:
                choice='Dal'
                qty='500gm'
                rs = 45
                c.add_itms(choice,qty)
                c.Bill(rs)
            elif qty==2:
                choice='Dal'
                qty='1 Kg'
                rs = 90
                c.add_itms(choice,qty)
                c.Bill(rs)
                print('Your cart contains',DMart.cart)
                print('Your current bill',DMart.bill,'Rs.')
        elif choice == 2:
            choice = 'Rajma'
            qty = '500gm'
            rs = 110
            c.add_itms(choice, qty)
            c.Bill(rs)
            print('Your cart contains', DMart.cart)
            print('Your current bill', DMart.bill, 'Rs.')
        elif choice==3:
            qt = int(input('select liters\n1.1 liter\n2.5 liter'))
            if qt == 1:
                choice = 'oil_small'
                qty = '1 liter'
                rs = 180
                c.add_itms(choice, qty)
                c.Bill(rs)
            elif qt == 2:
                choice = 'oil_large'
                qty = '5 liter'
                rs = 1000
                c.add_itms(choice, qty)
                c.Bill(rs)
                print('Your cart contains', DMart.cart)
                print('Your current bill', DMart.bill, 'Rs.')
        elif choice==4:
            qty=int(input('select kg\n1.500ml\n2.1liter\n'))
            if qty==1:
                choice='Ghee_small'
                qty='500ml'
                rs = 300
                c.add_itms(choice,qty)
                c.Bill(rs)
            elif qty==2:
                choice='Ghee_large'
                qty='1 liter'
                rs = 600
                c.add_itms(choice,qty)
                c.Bill(rs)
                print('Your cart contains',DMart.cart)
                print('Your current bill',DMart.bill,'Rs.')
        elif choice==5:
            qty=int(input('select kg\n1.1kg\n2.5kg'))
            if qty==1:
                choice='Rice_small'
                qty='1kg'
                rs = 100
                c.add_itms(choice,qty)
                c.Bill(rs)
            elif qty==2:
                choice = 'Rice_large'
                qty = '5kg'
                rs = 500
                c.add_itms(choice, qty)
                c.Bill(rs)
                print('Your cart contains',DMart.cart)
                print('Your current bill',DMart.bill,'Rs.')
        elif choice == 6:
            qt = int(input('select type of masala\n1.Chiken masala\n2.fish masala\n3.Garam masala'))
            if qt == 1:
                choice = 'Chiken masala'
                qty = '500 gm'
                rs = 180
                c.add_itms(choice, qty)
                c.Bill(rs)
                print('Your cart contains', DMart.cart)
                print('Your current bill', DMart.bill, 'Rs.')
            elif qt == 2:
                choice = 'fish masala'
                qty = '500 gm'
                rs = 180
                c.add_itms(choice, qty)
                c.Bill(rs)
                print('Your cart contains', DMart.cart)
                print('Your current bill', DMart.bill, 'Rs.')
            elif qt == 3:
                choice = 'Garam masala'
                qty = '500 gm'
                rs = 180
                c.add_itms(choice, qty)
                c.Bill(rs)
                print('Your cart contains', DMart.cart)
                print('Your current bill', DMart.bill, 'Rs.')
        elif choice == 7:
            qt = int(input('select what you want to buy\n1.salt\n2.sugar\n3.jaggery'))
            if qt == 1:
                choice = 'Salt'
                qty = '500 gm'
                rs = 50
                c.add_itms(choice, qty)
                c.Bill(rs)
            elif qt == 2:
                choice = 'Sugar'
                qty = '1 kg'
                rs = 100
                c.add_itms(choice, qty)
                c.Bill(rs)
                print('Your cart contains', DMart.cart)
                print('Your current bill', DMart.bill, 'Rs.')
            elif qt == 3:
                choice = 'Jaggery'
                qty = '500 gm'
                rs = 60
                c.add_itms(choice, qty)
                c.Bill(rs)
                print('Your cart contains', DMart.cart)
                print('Your current bill', DMart.bill, 'Rs.')
    elif n==2:
        m = int(input('Enter what you want to access\n1.Beverages\n2.Dairy'))
        if m==1:
            print('What you want to buy\n1.Tea,\n2.Coffee')
            qt=int(input("enter your choice"))
            if qt==1:
                choice = 'Tea'
                qty = '500 gm'
                rs = 100
                c.add_itms(choice, qty)
                c.Bill(rs)
                print('Your cart contains', DMart.cart)
                print('Your current bill', DMart.bill, 'Rs.')
            elif qt == 2:
                choice = 'coffee'
                qty = '500 gm'
                rs = 200
                c.add_itms(choice, qty)
                c.Bill(rs)
                print('Your cart contains', DMart.cart)
                print('Your current bill', DMart.bill, 'Rs.')
        elif m == 2:
            print('What you want to buy\n1.Milk,\n2.Amul Butter')
            qt = int(input("enter your choice"))
            if qt == 1:
                choice = 'Milk'
                qty = '1 liter'
                rs = 60
                c.add_itms(choice, qty)
                c.Bill(rs)
                print('Your cart contains', DMart.cart)
                print('Your current bill', DMart.bill, 'Rs.')
            elif qt == 2:
                choice = 'Amul Butter'
                qty = '500 gm'
                rs = 245
                c.add_itms(choice, qty)
                c.Bill(rs)
                print('Your cart contains', DMart.cart)
                print('Your current bill', DMart.bill, 'Rs.')
    elif n == 4:
        print(DMart.cart,'and Bill Ammount is',DMart.bill)
    elif n == 5:
        print('Thank you for shoping Directing you towads payment......')
        exit()





















