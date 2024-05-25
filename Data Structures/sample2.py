"""current = self.head
while current!=None:
    if current == current.next:
        current.next = -1
    current = current.next


for i in range(len(s1)):
    if i==s1[(len(s1)//2)-1]:
        s2.push(i)"""


class Graph:

    def __init__(self,edges):

        self.edges = edges
        self.graph_dict = {}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)

    def get_paths(self, start,end, visited=[],total=[]):

        if start in self.graph_dict:
            for child in self.graph_dict[start]:

                if child==end :
                    visited.append(child)
                    total.append(visited)



                else:
                    visited.append(child)
                    self.get_paths(child,end,visited,total)


                visited = []
        return total,len(total)

    def total_paths(self,start,end):
        pass










routes = [("Mumbai","Delhi"),
          ("Mumbai","Manali"),
          ("Kochi","Pune"),
          ("Pune","Mumbai"),
          ("Kochi","Banglore"),
          ("Banglore","Chennai"),
          ("Chennai","Mumbai"),
          ("Chennai","Hyderabad"),
          ("Hyderabad","Pune")]


map_1  = Graph(routes)
# map_1.total_paths("Kochi","Banglore")


y = map_1.get_paths("Kochi","Mumbai")
print(y)
