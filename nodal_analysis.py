import numpy as np

class NodalAnalysis:
    @staticmethod
    def solve(elements, nodes):
        node_dict = {node: idx for idx, node in enumerate(nodes)}
        num_nodes = len(nodes)
        
        ground_node = node_dict['0']
        
        G = np.zeros((num_nodes, num_nodes))
        I = np.zeros(num_nodes)
        
        for elem_type, name, node1, node2, value in elements:
            n1_idx = node_dict[node1]
            n2_idx = node_dict[node2]
            
            if elem_type == 'resistor':
                conductance = 1 / value
                G[n1_idx, n1_idx] += conductance
                G[n2_idx, n2_idx] += conductance
                G[n1_idx, n2_idx] -= conductance
                G[n2_idx, n1_idx] -= conductance
            
            elif elem_type == 'voltage_source':
                G[n1_idx, n1_idx] += 1
                G[n2_idx, n2_idx] += 1
                I[n1_idx] -= value
                I[n2_idx] += value
            
            elif elem_type == 'current_source':
                I[n1_idx] -= value
                I[n2_idx] += value
        
        non_ground_nodes = [i for i in range(num_nodes) if i != ground_node]
        
        G_reduced = G[non_ground_nodes, :][:, non_ground_nodes]
        I_reduced = I[non_ground_nodes]
        
        V_reduced = np.linalg.solve(G_reduced, I_reduced)
        
        V = np.zeros(num_nodes)
        V[non_ground_nodes] = V_reduced
        
        node_voltages = {nodes[idx]: V[idx] for idx in range(num_nodes)}
        
        return node_voltages