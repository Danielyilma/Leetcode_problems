class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = [0] * (n + 1)
        graph = defaultdict(list)
        res = 0

        for time in times:
            graph[time[0]].append((time[1], time[2]))

        heap = [(0, k)]

        while heap:
            time, node = heappop(heap)

            if not visited[node]:
                res = max(res, time)
            
            visited[node] = 1
            for nebr, ti in graph[node]:
                if not visited[nebr]:
                    heappush(heap, (ti + time, nebr))
        
        if sum(visited) != n:
            return -1
        return res

            
