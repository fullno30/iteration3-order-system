from domain.order import Order
from domain.order_item import OrderItem

class OrderService:
  def __init__(self, product_repo, order_repo):
    self.product_repo = product_repo
    self.order_repo = order_repo

  def create_order(self, order_id, items):
    """ items = list of tuples: (product_id, quantity)
    Example: [(1, 2), (2, 1)]"""

    # Create the order
    order = Order(order_id)

    # Loop through each requested item
    for product_id, quantity in items:
      product = self.product_repo.get(product_id)
      
      # Validate product exists
      if product is None:
        raise ValueError(f"Product with ID {product_id} does not exist.")
        # Create OrderItem and add to order
        order_item = OrderItem(product, quantity)
        order.add_item(order_item)

    # Save the order
    self.order_repo.save(order)

    return order
