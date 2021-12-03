

# 図02-02-01に示すグラフを定義
from anytree import Node, RenderTree
 
node_a  = Node( "A" , parent=None )
node_b = Node( "B", parent=node_a )
node_d = Node( "D", parent=node_b )
node_e = Node( "E", parent=node_b )
node_f = Node( "F", parent=node_d )
node_g = Node( "G", parent=node_d )
node_h = Node( "H", parent=node_g )
node_i = Node( "I", parent=node_g )
node_c  = Node( "C",  parent=node_a )

# グラフを出力
for pre, fill, node in RenderTree(node_a):
    print("%s%s" % (pre, node.name))
