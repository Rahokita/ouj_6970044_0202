

# 図02-02-01に示すグラフを定義
Tree = [["A",1,2],["B",3,4],["C",0,0],["D",5,6],["E",0,0],["F",0,0],["G",7,8],["H",0,0],["I",0,0]]

#-------------------------------------
# 幅優先探索
#-------------------------------------
# [0]初期化
OpenList= ""
CloseList= ""
i = 0
n = ""

mode = input('1:深さ優先探索　2:幅優先探索　->　')
# [0-2]目標点を設定する
GoalNode= input('目標点を設定　->　')


# [0-3]探索を開始する点をOpenListに入れる
OpenList = OpenList + Tree[0][0]
print("n:",n,"\tOpenList:" ,OpenList ,"\t\t\t CloseList:" ,CloseList)

# [1]
counter = 0
#while True:
while(counter < 10):
    counter = counter + 1   
# [1-1]

    #(2) OpenListが空（解がない）なら探索は失敗して終了
    if OpenList == "":
        print("探索失敗")
        break
    #(3) OpenListの先頭のnを取り除き、CloseListに入れる
    #(3-1)OpenListの先頭のnを取り除く
    n = OpenList[0]
    OpenList = OpenList[1:]
    #(3-2)nをCloseListに入れる
    CloseList= n + CloseList
    
    i = 0
    while (i < len(Tree) - 1):
        if Tree[i][0] == n:
            break
        i = i + 1
        
    print("n:",n,"\tOpenList:" ,OpenList ,"\t\t\t CloseList:" ,CloseList)

    #(4)nが目標点であるならば、探索は成功して終了
    if GoalNode == n:
        print("探索成功")
        break
    
    #(5)nの子をOpenListに入れる
    tmpString =""
    for j in range(2):
        #(5-1)nの子ノードNoを取得。子が存在しない場合は0となる
        child_node = Tree[i][j+1]
       
        if child_node != 0:
            #tmpString = tmpString + Tree[child_node][0]
             # nの子がOpenListやCloseListに含まれていないことを確認
            if (Tree[child_node][0] in OpenList) == False:
                if (Tree[child_node][0] in CloseList) == False:                     
                    tmpString = tmpString + Tree[child_node][0]
           
    if tmpString != "":
        #(5-2)nの子が取得できた場合、子をOpenListに入れる
        if mode == "1": #深さ優先探索
            #(*-a)子をOpenListの先頭に入れる
            OpenList = tmpString + OpenList
        if mode == "2":
            #(*-b)子をOpenListの末尾に入れる
            OpenList = OpenList + tmpString
        print("n:",n,"\tOpenList:" ,OpenList ,"\t\t\t CloseList:" ,CloseList)
    #break
    
    



