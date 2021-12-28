def countPathsUtil(u, d,
					visited, count, adjList):
		visited[u] = True

		# If current vertex is same as
		# destination, then increment count
		if (u == d):
			count += 1

		# If current vertex is not destination
		else:

			# Recur for all the vertices
			# adjacent to current vertex
			i = 0
			while i < len(adjList[u]):
				if (not visited[adjList[u][i]]):
					countPathsUtil(adjList[u][i], d,
										visited, pathCount, adjList)
				i += 1

		visited[u] = False

def solution():
    f = open("day12/12.txt","r")
    edges = []
    adjList = {}
    for line in f:
        edges.append(line.rstrip().split("-"))
    for edge in edges:
        if edge[0] not in adjList.keys(): adjList[edge[0]] = []
        adjList[edge[0]].append(edge[1])
    visited = [False] * len(adjList)
    pathCount = [0]
	countPathsUtil(start, end, visited, pathCount)
    return pathCount[0]

# Python 3 program to count all paths
# from a source to a destination.

# A directed graph using adjacency
# list representation


class Graph:

	def __init__(self, V):
		self.V = V
		self.adj = [[] for i in range(V)]

	def addEdge(self, u, v):

		# Add v to u’s list.
		self.adj[u].append(v)

	# Returns count of paths from 's' to 'd'
	def countPaths(self, s, d):

		# Mark all the vertices
		# as not visited
		visited = [False] * self.V

		# Call the recursive helper
		# function to print all paths
		pathCount = [0]
		self.countPathsUtil(s, d, visited, pathCount)
		return pathCount[0]

	# A recursive function to print all paths
	# from 'u' to 'd'. visited[] keeps track
	# of vertices in current path. path[]
	# stores actual vertices and path_index
	# is current index in path[]
	


# Driver Code
if __name__ == '__main__':

	# Create a graph given in the
	# above diagram
	g = Graph(4)
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(0, 3)
	g.addEdge(2, 0)
	g.addEdge(2, 1)
	g.addEdge(1, 3)

	s = 2
	d = 3
	print(g.countPaths(s, d))

# This code is contributed by PranchalK

solution()