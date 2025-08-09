class FondosInsuficientesError(Exception):
    pass
def cajero_automatico():
    saldo = 1500  # Saldo inicial
    print(f"Saldo disponible: {saldo}")
    while True:
        try:
            monto = float(input("Ingrese el monto a retirar: "))
            if monto > saldo:
                raise FondosInsuficientesError("No hay fondos suficientes.")
            if monto > 1000:
                raise Exception("El monto excede el límite permitido por transacción.")
            saldo = saldo - monto
            print(f"Retiro exitoso. Saldo restante: {saldo}")
        except FondosInsuficientesError as e:
            print("Error:", e)
        except Exception as e:
            print("Error inesperado:", e)
cajero_automatico()