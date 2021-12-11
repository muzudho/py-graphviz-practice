from graphviz import Digraph

g = Digraph(format="png")
g.attr("node", shape="square", style="filled")
g.edge("start", "state1", label="0.8")
g.edge("start", "state2", label="0.2")
g.edge("state1", "state1", label="0.5")
g.edge("state2", "state2", label="0.8")
g.edge("state1", "state2", label="0.5")
g.edge("state2", "end", label="0.2")
g.edge("end", "count", label="1.0")
g.edge("count", "start", label="1.0")
g.node("start", shape="circle", color="pink")
g.render("graphs")

"""
from graphviz import Graph
from graphviz import Digraph

g = Graph(format='png')
dg = Digraph(format='png')

# 無向グラフ
# nodeを追加
g.node('1')
g.node('2')
g.node('3')
# edgeを追加
g.edge('1', '2')
g.edge('2', '3')
g.edge('3', '1')

# 有向グラフ
dg.node('1')
dg.node('2')
dg.node('3')
dg.edge('1', '2')  # 1 -> 2
dg.edge('2', '3')  # 2 -> 3
dg.edge('3', '1')  # 3 -> 1

g.render('./graph', view=True)
dg.render('./dgraph', view=True)

g = Graph()

g.edge('1', '2')
g.edge('2', '3')
g.edge('3', '1')

g.view()
"""
