import sys

# python this.py SECCON{**************************} **************


def _l(idx, s):
    return s[idx:] + s[:idx]


# k1 = 34
# k2 = 14
def main(p, k1, k2):
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"

    t = [ [_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]

    i1 = 0
    i2 = 0
    c = ""

    for a in p:
        c += t[s.find(a)][s.find(k1[i1])][s.find(k2[i2])]
        i1 = (i1 + 1) % len(k1)
        i2 = (i2 + 1) % len(k2)

    return c


print main(sys.argv[1], sys.argv[2], sys.argv[2][::-1])