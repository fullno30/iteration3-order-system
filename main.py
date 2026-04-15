from domain.product import Product
from repository.product_repo import ProductRepository
from repository.order_repo import OrderRepository
from service.order_service import OrderService

def main():
    # Create repositories
    product_repo = ProductRepository()
    order_repo = OrderRepository()

    # Create products (same as your Iteration 1, just with IDs added)
    mug = Product(1, "Mug", 12.50)
    scarf = Product(2, "Scarf", 25.00)

    # Store products in the repository
    product_repo.add(mug)
    product_repo.add(scarf)

    # Create the service
    service = OrderService(product_repo, order_repo)

    # Create an order (similar to Iteration 2, but using the service)
    order = service.create_order([ (1, 2), # 2 mugs (2, 1), # 1 scarf])

    # Print subtotals (same output style as your Iteration 1)
    for item in order.items:
        print(f"Item: {item.product.name}x{item.quantity} = ${item.subtotal():.2f}")

    # Print total
    print(f"Total = ${order.total():.2f}")


if __name__ == "__main__":
    main()
