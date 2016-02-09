"""
In a word ladder puzzle you are given the challenge
say of transforming the word "FOOL" into the word "SAGE".  
You must make the change occur gradually by 
changing one letter at a time. 
At each step you must transform one word 
into another word, you are not allowed to 
transform a word into a non-word. 

We want to find the smallest number of 
transformations needed to turn the 
starting word into the ending word.

We do this by representing the relationships 
between the words as a graph and by using 
breadth first search to find an efficient 
path from the starting word to the ending word.
"""


from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def build_graph(word_file):
    d = {}
    g = Graph()
    wfile = open(word_file,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g



def bfs(g, start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')


def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

traverse(g.getVertex('sage'))
