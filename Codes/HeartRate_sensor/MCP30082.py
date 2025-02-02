# First install spidev:
# Enable SPI (sudo raspi-config)
# $ sudo apt-get update 
# $ sudo apt-get upgrade
# $ sudo apt-get install python-dev
# $ sudo reboot
# $ wget https://github.com/doceme/py-spidev/archive/master.zip 
# $ unzip master.zip
# $ cd py-spidev-master
# $ sudo python setup.py install

from spidev import SpiDev

class MCP3008:
    def __init__(self, bus = 0, device = 0):
        self.bus, self.device = bus, device
        self.spi = SpiDev()
        self.open()

    def open(self):
        self.spi.open(self.bus, self.device)
    
    def read(self, channel = 0):
        adc = self.spi.xfer2([6|(Channel&4)>>2,(Channel&3)<<6,0])
        data = ((adc[1] & 15) << 8) + adc[2]
        return data
            
    def close(self):
        self.spi.close()

