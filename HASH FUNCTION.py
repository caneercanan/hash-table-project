import random


def custom_hash(item_name, table_size):
    return sum(ord(char) for char in item_name) % table_size


items = [f"Item_{i}" for i in range(1, 101)]  
prices = [round(random.uniform(5, 500), 2) for _ in range(100)]  


hash_table_size = 100
price_list = [None] * hash_table_size  


def build_price_list(items, prices, table_size):
    for i in range(len(items)):
        item = items[i]
        price = prices[i]
        hash_index = custom_hash(item, table_size)
        
      
        while price_list[hash_index] is not None:
            hash_index = (hash_index + 1) % table_size 
        
        price_list[hash_index] = (item, price)


build_price_list(items, prices, hash_table_size)


for index, entry in enumerate(price_list):
    if entry:
        print(f"Hash Index: {index}, Item: {entry[0]}, Price: {entry[1]}TL")
