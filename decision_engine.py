def decide_message_type(context):
    trigger = context.get("trigger", "").lower()
    performance = context.get("performance", {})
    delta = performance.get("delta_7d", {})

    views = delta.get("views_pct", 0)

    if context.get("customer_segment") == "inactive":
        return "reactivation"

    if "lapsed" in trigger or "inactive" in trigger:
        return "reactivation"

    if "appointment" in trigger or "reminder" in trigger:
        return "reactivation"

    if "recall" in trigger or "due" in trigger:
        return "reactivation"

    if "festival" in trigger or "event" in trigger:
        return "seasonal_campaign"

    if "expiry" in trigger or "deadline" in trigger:
        return "urgency_push"

    if "competitor" in trigger:
        return "performance_boost"

    if views is not None and views < -0.05:
        return "performance_boost"

    return "general_engagement"


def generate_reason(context, decision):
    performance = context.get("performance", {})
    delta = performance.get("delta_7d", {})

    views = delta.get("views_pct")
    calls = delta.get("calls_pct")

    trigger = context.get("trigger", "").lower()

    if decision == "performance_boost":
        if views is not None:
            pct = abs(round(views * 100))
            return f"views dropped by {pct}% in the last 7 days"

        if calls is not None:
            pct = abs(round(calls * 100))
            return f"calls dropped by {pct}% recently"

        return "engagement has declined recently"

    if decision == "seasonal_campaign":
        return "customer demand is rising due to current trends"

    if decision == "urgency_push":
        return "this offer is time-sensitive and needs immediate push"

    if decision == "reactivation":
        return "some customers haven’t visited in a while"

    if "festival" in trigger:
        return "upcoming festive demand can significantly boost customer traffic"

    if "appointment" in trigger:
        return "scheduled appointments create a timely engagement opportunity"

    if "competitor" in trigger:
        return "increased competition makes it important to stay visible"

    if "recall" in trigger or "due" in trigger:
        return "customers are due for follow-up, making this a strong engagement moment"

    return "recent trends suggest a good opportunity to increase visibility"
