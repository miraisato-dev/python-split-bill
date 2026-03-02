# 幹事無料ボタンを追加

import tkinter as tk
import math

def calc_payment(total, num, unit):
    dnum = total / num
    ind_payment = math.ceil(dnum / unit) * unit
    payorg = total - ind_payment * (num - 1)
    return ind_payment, payorg

def calc_organizer_free(total, num, unit):
    num_for_calc = num - 1
    ind = math.ceil((total / num_for_calc) / unit) * unit
    org = 0
    return ind, org

def execute():
    try:
        num = num_var.get()
        total = int(entry_total.get())

        if num <= 0:
            label_result.config(text='人数は1人以上にしてください')
            return

        unit_map = {1:100, 2:10, 3:1}
        unit = unit_map[calc_type.get()]

        # 幹事無料チェック
        if var1.get() == 1:
            if num <= 1:
                label_result.config(text='幹事無料にするには2人以上必要です')
                return

            ind, org = calc_organizer_free(total, num, unit)

        else:
            ind, org = calc_payment(total, num, unit)

        # 表示
        label_result.config(
            text=f'一人当たり: {ind} 円\n幹事: {org} 円'
        )

    except ValueError:
        label_result.config(text='数字を入力してください')

root = tk.Tk()
root.title('割り勘計算アプリ')
root.geometry('300x300')

# 人数用の変数
num_var = tk.IntVar(value=1)

tk.Label(root, text='参加人数を選択してください >>').pack()

tk.OptionMenu(
    root,
    num_var,
    *range(1, 21)   # 1〜20
).pack(pady=10)

# 合計金額
tk.Label(root, text='合計金額を入力してください >>').pack()
entry_total = tk.Entry(root)
entry_total.pack(pady=0)

# 漢字を会計から除外する場合のチェックボックス
var1 = tk.IntVar()
tk.Checkbutton(root, text="幹事を会計から除外する", variable=var1).pack(pady=10)

# 会計計算単位を選ぶラジオボタン
tk.Label(root, text='計算方法を選択してください >>').pack()
# 横並び用フレームを作る
frame_radio = tk.Frame(root)
frame_radio.pack()   # 中央に置かれる(packはデフォルトが中央設置)

# フレームの中で横並び
calc_type = tk.IntVar(value=1)  # ← ここで初期値を指定
tk.Radiobutton(frame_radio, text="100円単位", variable=calc_type, value=1)\
    .pack(side=tk.LEFT, padx=10)

tk.Radiobutton(frame_radio, text="10円単位", variable=calc_type, value=2)\
    .pack(side=tk.LEFT, padx=10)

tk.Radiobutton(frame_radio, text="1円単位", variable=calc_type, value=3)\
    .pack(side=tk.LEFT, padx=10)

tk.Button(root, text='実行', command=execute).pack(pady=10)

label_result = tk.Label(root, text='')
label_result.pack()

root.mainloop()

