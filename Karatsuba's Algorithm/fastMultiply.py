def fastMultiply(a, b):
    from math import log10

    if (a < 10 or b < 10):
        return a * b

    n = max(int(log10(a) + 1), int(log10(b) + 1))
    mid = n // 2

    aL = a // pow(10, mid)
    aR = a % pow(10, mid)
    bL = b // pow(10, mid)
    bR = b % pow(10, mid)

    x1 = fastMultiply(aL, bL)
    x2 = fastMultiply(aR, bR)
    x3 = fastMultiply(aL + aR, bL + bR)

    return x1 * pow(10, 2 * mid) + (x3 - x1 - x2) * pow(10, mid) + x2

if __name__ == "__main__":
    num1 = 248964532246092369
    num2 = 1327683564561938302938

    product = fastMultiply(num1, num2)
    print(f"{product}")