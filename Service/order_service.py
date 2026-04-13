from domain.order import Order
from domain.order_item import OrderItem
from domain.product import Product

class OrderService:
  def __init__(self, product_repo, order_repo):
    self.product_repo = product_repo
    self.order_repo = order_repo
    self._next_order_id = 1

  def create_order(self, order_id, items):
    """ items = list of tuples: (product_id, quantity)
    Example: [(1, 2), (2, 1)]"""

    # Cannot create an order with no items
    if not items_data:
      raise ValueError("Order must have one item.")

    order = Order(self._next_order_id)
    self._next_order_id += 1

    # Loop through each requested item
    for product_id, quantity in items:
      
      # Quantity must be greater than 0
      if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
      
      product = self.product_repo.get(product_id)

      # Product must exist
      if product is None:
        raise ValueError(f"Product with ID {product_id} does not exist.")
       
        # Create OrderItem and add to order
        order_item = OrderItem(product, quantity)
        order.add_item(order_item)

    # Save the order
    self.order_repo.save(order)
    return order
  
def get_order(self, order_id):
  order = self.order_repo.get(order_id)
  if order is None:
    raise ValueError(f"Order {order_id} not found.")
  return order

def get_order_total(self, order_id):
  order = self.get_order(order_id)
  return order.total()
