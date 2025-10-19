class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = [0] * (len(rooms))

        for i, room in enumerate(rooms):
            graph[i].extend(room)

        queue = deque([0])

        while queue:
            leng = len(queue)

            for _ in range(leng):
                room = queue.popleft()
                visited[room] = 1
            
                for room_keys in graph[room]:
                    if not visited[room_keys]:
                        queue.append(room_keys)
        
        return sum(visited) == len(rooms)
                
