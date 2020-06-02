from ina260.controller import Controller

if __name__ == "__main__":
    c = Controller()

    print("Bus voltage: {} V").format(c.voltage())
    print("Bus current: {} A").format(c.current())
    print("Bus power: {} W").format(c.power())
