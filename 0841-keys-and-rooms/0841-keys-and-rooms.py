class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = [0] * (len(rooms))
        visited[0] = 1

        for i, keys in enumerate(rooms):
            graph[i].extend(keys)

        def dfs(room):

            for room_key in graph[room]:

                if not visited[room_key]:
                    visited[room_key] = 1
                    dfs(room_key)
        
        dfs(0)
        return sum(visited) == (len(rooms))
                
