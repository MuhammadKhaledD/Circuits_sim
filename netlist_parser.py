import re

class NetlistParser:
    @staticmethod
    def parse_netlist(filename):
        elements = []
        nodes = set()
        
        with open(filename, 'r') as file:
            for line in file:
                line = line.split('#')[0].strip()
                if not line:
                    continue
                
                parts = line.split()
                if len(parts) < 4:
                    raise ValueError(f"Invalid netlist line: {line}")
                
                element_type = parts[0][0]
                element_name = parts[0]
                node1 = parts[1]
                node2 = parts[2]
                value = float(parts[3])
                
                nodes.update([node1, node2])
                
                if element_type == 'R':
                    elements.append(('resistor', element_name, node1, node2, value))
                elif element_type == 'V':
                    elements.append(('voltage_source', element_name, node1, node2, value))
                elif element_type == 'I':
                    elements.append(('current_source', element_name, node1, node2, value))
                else:
                    raise ValueError(f"Unknown element type: {element_type}")
        
        return list(elements), sorted(list(nodes))