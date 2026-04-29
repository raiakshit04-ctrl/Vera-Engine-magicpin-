def build_context(input_data):
    merchant = input_data.get("merchant", {})
    trigger = input_data.get("trigger", {})
    customer = input_data.get("customer", {})
    category = input_data.get("category", {})

    # 🔥 Handle trigger (string OR dict)
    if isinstance(trigger, str):
        trigger_type = trigger
    elif isinstance(trigger, dict):
        trigger_type = trigger.get("type", "")
    else:
        trigger_type = ""

    # 🔥 Merchant fields
    identity = merchant.get("identity", {})
    offers = merchant.get("offers", [])
    performance = merchant.get("performance", {})

    merchant_name = identity.get("name", "Your store")

    # 🔥 Category handling
    category_slug = merchant.get("category_slug", "")

    category_map = {
        "restaurants": "restaurants",
        "salon": "salon",
        "gym": "gym",
        "pharmacy": "pharmacy"
    }

    category_name = (
        category.get("name")
        or category_map.get(category_slug, category_slug)
        or "business"
    )

    # 🔥 Offer handling (fallback fixed)
    if offers and isinstance(offers, list):
        offer_text = offers[0].get("title", "")
    else:
        offer_text = ""

    if not offer_text:
        offer_text = f"best {category_name} offers nearby"

    return {
        "merchant_name": merchant_name,
        "category": category_name,
        "offer": offer_text,
        "performance": performance,
        "trigger": trigger_type,
        "customer_segment": customer.get("segment", "")
    }