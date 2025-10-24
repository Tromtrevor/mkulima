# Dummy crop data (KES values)
CROP_DATA = {
    "maize": {
        "market_price": 35000,              # per ton
        "seed_cost_per_acre": 3000,
        "fertilizer_cost_per_acre": 5000,
        "labor_cost_per_acre": 10000,     # tons per acre
    },
    "beans": {
        "market_price": 35000,
        "seed_cost_per_acre": 2500,
        "fertilizer_cost_per_acre": 6000,
        "labor_cost_per_acre": 8000,
    },
    "potato": {
        "market_price": 45000,
        "seed_cost_per_acre": 9000,
        "fertilizer_cost_per_acre": 10000,
        "labor_cost_per_acre": 12000,
    },
    "tomatoes": {
        "market_price": 60000,
        "seed_cost_per_acre": 12000,
        "fertilizer_cost_per_acre": 15000,
        "labor_cost_per_acre": 18000,
    },
    "sorghum": {
        "market_price": 30000,
        "seed_cost_per_acre": 2000,
        "fertilizer_cost_per_acre": 4000,
        "labor_cost_per_acre": 6000,
    },
    "wheat": {
        "market_price": 40000,
        "seed_cost_per_acre": 4000,
        "fertilizer_cost_per_acre": 9000,
        "labor_cost_per_acre": 11000,
    },
    "rice": {
        "market_price": 50000,
        "seed_cost_per_acre": 7000,
        "fertilizer_cost_per_acre": 12000,
        "labor_cost_per_acre": 15000,
    },
    "cabbage": {
        "market_price": 30000,
        "seed_cost_per_acre": 5000,
        "fertilizer_cost_per_acre": 8000,
        "labor_cost_per_acre": 10000,
    },
    "onions": {
        "market_price": 65000,
        "seed_cost_per_acre": 8000,
        "fertilizer_cost_per_acre": 12000,
        "labor_cost_per_acre": 15000,
    }
}


def calculate_profit(crop_name, land_size_acres, predicted_yield):
    crop = CROP_DATA.get(crop_name.lower())
    if not crop:
        return None

    total_yield = predicted_yield * land_size_acres
    total_revenue = total_yield * crop["market_price"]
    total_cost = (crop["seed_cost_per_acre"] +
                  crop["fertilizer_cost_per_acre"] +
                  crop["labor_cost_per_acre"]) * land_size_acres
    total_profit = total_revenue - total_cost

    return {
        "total_yield": total_yield,
        "total_revenue": total_revenue,
        "total_cost": total_cost,
        "total_profit": total_profit
    }