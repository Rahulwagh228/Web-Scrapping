
collection = {
    '0':'',
    '1':'https://adexusa.com/familia/ceramic-tiles/?catalogo=general'
     }

collection = {}

for i in range(2, 64):
    key = f"{i}"
    value = f"https://adexusa.com/familia/ceramic-tiles/page/{i}/?catalogo=general"
    
    collection.update({key : value})

print(collection)
