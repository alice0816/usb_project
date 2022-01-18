import serial

class USBControl(object):
    def __init__(self, com):
        self.ser = serial.Serial(com, 9600, timeout=3)

    def write(self, chn):
        str = f's {chn}\r'
        self.ser.write(bytes(str, encoding='utf-8'))

if __name__ == "__main__":
    usbCtrl = USBControl('COM10')
    usbCtrl.write('3')



