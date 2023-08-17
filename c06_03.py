userinfo = input('名前と血液型をカンマで区切って１行で入力>>')
[name, blood] = userinfo.split(',')
blood = blood.upper().strip()  # メソッドチェーン
print(f'{name}さんは{blood}型なので大吉です')
"""
strip():文字列の前後の空白を取り除く
upper():すべて大文字に
"""
