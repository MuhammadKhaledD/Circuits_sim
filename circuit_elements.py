class CircuitElement:
    def __init__(self, name, node1, node2, value):
        self.name = name
        self.node1 = node1
        self.node2 = node2
        self.value = value

class Resistor(CircuitElement):
    def __init__(self, name, node1, node2, resistance):
        super().__init__(name, node1, node2, resistance)
        self.resistance = resistance

class VoltageSource(CircuitElement):
    def __init__(self, name, node1, node2, voltage):
        super().__init__(name, node1, node2, voltage)
        self.voltage = voltage

class CurrentSource(CircuitElement):
    def __init__(self, name, node1, node2, current):
        super().__init__(name, node1, node2, current)
        self.current = current