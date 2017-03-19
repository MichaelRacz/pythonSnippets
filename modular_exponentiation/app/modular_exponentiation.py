def exponentiate(base, exponent, modulus):
    """
    Return the result of base ** exponent % modulus. The runtime of this
    algorithm is log(n).
    arguments:
    base -- Base value of the exponentiation.
    exponent -- Exponent of the exponentiation. Negative values are not supported.
    modulus -- Modulus of the exponentiation.
    result: base ** exponent % modulus.
    """
    if exponent < 0:
        raise ValueError('Calculating roots is not supported, the exponent must not be negative.')
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = result * base % modulus
            exponent -= 1
        exponent /= 2
        base = (base * base) % modulus
    return result
