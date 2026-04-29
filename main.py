from decision_engine import decide_message_type, generate_reason
from generator import generate_message
from utils import build_context

def run_engine(input_data):
    context = build_context(input_data)

    decision = decide_message_type(context)
    reason = generate_reason(context, decision)

    message = generate_message(context, decision, reason)

    return {
        "message_type": decision,
        "why_now": reason,
        "message": message
    }


if __name__ == "__main__":
    import json

    with open("sample_input.json", "r") as f:
        data = json.load(f)

    output = run_engine(data)
    print(json.dumps(output, indent=2))