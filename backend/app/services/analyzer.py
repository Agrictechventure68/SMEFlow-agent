def analyze_data(data: dict) -> dict:
    """
    Very basic SME data analysis (placeholder for AI/ML).
    Later you can integrate Pandas, scikit-learn, etc.
    """
    revenue = data.get("revenue", 0)
    expenses = data.get("expenses", 0)
    profit = revenue - expenses

    return {
        "revenue": revenue,
        "expenses": expenses,
        "profit": profit,
        "profit_margin": round((profit / revenue) * 100, 2) if revenue else 0
    }