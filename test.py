import sys

products_map = {}


def parse_inputs():
    target = sys.stdin.readline().strip()
    for line in sys.stdin:
        parts = line.split(',')
        product_name = parts[0]
        purchase_price = None if parts[1] == "null" else float(parts[1])
        materials = parts[3].strip().split(';') if int(parts[2]) > 0 else []
        products_map[product_name] = (purchase_price, materials)
    return target


def compute_cost(product_name):
    purchase_price, materials = products_map[product_name]

    if not materials:
        return purchase_price

    production_cost = sum([compute_cost(material) for material in materials])

    if purchase_price is None:
        return production_cost
    else:
        return min(purchase_price, production_cost)


if __name__ == "__main__":
    target_product = parse_inputs()
    result = compute_cost(target_product)
    print("{:.2f}".format(result))