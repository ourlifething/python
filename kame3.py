import turtle

t = turtle.Turtle() # インスタンス作成
t.shape('turtle') # 見た目を亀に
t.forward(100) # 向いてる方向に100移動
t.right(90) # 90度回転
t.forward(100) # 向いてる方向に100移動
t.right(90) # 90度回転
t.forward(100) # 向いてる方向に100移動
t.home() # 原点に移動し、デフォルトの方向を向く（右)
turtle.mainloop() # 実行を監視
