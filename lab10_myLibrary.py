from math import ceil

def displayIntro ():
    print("Hi")

def sales_price_calc (purchase_price):
    purchase_price = float(purchase_price) # Converts the purchase price to a float

    #Dislplay calculation intro
    print("\nSales Price Calculator:")

    # Ask for a product name (adds interaction)
    product_name = input("Enter the product name: ")

# Calculates the sale price of an item given the purchase price
# it will add 15% of operating costs to the purchase price
# and add 30% profit to the purchase price
# and return the sale price
    operating_costs = purchase_price * 0.15
    profit = purchase_price * 0.30
    sale_price = purchase_price + operating_costs + profit

    print(f"\nProduct Name: {product_name}")
    print(f"\nSales Price Calculation:")
    print(f"Purchase Price: ${purchase_price:.2f}") #{:.2f} formats the float to 2 decimal places
    print(f"Operating Costs (15%): ${operating_costs:.2f}")
    print(f"Profit (30%): ${profit:.2f}")
    print(f"Sale Price: ${ceil(sale_price):.2f}") # ceil rounds up to the nearest whole number
    return sale_price
