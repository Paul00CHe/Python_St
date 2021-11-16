def ff(x):
    """Вычисляет функцию.
    >>> ff(2)
    32.0
    >>> ff(1)
    5.0
    
    """
    return float(round((x**4+4**x), 3))

import doctest
doctest.testmod()
