"""📖 [Python上でGraphvizを使って綺麗なグラフを描く](https://programgenjin.hatenablog.com/entry/2019/02/26/075121)"""

from graphviz import Graph

g = Graph(format="png")

g.attr('node', shape='circle')

with g.subgraph(name='cluster_root') as c:
    c.attr(color='white', label='root')   # デフォルトではgraphに適用される
    c.node('0')
    c.edges([('0', '1'), ('0', '2')])

with g.subgraph(name='cluster_0') as c:
    c.attr(color='blue')
    c.edges([('1', '3'), ('1', '4')])
    with c.subgraph(name='cluster_00') as cc0:
        cc0.attr(color='darkgreen')
        cc0.node('3')
    with c.subgraph(name='cluster_01') as cc1:
        cc1.attr('graph', color='darkgreen')
        cc1.node('4')

with g.subgraph(name='cluster_1') as c:
    c.attr(color='blue')
    c.edges([('2', '5'), ('2', '6')])
    with c.subgraph(name='cluster_10') as cc0:
        cc0.attr(color='darkgreen')
        cc0.node('5')
    with c.subgraph(name='cluster_11') as cc1:
        cc1.attr(color='darkgreen')
        cc1.edges([('6', '7'), ('6', '8')])
        with cc1.subgraph(name='cluster_110') as ccc0:
            ccc0.attr(color='red')
            ccc0.node('7')
        with cc1.subgraph(name='cluster_111') as ccc1:
            ccc1.attr(color='red')
            ccc1.node('8')


# g.view()
g.render("graphs")
