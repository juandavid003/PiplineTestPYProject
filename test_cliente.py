# test_cliente.py
import pytest
from cliente import Cliente

def test_cliente_creation():
    """Test para verificar que un cliente se crea correctamente."""
    cliente = Cliente("1", "Juan Pérez", "juan@email.com", "Madrid", 30)
    assert cliente.id == "1"
    assert cliente.nombre == "Juan Pérez"
    assert cliente.email == "juan@email.com"
    assert cliente.ciudad == "Madrid"
    assert cliente.edad == 30

def test_cliente_invalid_email():
    """Test para verificar que se lance un error con un email inválido."""
    with pytest.raises(ValueError):
        Cliente("2", "Ana García", "ana-email.com", "Barcelona", 25)

def test_cliente_empty_name():
    """Test para verificar que se lance un error si el nombre está vacío."""
    with pytest.raises(ValueError):
        Cliente("3", "", "ana@email.com", "Madrid", 25)
