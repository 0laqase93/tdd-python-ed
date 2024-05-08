# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import multiplicacion

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class MultiplicacionTestClass:

    # Test para la operación suma
    def test_multiplicacion(self):
        assert multiplicacion(4,5) == 20
        assert multiplicacion(-1,-2) == 2
        assert multiplicacion(-7,5) == -35
        assert multiplicacion(-7,9) == -63
