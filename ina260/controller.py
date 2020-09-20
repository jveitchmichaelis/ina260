from smbus2 import SMBus
import struct

PCA_AUTOINCREMENT_OFF = 0x00
PCA_AUTOINCREMENT_ALL = 0x80
PCA_AUTOINCREMENT_INDIVIDUAL = 0xA0
PCA_AUTOINCREMENT_CONTROL = 0xC0
PCA_AUTOINCREMENT_CONTROL_GLOBAL = 0xE0

REG_CONFIG = 0x00
REG_CURRENT = 0x01
REG_BUS_VOLTAGE = 0x02
REG_POWER = 0x03
REG_MASK_ENABLE = 0x06
REG_ALERT = 0x07
REG_MANUFACTURER_ID = 0xFE
REG_DIE_ID = 0xFF

RST = 15
AVG2 = 11
AVG1 = 10
AVG0 = 9
VBUSCT2 = 8
VBUSCT1 = 7
VBUSCT0 = 6
ISHCT2 = 5
ISHCT1 = 4
ISHCT0 = 3
MODE3 = 2
MODE2 = 1
MODE1 = 0

OCL = 15
UCL = 14
BOL = 13
BUL = 12
POL = 11
CNVR = 10
AFF = 4
CVRF = 3
OVF = 2
APOL = 1
LEN = 0

class Controller:

    def __init__(self, address=0x40, channel=1):
        self.i2c_channel = channel
        self.bus = SMBus(self.i2c_channel)
        self.address = address

    def _read(self, reg):
        """
        Read a word from the device
        
        Parameters
        ---------
            reg: register address

        Returns
        ------
            list of bytes as characters for struct unpack

        """
        res = self.bus.read_i2c_block_data(self.address, reg, 2)
        return bytearray(res)

    def voltage(self):
        """
        Returns the bus voltage in Volts

        """
        voltage = struct.unpack('>H', self._read(REG_BUS_VOLTAGE))[0]
        voltage *= 0.00125 # 1.25mv/bit

        return voltage

    def current(self):
        """
        Returns the current in Amps

        """
        current = struct.unpack('>H', self._read(REG_CURRENT))[0]

        # Fix 2's complement
        if current & (1 << 15):
            current -= 65535

        current *= 0.00125 # 1.25mA/bit

        return current

    def power(self):
        """
        Returns the power calculated by the device in Watts

        This will probably be different to reading voltage and current
        and performing the calculation manually.
        """
        
        power = struct.unpack('>H', self._read(REG_POWER))[0]
        power *= 0.01 # 10mW/bit

        return power

    def manufacturer_id(self):
        """
        Returns the manufacturer ID - should always be 0x5449

        """
        man_id = struct.unpack('>H', self._read(REG_MANUFACTURER_ID))[0]
        return man_id


    def die_id(self):
        """
        Returns a tuple containing the die ID and revision - should be 0x227 and 0x0.
        """
        die_id = struct.unpack('>H', self._read(REG_DIE_ID))[0]
        return (die_id >> 4), (die_id & 0x000F)

    def __del__(self):
        self.bus.close()
