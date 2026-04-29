import json
from main import run_engine
from data_loader import MERCHANTS, TRIGGERS, CUSTOMERS, CATEGORIES


def normalize_data(data):
    # Case 1: wrapped dict
    if isinstance(data, dict):
        if "data" in data:
            data = data["data"]
        else:
            data = list(data.values())

    # Case 2: nested list like [[...]]
    if isinstance(data, list) and len(data) == 1 and isinstance(data[0], list):
        data = data[0]

    return data


def run_batch(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    data = normalize_data(data)

    print("Total items:", len(data))

    results = []

    for item in data:
    # rest of your logic (temporarily ignored because of break)
        # 🔥 Skip invalid entries
        if not isinstance(item, dict):
            continue

        merchant = MERCHANTS.get(item.get("merchant_id"), {})
        trigger = TRIGGERS.get(item.get("trigger_id"), {})
        customer = (
            CUSTOMERS.get(item.get("customer_id"), {})
            if item.get("customer_id")
            else {}
        )

        category_id = merchant.get("category_id")
        category = CATEGORIES.get(category_id, {})

        input_data = {
            "merchant": merchant,
            "trigger": trigger,
            "customer": customer,
            "category": category,
        }

        output = run_engine(input_data)
        results.append(output)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"✅ Results saved to {output_file}")


if __name__ == "__main__":
    run_batch("dataset/expanded/test_pairs.json", "output.json")