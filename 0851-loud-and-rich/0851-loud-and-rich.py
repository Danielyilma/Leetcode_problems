class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()

        maxs = max(quiet)


        res = [quiet.index(maxs)] * len(quiet)
        for edge in richer:
            graph[edge[0]].append(edge[1])
            indegree[edge[1]] += 1
        
        for node in range(len(quiet)):
            if indegree[node] == 0:
                queue.append((node, node))
    
        while queue:
            leng = len(queue)

            for _ in range(leng):
                node, min_node = queue.popleft()

                if quiet[min_node] < quiet[node]:
                    mins = min_node
                else:
                    mins = node

                if quiet[res[node]] > quiet[mins]:
                    res[node] = mins
                else:
                    mins = res[node]

                for nebr in graph[node]:
                    indegree[nebr] -= 1

                    if indegree[nebr] == 0:
                        queue.append((nebr, mins))
                    elif quiet[res[nebr]] > quiet[mins]:
                        res[nebr] = mins
    
        return res          
                
