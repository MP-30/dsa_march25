sales_orders = [
    {"order_id": "SO-1", "customer": "Customer A"},
    {"order_id": "SO-2", "customer": "Customer B"},
]
 
itemss = [
    {"order_id": "SO-1", "item": "Item-1"},
    {"order_id": "SO-1", "item": "Item-2"},
    {"order_id": "SO-2", "item": "Item-3"},
]

""" 
[
  {"order_id": "SO-1", "customer": "Customer A", "items": ["Item-1", "Item-2"]},
  {"order_id": "SO-2", "customer": "Customer B", "items": ["Item-3"]}
]
"""
def to_check(sales_orders,items):
    items_by_order = {}
    for entry in items:
        order_id = entry["order_id"]
        item = entry["item"]
        items_by_order.setdefault(order_id, []).append(item)
    print(items_by_order)
    
    merged_orders = []
    for order in sales_orders:
        order_id = order["order_id"]
        merged_order = {
            **order,
            "items": items_by_order.get(order_id, [])
        }
        merged_orders.append(merged_order)
                    
to_check(sales_orders,itemss)
