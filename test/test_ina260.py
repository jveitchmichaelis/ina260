import pytest
from ina260.controller import Controller

@pytest.fixture
def ina260_controller():
    dev = Controller()
    yield dev


def test_voltage(ina260_controller):
    dev = ina260_controller
    assert dev.voltage() > 0

def test_current(ina260_controller):
    dev = ina260_controller
    assert abs(dev.current()) > 0

def test_power(ina260_controller):
    dev = ina260_controller

    power = dev.power()
    assert abs(dev.power() > 0)

def test_manufacturer_id(ina260_controller):
    dev = ina260_controller

    # Fixed for TI
    assert dev.manufacturer_id() == 0x5449

def test_die_ied(ina260_controller):
    dev = ina260_controller

    device_id, revision_id = dev.die_id()

    assert device_id == 0x227
    assert revision_id == 0
