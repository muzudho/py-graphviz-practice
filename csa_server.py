from graphviz import Digraph

# グラフの設定
g = Digraph(format="png")
g.attr("node", shape="square", style="filled")

# クラスター 'cluster_' から名前を始める必要あり
with g.subgraph(name='cluster_root') as c:
    # 一番外側のクラスターのラベルは図のタイトルのように見える
    c.attr(color='white', label='CSA Server protocol 1.2.1')

    # 開始ノード
    c.node("Start", shape="circle", color="pink")

    # ２つのノードと、その二間の有向な辺
    c.edge("Start", "1", label="Start")

    with c.subgraph(name='cluster_init') as c2:
        c2.attr(color='pink', label='Init')
        c2.node('1', color="pink")
        c2.node('Login')
        c2.edge('1', 'Login', label='login')
        c2.edge('Login', '1', label='incorrect')

    with c.subgraph(name='cluster_lobby') as c2:
        c2.attr(color='pink', label='Lobby')
        c2.node('2', color="pink")
        c2.node('Logout')
        c2.edge("2", "Logout", label="logout")

    with c.subgraph(name='cluster_reply') as c2:
        c2.attr(color='pink', label='Reply')
        c2.node('3', color="pink")
        c2.node('Agree')
        c2.node('Reject')
        c2.edge("3", "Agree", label="agree")
        c2.edge("3", "Reject", label="reject")

    with c.subgraph(name='cluster_game') as c2:
        c2.attr(color='pink', label='Game')
        c2.node('4', color="pink")
        c2.edge("4", "4", label="Move")
        c2.edge("4", "4", label="MoveEcho")

    c.edge("Login", "2", label="ok")
    c.edge("Logout", "1", label="completed")
    c.edge("Reject", "2", label="reject")
    c.edge("2", "3", label="game_summary")
    c.edge("Agree", "4", label="start")
    c.edge("4", "2", label="GameoverWcsc")
    c.edge("4", "1", label="GameoverFloodgate")

# 描画
g.render("graphs")
