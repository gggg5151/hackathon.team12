from flask import Flask, render_template
import random

app = Flask(__name__)

# メニュー項目とそれぞれの価格を辞書で定義
menu_items = {
    "主食": [("ご飯", 100), ("パン", 150), ("うどん", 150)],
    "汁物": [("味噌汁", 70), ("スープ", 120), ("コンソメスープ", 130)],
    "小鉢": [("サラダ", 150), ("おひたし", 100), ("冷奴", 120)],
    "おかず": [("焼き魚", 250), ("ハンバーグ", 350), ("エビフライ", 280)],
    "飲み物": [("お茶", 100), ("ジュース", 150), ("コーヒー", 200)]
}

@app.route('/')
def index():
    # ランダムにメニューを選択
    selected_menu = {category: random.choice(items) for category, items in menu_items.items()}
    
    # 各項目の価格を合計
    total_price = sum(price for item, price in selected_menu.values())
    
    # HTMLに変数を渡して表示
    return render_template('kondate.html', menu=selected_menu, total=total_price)

if __name__ == '__main__':
    app.run(debug=True)
