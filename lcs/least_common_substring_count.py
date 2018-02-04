def lcs(x, y, a, b):
    if a == 0 or b == 0:
        return 0
    if x[a-1] == y[b -1]:
        return 1 + lcs(x, y, a-1, b-1)
    else:
        return max(lcs(x, y, a, b-1), lcs(x, y, a-1, b))

if __name__ == "__main__":
    x = "abcdefg"
    y = "xayczd"
    print lcs(x, y, len(x), len(y))
