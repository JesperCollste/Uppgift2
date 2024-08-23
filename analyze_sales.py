import csv
import os
import locale
from collections import Counter

def analyze_sales_data(filename):
    products = {}
    quantities = Counter()  # To keep track of the number of times each product is sold

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row['Product']
            sales = float(row['Sales'])
            
            # Track total sales per product
            if product in products:
                products[product] += sales
            else:
                products[product] = sales
            
            # Track the count of each product sold
            quantities[product] += 1
    
    
    most_sold_product = quantities.most_common(1)[0]  # (product, count)
    
   
    most_lucrative_product = max(products, key=products.get)
    

    average_sales = sum(products.values()) / len(products)

    print(f"Mest sålda produkt: \"{most_sold_product[0]}\", Antal: {most_sold_product[1]}")
    print(f"Mest lukrativa produkt: \"{most_lucrative_product}\" med försäljning på {locale.currency(products[most_lucrative_product], grouping=True)}")
    print(f"Genomsnittlig försäljning per produkt: {locale.currency(average_sales, grouping=True)}")


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')

os.system('cls')
analyze_sales_data('sales_data.csv')
