import random
from abc import ABC, abstractmethod

class DelayTimeGenerator(ABC):
    @abstractmethod
    def get_delay(self):
        pass

class TriangularTimeGenerator(DelayTimeGenerator):
    def get_delay(self):
        return random.triangular(60, 240, 120) # Parameters: range from 1 to 4 with mode 2 hours

class UniformDelayTimeGenerator1(DelayTimeGenerator):
    def get_delay(self):
        return random.uniform(45, 90)  # Parameters: range from 3 to 8

class UniformDelayTimeGenerator2(DelayTimeGenerator):
    def get_delay(self):
        return random.uniform(15, 60)  # Example parameters: range from 6 to 10

class UniformDelayTimeGenerator3(DelayTimeGenerator):
    def get_delay(self):
        return random.uniform(10, 20)  # Example parameters: range from 1 to 7

# Example usage:
generator1 = UniformDelayTimeGenerator1()
generator2 = UniformDelayTimeGenerator2()
generator3 = UniformDelayTimeGenerator3()
generator4 = TriangularTimeGenerator()

# Generate delays using different generators
print("Delay 1:", generator1.get_delay())
print("Delay 2:", generator2.get_delay())
print("Delay 3:", generator3.get_delay())
print("Delay 4:", generator4.get_delay())