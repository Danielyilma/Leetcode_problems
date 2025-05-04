class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time_heap = []
        time = 0
        heap2 = []

        for i, task in enumerate(tasks):
            heappush(time_heap, (task[0], i))
       
        res = []

        while len(heap2) != 0 or len(time_heap) != 0:

            if len(heap2) == 0:
                time = time_heap[0][0]
            else:
                process = heappop(heap2)
                time += process[0]
                res.append(process[1])

            while len(time_heap) > 0 and time_heap[0][0] <= time:
                t = heappop(time_heap)
                heappush(heap2, (tasks[t[1]][1], t[1]))
        

        return res