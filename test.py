def calc_disc(total):

    discount = 0

    if total > 5000000:
        discount += (total - 5000000) * 0.35
        total = 5000000

    if total > 2000000:
        discount += (total - 2000000) * 0.30
        total = 2000000

    if total > 1000000:
        discount += (total - 1000000) * 0.20
        total = 1000000

    if total > 500000:
        discount += (total - 500000) * 0.10
        total = 500000

    discount += total * 0.05

    return discount


print(calc_disc(1200000))