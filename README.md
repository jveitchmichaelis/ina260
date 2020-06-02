# INA260 Driver

![coverage](coverage.svg)

## Introduction

This Python package provides a platform agnostic driver for the [TI INA260](https://www.ti.com/product/INA260) precision power monitor. Conveniently, the INA260 has a built-in sense resistor so it's very easy to integrate into your projects. It can sense from 0 to 36V and up to 15A(!) with 16-bit resolution. Thus, it's perfect for pretty much all hobbyist projects.

The only dependency for this library is `smbus2` so provided your I2C device is addressable by that, this library should work (for example on a Raspberry Pi or other dev board).

## Examples

```python

from ina260.controller import Controller

c = Controller()

print(c.voltage())
print(c.current())
print(c.power()))

```

see the example script in the repository. Note that the power measurement is usually not the same as voltage times current unless you read all three registers instantaneously.

## Hardware notes

The chip itself is very easy to hook up (although it comes in a VSSOP package which can be challenging to solder if you've not had much experience with SMD soldering).

Be sure to follow TI's guidelines in the datasheet about proper power planes and PCB layout. The package is designed so that your power rail goes in one side and out the other. Otherwise the chip is very easy to integrate and minimally just needs a standard 0.1uF bypass capacitor.

## Test suite

This package has a comprehensive test suite which you can use to check that commands are being recieved and interpreted properly. You need `pytest`. Run with:

```
python -m pytest test
```

Coverage is 99% because there should also be a check for reverse current which is obviously difficult to do simultaneously with forward current.

