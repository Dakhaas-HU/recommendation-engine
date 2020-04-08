def sort(product):
    return product[12]


def discount_filter(recommendations):
    recommendations.sort(reverse=True, key=sort)
    return recommendations
