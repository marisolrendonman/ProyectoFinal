class NotaInvalidaError(Exception):
    def __init__(self, mensaje="La nota debe estar entre 0 y 5"):
        super().__init__(mensaje)