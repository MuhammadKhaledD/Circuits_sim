import numpy as np

class MeshAnalysis:
    @staticmethod
    def solve(elements, nodes):
        meshes = []
        processed_elements = set()
        
        for i, (elem_type1, name1, node1a, node1b, value1) in enumerate(elements):
            if name1 in processed_elements:
                continue
            
            mesh = [i]
            processed_elements.add(name1)
            
            for j, (elem_type2, name2, node2a, node2b, value2) in enumerate(elements):
                if j == i or name2 in processed_elements:
                    continue
                
                if (node1a == node2a or node1a == node2b or 
                    node1b == node2a or node1b == node2b):
                    mesh.append(j)
                    processed_elements.add(name2)
            
            meshes.append(mesh)
        
        num_meshes = len(meshes)
        Z = np.zeros((num_meshes, num_meshes))
        V = np.zeros(num_meshes)
        
        for i, mesh in enumerate(meshes):
            for elem_idx in mesh:
                elem_type, name, node1, node2, value = elements[elem_idx]
                
                if elem_type == 'resistor':
                    Z[i, i] += value
                
                elif elem_type == 'voltage_source':
                    V[i] += value
        
        mesh_currents = np.linalg.solve(Z, V)
        
        results = {f'Mesh {i+1}': current for i, current in enumerate(mesh_currents)}
        return results