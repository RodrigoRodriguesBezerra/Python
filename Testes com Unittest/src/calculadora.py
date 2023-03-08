def soma(x, y):
    # Garante que x e y serão int ou float
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'

    return x + y


def subtrai(x, y):
    # Garante que x e y serão int ou float
    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'

    return x - y
