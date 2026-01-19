from netlist_parser import NetlistParser
from nodal_analysis import NodalAnalysis
from mesh_analysis import MeshAnalysis

class CircuitSolver:
    @classmethod
    def solve(cls, netlist_file, method='nodal'):
        elements, nodes = NetlistParser.parse_netlist(netlist_file)
        
        if method.lower() == 'nodal':
            return NodalAnalysis.solve(elements, nodes)
        elif method.lower() == 'mesh':
            return MeshAnalysis.solve(elements, nodes)
        else:
            raise ValueError(f"Unsupported analysis method: {method}")