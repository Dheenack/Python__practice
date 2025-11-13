class Restaurant:
    def __init__(self):
        self.menu = {
            "Idly": 10,
            "Dosa": 15,
            "Kichdi": 12
        }
        self.orders = []

    def show_menu(self):
        print("\nMenu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def take_order(self):
        item = input("Enter item name: ").title()
        if item in self.menu:
            self.orders.append(item)
            print("Item added to order")
        else:
            print("Item not found")

    def view_order(self):
        if not self.orders:
            print("No orders")
        else:
            print("Orders:")
            for i, item in enumerate(self.orders, 1):
                print(f"{i}: {item}")

    def total_bill(self):
        total = sum(self.menu[item] for item in self.orders)
        print(f"Total bill: ${total}")

    def run(self):
        while True:
            print("\nRestaurant App:")
            print("1. Show Menu\n2. Take Order\n3. View Order\n4. Total Bill\n5. Exit")
            ch = input("Enter your choice: ")
            match ch:
                case "1":
                    self.show_menu()
                case "2":
                    self.take_order()
                case "3":
                    self.view_order()
                case "4":
                    self.total_bill()
                case "5":
                    print("Thank you for visiting!")
                    break
                case _:
                    print("Invalid option")

if __name__ == "__main__":
    Restaurant().run()
