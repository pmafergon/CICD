def dividir(a, b):
    try:
        a / b
        return a / b
    except ZeroDivisionError:
        return ("¡No es posible dividir entre cero!")
        


if __name__ == "__main__":

    print(dividir(5, 3))