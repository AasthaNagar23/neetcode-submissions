class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*(numCourses)
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course]+=1
        queue=[]
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        result=[]
        while queue:
            course=queue.pop(0)
            result.append(course)
            for i in graph[course]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        if len(result)!=numCourses:
            return []
        return result
