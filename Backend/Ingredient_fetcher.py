import requests

def get_ingredients(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    data = response.json()
    
    if data["status"] == 1:
        product = data["product"]
        name = product.get("product_name", "Unknown Product")
        ingredients = product.get("ingredients_text", "Ingredients not available")
        return {
            "product_name": name,
            "ingredients": ingredients
        }
    else:
        return {"error": "Product not found"}

# Test it
barcode = "3017620422003"
result = get_ingredients(barcode)
print(result)
