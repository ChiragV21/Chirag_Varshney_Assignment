def calculate_discount(cart, discounts):
    max_discount = 0
    applied_discount = ""

    # Calculate flat $10 discount
    if cart['subtotal'] > 200 and discounts['flat_10_discount']:
        max_discount = 10
        applied_discount = "flat_10_discount"

    # Calculate bulk 5% discount
    for product in cart['products']:
        if product['quantity'] > 10 and discounts['bulk_5_discount']:
            discount_amount = product['total'] * 0.05
            if discount_amount > max_discount:
                max_discount = discount_amount
                applied_discount = "bulk_5_discount"

    # Calculate bulk 10% discount
    if cart['total_quantity'] > 20 and discounts['bulk_10_discount']:
        discount_amount = cart['subtotal'] * 0.1
        if discount_amount > max_discount:
            max_discount = discount_amount
            applied_discount = "bulk_10_discount"

    # Calculate tiered 50% discount
    if cart['total_quantity'] > 30 and discounts['tiered_50_discount']:
        for product in cart['products']:
            if product['quantity'] > 15:
                discount_amount = product['total'] * 0.5
                if discount_amount > max_discount:
                    max_discount = discount_amount
                    applied_discount = "tiered_50_discount"

    return max_discount, applied_discount


def main():
    products = {
        "Product A": 20,
        "Product B": 40,
        "Product C": 50
    }

    discounts = {
        "flat_10_discount": True,
        "bulk_5_discount": True,
        "bulk_10_discount": True,
        "tiered_50_discount": True
    }

    cart = {'products': [], 'subtotal': 0, 'total_quantity': 0}

    for product_name, price in products.items():
        quantity = int(input(f"Enter the quantity of {product_name}: "))
        is_gift_wrapped = input(f"Is {product_name} wrapped as a gift? (yes/no): ").lower() == 'yes'
        total_amount = quantity * price
        cart['subtotal'] += total_amount
        cart['total_quantity'] += quantity
        cart['products'].append({'name': product_name, 'quantity': quantity, 'total': total_amount, 'gift_wrapped': is_gift_wrapped})

    # Calculate discount
    discount_amount, discount_name = calculate_discount(cart, discounts)

    # Calculate shipping and gift wrap fees
    shipping_fee = (cart['total_quantity'] + 9) // 10 * 5
    gift_wrap_fee = sum(product['quantity'] for product in cart['products'] if product['gift_wrapped']) * 1

    # Calculate total
    total_amount = cart['subtotal'] - discount_amount + shipping_fee + gift_wrap_fee

    # Display details
    print("\nOrder Details:")
    for product in cart['products']:
        print(f"{product['name']} - Quantity: {product['quantity']}, Total: ${product['total']}")
    print(f"\nSubtotal: ${cart['subtotal']}")
    print(f"Discount Applied: {discount_name}, Amount: ${discount_amount}")
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Gift Wrap Fee: ${gift_wrap_fee}")
    print(f"\nTotal: ${total_amount}")


if __name__ == "__main__":
    main()
