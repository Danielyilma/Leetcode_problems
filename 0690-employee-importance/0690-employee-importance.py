"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {}
        weight = defaultdict(int)
        visited = set()

        for emp in employees:
            graph[emp.id] = emp
            weight[emp.id] = emp.importance
        
        # print(graph)
        


        def dfs(emp):
            sums = 0
            for emp_id in emp.subordinates:
                sums += dfs(graph[emp_id])
                
            return emp.importance + sums

        for emp in employees:
            if emp.id == id:
                return dfs(emp)


