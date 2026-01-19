from circuit_solver import CircuitSolver
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <netlist_file> <analysis_method>")
        print("Analysis methods: nodal, mesh")
        sys.exit(1)
    
    netlist_file = sys.argv[1]
    method = sys.argv[2]
    
    try:
        results = CircuitSolver.solve(netlist_file, method)
        
        print(f"\nCircuit Analysis Results ({method.upper()} Analysis):")
        for key, value in results.items():
            print(f"{key}: {value}")
    
    except Exception as e:
        print(f"Error solving circuit: {e}")

if __name__ == "__main__":
    main()