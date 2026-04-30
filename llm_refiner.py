def refine_with_llm(message, context, decision):
    """
    Lightweight refinement layer.
    No external API (safe for submission).
    Just improves tone, urgency, and clarity.
    """

    name = context.get("merchant_name", "")
    category = context.get("category", "")
    discount = context.get("discount", "")
    timing = context.get("timing", "")

    if decision == "urgency_push":
        if "midnight" not in message.lower():
            message += " Hurry, ends tonight!"

    if decision == "seasonal_campaign":
        message = message.replace("!", "!! 🎉")

    if decision == "performance_boost":
        message = message.replace("Try promoting", "Boost sales with")

    if decision == "reactivation":
        message = message.replace("We miss you!", f"We miss you at {name}!")

    message = message.replace("  ", " ")
    message = message.strip()

    return message
