# Encapsulation Demo: Order Management System
class Order:
    def __init__(self, order_id, customer_name):
        self.__order_id = order_id  # Private attribute
        self.__customer_name = customer_name  # Private attribute
        self.__items = []  # Private attribute

    def add_item(self, item_name, quantity, price):
        item = {
            'item_name': item_name,
            'quantity': quantity,
            'price': price
        }
        self.__items.append(item)

    def get_order_details(self):
        return {
            'order_id': self.__order_id,
            'customer_name': self.__customer_name,
            'items': self.__items
        }

    def __calculate_total(self):
        total = sum(item['quantity'] * item['price'] for item in self.__items)
        return total
    
# %%    
class OrderManager:
    def __init__(self):
        self.__orders = {}  # Private attribute

    def create_order(self, order_id, customer_name):
        order = Order(order_id, customer_name)
        self.__orders[order_id] = order
        return order

    def get_order(self, order_id):
        return self.__orders.get(order_id)

    def get_order_total(self, order_id):
        order = self.get_order(order_id)
        if order:
            # Accessing the private method of Order class
            return order._Order__calculate_total()
        return None
    
if __name__ == "__main__":
    manager = OrderManager()
    order1 = manager.create_order(1, "Alice")
    order1.add_item("Laptop", 1, 1200)
    order1.add_item("Mouse", 2, 25)

    order2 = manager.create_order(2, "Bob")
    order2.add_item("Keyboard", 1, 100)
    order2.add_item("Monitor", 2, 300)

    print("Order 1 Details:", order1.get_order_details())
    print("Order 1 Total:", manager.get_order_total(1))

    print("Order 2 Details:", order2.get_order_details())
    print("Order 2 Total:", manager.get_order_total(2))