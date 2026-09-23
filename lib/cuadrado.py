def get_area(lado:int) -> int:
    return lado**2 if isinstance(lado, int) else None

def get_identificador() -> str:
    return 'cuadrado'