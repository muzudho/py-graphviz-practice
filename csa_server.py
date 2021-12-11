from graphviz import Digraph

# グラフの設定
g = Digraph(format="png")
g.attr("node", shape="square", style="filled")

# クラスター 'cluster_' から名前を始める必要あり
with g.subgraph(name='cluster_root') as c:
    c.attr(color='white', label='Root')   # デフォルトではgraphに適用される

    # 開始ノード
    c.node("Start", shape="circle", color="pink")

    # 有向な２つのノード
    c.edge("Start", "1", label="Start")

    with c.subgraph(name='cluster_init') as c2:
        c2.attr(color='pink', label='Init')
        c2.node('1')
        c2.node('Login')
        c2.edge('1', 'Login', 'login')
        c2.edge('Login', '1', 'incorrect')

    with c.subgraph(name='cluster_lobby') as c2:
        c2.attr(color='pink', label='Lobby')
        c2.node('2')
        c2.node('Logout')
        c2.edge("Login", "2", label="ok")
        c2.edge("2", "Logout", label="logout")
        c2.edge("Logout", "Init", label="completed")
        c2.edge("2", "Reply", label="game_summary")

    c.edge("Reply", "Game", label="Agree")
    c.edge("Reply", "Lobby", label="Reject")

    c.edge("Game", "Game", label="Move")
    c.edge("Game", "Game", label="MoveEcho")
    c.edge("Game", "Init", label="GameoverFloodgate")
    c.edge("Game", "Lobby", label="GameoverWcsc")

# 描画
g.render("graphs")
