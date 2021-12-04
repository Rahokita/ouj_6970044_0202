

# 図02-02-01に示すグラフを定義
from anytree import Node, RenderTree, findall_by_attr,Walker
# from anytree.exporter import JsonExporter
 
node_a  = Node( "A" , parent=None )
node_b = Node( "B", parent=node_a )
node_d = Node( "D", parent=node_b )
node_e = Node( "E", parent=node_b )
node_f = Node( "F", parent=node_d )
node_g = Node( "G", parent=node_d )
node_h = Node( "H", parent=node_g )
node_i = Node( "I", parent=node_g )
node_c = Node( "C",  parent=node_a )

# グラフを出力
for pre, fill, node in RenderTree(node_a):
    print("%s%s" % (pre, node.name))
    
#print(node_a.root)
#print(node_c.is_leaf)
#print(node_a.children)
#print(node_a.name)
#print(node_a.leaves)

string = str(node_a.children[0])
print(string[-3])

print(findall_by_attr(node_a, "D"))
w = Walker()
print(w.walk(node_b, node_d))
print(node_a)

# exporter = JsonExporter()
# print(exporter.export(node_a))


#-------------------------------------
# 深さ優先探索
#-------------------------------------
# [0]初期化
OpenList= ""
CloseList= ""

# [0-1]目標点を設定する
GoalNode= input('目標点を設定　->　')
#GoalNode="E"

# [0-2]探索を開始する点をOpenListに入れる
OpenList = OpenList + node_a.name

# [1]
while True:
# [1-1]
    print("OpenList:" ,OpenList ,"CloseList:" ,CloseList)

    #(2) OpenListが空（解がない）なら探索は失敗して終了
    if OpenList == "":
        print("探索失敗")
        break
    #(3) OpenListの先頭のnを取り除き、CloseListに入れる
    n = OpenList[0]
    OpenList = OpenList[2:]
    CloseList= CloseList + n

    #(4)nが目標点であるならば、探索は成功して終了
    if GoalNode == n:
        print("探索成功")
        break
    
    #(5)
    #(*-1)nの子を取得
    



