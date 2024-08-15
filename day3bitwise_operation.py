def bit(a,b):
    m=a & b
    print(f'{a} & {b},result={m},bitwise and operation')

    m=a | b
    print(f'{a} | {b},result={m},bitwise or operation')

    m=a^b
    print(f'{a} & {b},result={m},bitwise xor operation')

    m=~a
    m=~b
    print(f'{~a} result={m},bitwise not operation')
    print(f'{~b},result={m},bitwise not operation')

    m=a << 2
    print(f'{a<<2}result={m},bitwise and operation')
    m=b>>2
    print(f'{b>>2},result={m},bitwise and operation')
r=bit(10,4)
