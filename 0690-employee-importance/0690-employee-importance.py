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
        graph = defaultdict(set)

        for emp in employees:
            graph[emp.id] = emp

        
        def dfs(employee):
            sums = 0

            for emp_id in employee.subordinates:
                sums += dfs(graph[emp_id])
            
            return sums + employee.importance
        
        return dfs(graph[id])
        
         