ef recommend_growth(data: dict) -> list:
    """
    Very basic placeholder recommendation logic.
    Later you can plug in ML models or GPT for smart insights.
    """
    recommendations = []

    if data.get("profit", 0) < 0:
        recommendations.append("Reduce expenses to cut losses.")
    elif data.get("profit", 0) < 50000:
        recommendations.append("Explore digital marketing to boost sales.")
    else:
        recommendations.append("Consider scaling operations to new markets.")

    if data.get("revenue", 0) > 1000000:
        recommendations.append("Look into export opportunities.")

    return recommendations