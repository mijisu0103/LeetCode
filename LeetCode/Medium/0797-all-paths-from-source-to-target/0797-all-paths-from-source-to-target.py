class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1
        results = []

        def backtrack(curr_node, path):

            if curr_node == target:
                results.append(list(path))
                return

            for next_node in graph[curr_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()

        path = [0]
        backtrack(0, path)

        return results