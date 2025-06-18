class Especialidad:
    DIAS_VALIDOS = {'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'}

    def __init__(self, tipo: str, dias: list[str]):
        dias_lower = [dia.lower() for dia in dias]
        for dia in dias_lower:
            if dia not in self.DIAS_VALIDOS:
                raise ValueError(f"Día inválido: {dia}")
        self.__tipo = tipo
        self.__dias = dias_lower

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in self.__dias

    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"

    @property
    def nombre(self) -> str:
        return self.__tipo

    @property
    def dias_de_atencion(self) -> list[str]:
        return self.__dias
