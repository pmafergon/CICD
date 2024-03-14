def dividir(a, b):
    return a / b


if __name__ == "__main__":
    try:
        print(dividir(5, 3))
    except ZeroDivisionError:
        print("¡No es posible dividir entre cero!")