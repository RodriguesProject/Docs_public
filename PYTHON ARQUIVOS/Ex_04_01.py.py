hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Rate:")
r = float(rte)

def computepay(h, r):
    if h > 40:
        extra_h = h - 40
        return (40 * r) + (extra_h * r * 1.5)
    else:
        return h * r
p = computepay(h, r)

print("Pay", p)
