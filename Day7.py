class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emps = {emp.id: emp for emp in employees}
        total = 0
        stack = [id]

        while stack:
            cur = stack.pop()
            emp = emps.get(cur)
            if not emp:
                continue
            total += emp.importance
            # push subordinates to stack
            for s in emp.subordinates:
                stack.append(s)

        return total
