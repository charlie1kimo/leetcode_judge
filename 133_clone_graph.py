"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""
# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution(object):
    """
    Idea:
        - use a queue to BFS, and keep a visited_map
        - visited_map is essentially the new graph, stores:
            key: label
            value: new node
        - return visited_map[node.label]
    """
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node is None:
            return None

        visited_map = dict()
        queue = [node]

        while len(queue) > 0:
            curr = queue.pop(0)
            if curr.label not in visited_map:
                visited_map[curr.label] = UndirectedGraphNode(curr.label)

            for neighbor in curr.neighbors:
                if neighbor.label not in visited_map:
                    queue.append(neighbor)
                    visited_map[neighbor.label] = UndirectedGraphNode(neighbor.label)

                visited_map[curr.label].neighbors.append(visited_map[neighbor.label])

        return visited_map[node.label]
