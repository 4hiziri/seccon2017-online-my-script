import sys


def _l(idx, s):
    return s[idx:] + s[:idx]


s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
t = [ [_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]

cipher = "POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9"
k1_len = 14
k2_len = 14


# first seven chars is SECCON{, so I can decrypto key's first seven and last seven.

s.find('S')


def specify_key(plain_char, cipher_char):
    table = t[s.find(plain_char)]

    for i in range(len(s)):
        for j in range(len(s)):
            if table[i][j] == cipher_char:
                return (i, j)


def get_key():
    p = 'SECCON{'
    c = cipher[:7]
    former = ''
    latter = ''

    for p_ch, c_ch in zip(p, c):
        f_i, l_i = specify_key(p_ch, c_ch)
        former += s[f_i]
        latter += s[l_i]

    return (former, latter)

def decrypto(cipher, key):
    k1 = key
    k2 = key[::-1]
    i1 = 0
    i2 = 0
    plain = ''

    for a in cipher:
        for index, table in enumerate(t):
            if table[s.find(k1[i1])][s.find(k2[i2])] == a:
                plain += s[index]
                break
        i1 = (i1 + 1) % len(k1)
        i2 = (i2 + 1) % len(k2)

    return plain

key = 'AAAAAAA_aZ2PK_'
# 'SECCON{Welc0me_to_SECCON_CTF_2017}'
