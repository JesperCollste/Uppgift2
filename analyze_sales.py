import csv
import os
from collections import Counter

def analyze_sales_data(filename):
    products = {}
    quantities = Counter()  # Hur många gånger varje produkt har blivit såld

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row['Product']
            sales = float(row['Sales'])
            
            if product in products:
                products[product] += sales
            else:
                products[product] = sales
            
            # count av alla produkter sålda
            quantities[product] += 1
    
    #TODO: Hitta den mest sålda produkten (TIPS! Använd Counter från collections)
    most_sold_product = quantities.most_common(1)[0]  # (product, count)
    
    # Hitta den mest lukrativa produkten
    most_lucrative_product = max(products, key=products.get)
    
    # Genomsnittlig försäljning per produkt
    average_sales = sum(products.values()) / len(products)

    # printar ut allting 
    print(f"Mest sålda produkt: \"{most_sold_product[0]}\", Antal: {most_sold_product[1]}")  #FIXME: Redovisa mest sålda produkt här
    print(f"Mest lukrativa produkt: \"{most_lucrative_product}\" med försäljning på {products[most_lucrative_product]:,.2f} kr")
    print(f"Genomsnittlig försäljning per produkt: {average_sales:,.2f} kr")


os.system('cls')
analyze_sales_data('sales_data.csv')

