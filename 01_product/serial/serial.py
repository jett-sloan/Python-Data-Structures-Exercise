class SerialGenerator:
    def __init__(self, start_number):
        self.serial_number = start_number
        self.start_number = start_number

    def __repr__(self):
        return f"<SerialGenerator start={self.serial_number} next={self.serial_number + 1}>"

    def generate(self):
        self.serial_number += 1
    def reset(self):
        self.serial_number = self.start_number
    

# Creating an instance of SerialGenerator
serial = SerialGenerator(start_number=100)

# Generating a new serial number
serial.generate()
serial.generate()
serial.generate()
serial.reset()




# Printing the updated representation of the object
print(serial)  # Output: <SerialGenerator start=101 next=102>
