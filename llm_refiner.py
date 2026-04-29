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

    # 🔥 Add urgency punch
    if decision == "urgency_push":
        if "midnight" not in message.lower():
            message += " Hurry, ends tonight!"

    # 🎉 Make seasonal more exciting
    if decision == "seasonal_campaign":
        message = message.replace("!", "!! 🎉")

    # 📉 Improve performance tone
    if decision == "performance_boost":
        message = message.replace("Try promoting", "Boost sales with")

    # 👋 Make reactivation more human
    if decision == "reactivation":
        message = message.replace("We miss you!", f"We miss you at {name}!")

    # ✨ General polish
    message = message.replace("  ", " ")
    message = message.strip()

    return message