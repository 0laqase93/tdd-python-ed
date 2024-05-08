# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import division

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_division(self):
        assert division(5,5) == 1.0
        assert division(-1,-2) == 0.5
        assert division(-7,14) == -0.5
        assert division(-18,9) == -2.0
