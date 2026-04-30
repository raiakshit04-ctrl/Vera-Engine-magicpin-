def generate_message(context, decision, reason):
    name = context["merchant_name"]
    category = context["category"]
    offer = context["offer"]
    trigger = context.get("trigger", "").lower()

    category_lower = category.lower()

    if "restaurant" in category_lower:
        hook = "🍽️ Drive more orders"
    elif "salon" in category_lower:
        hook = "💇 Boost appointments"
    elif "gym" in category_lower:
        hook = "🏋️ Increase memberships"
    elif "pharmacy" in category_lower:
        hook = "💊 Improve repeat purchases"
    else:
        hook = "📈 Grow your business"

    extra_line = ""

    if "festival" in trigger:
        extra_line = "🎉 Festival demand is rising right now.\n\n"
    elif "appointment" in trigger:
        extra_line = "📅 You already have customer activity scheduled.\n\n"
    elif "competitor" in trigger:
        extra_line = "⚠️ A competitor is actively attracting customers nearby.\n\n"
    elif "recall" in trigger or "due" in trigger:
        extra_line = "🔁 Customers are due for a follow-up.\n\n"
    cta = "👉 Want me to push this offer to nearby customers?"

    if decision == "performance_boost":
        return (
            f"📉 Quick update for *{name}*\n\n"
            f"{extra_line}"
            f"{hook} using:\n👉 {offer}\n\n"
            f"{reason.capitalize()}.\n\n"
            f"🚀 Running this now can help recover momentum.\n\n"
            f"{cta}"
        )

    if decision == "seasonal_campaign":
        return (
            f"🎉 Great timing for *{name}*\n\n"
            f"{extra_line}"
            f"{hook} with:\n👉 {offer}\n\n"
            f"{reason.capitalize()}.\n\n"
            f"📈 Customers are actively searching right now.\n\n"
            f"{cta}"
        )

    if decision == "urgency_push":
        return (
            f"🔥 Don’t miss this for *{name}*\n\n"
            f"{extra_line}"
            f"{hook} using:\n👉 {offer}\n\n"
            f"{reason.capitalize()}.\n\n"
            f"⏳ Push this immediately before it expires.\n\n"
            f"{cta}"
        )

    if decision == "reactivation":
        return (
            f"👋 Bring customers back to *{name}*\n\n"
            f"{extra_line}"
            f"{hook} with:\n👉 {offer}\n\n"
            f"{reason.capitalize()}.\n\n"
            f"💡 A simple reminder can drive repeat visits.\n\n"
            f"{cta}"
        )

    return (
        f"📢 Quick insight for *{name}*\n\n"
        f"{extra_line}"
        f"{hook} using:\n👉 {offer}\n\n"
        f"{reason.capitalize()}.\n\n"
        f"📢 Staying active helps maintain visibility.\n\n"
        f"{cta}"
    )
