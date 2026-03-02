# 計算の単位を変更できるようになった
import tkinter as tk
import math

def calc_payment(total, num):
    dnum = total / num
    ind_payment = math.ceil(dnum / 100) * 100
    payorg = total - ind_payment * (num - 1)
    return ind_payment, payorg

def calc_payment_10(total, num):
    dnum = total / num
    ind_payment = math.ceil(dnum / 10) * 10
    payorg = total - ind_payment * (num - 1)
    return ind_payment, payorg

def calc_payment_1(total, num):
    dnum = total / num
    ind_payment = math.ceil(dnum)
    payorg = total - ind_payment * (num - 1)
    return ind_payment, payorg

def execute():
    try:
        num = int(entry_num.get())
        total = int(entry_total.get())

        if num <= 0:
            label_result.config(text='人数は1人以上にしてください')
            return

        # ラジオボタンの値を取得
        selected = calc_type.get()

        if selected == 1:
            ind, org = calc_payment(total, num)
        elif selected == 2:
            ind, org = calc_payment_10(total, num)
        elif selected == 3:
            ind, org = calc_payment_1(total, num)

        label_result.config(
            text=f'一人当たり: {ind} 円\n幹事: {org} 円'
        )

    except:
        label_result.config(text='数字を入力してください')

root = tk.Tk()
root.title('割り勘計算アプリ')
root.geometry('300x300')

tk.Label(root, text='参加人数を入力してください >>').pack()
entry_num = tk.Entry(root)
entry_num.pack(pady=10)

tk.Label(root, text='合計金額を入力してください >>').pack()
entry_total = tk.Entry(root)
entry_total.pack(pady=10)

label_result = tk.Label(root, text='')
label_result.pack()

tk.Label(root, text='計算方法を選択してください >>').pack()
# 横並び用フレームを作る
frame_radio = tk.Frame(root)
frame_radio.pack()   # ← これで中央に置かれる

# フレームの中で横並び
calc_type = tk.IntVar(value=1)  # ← ここで初期値を指定
tk.Radiobutton(frame_radio, text="100円単位", variable=calc_type, value=1)\
    .pack(side=tk.LEFT, padx=10)

tk.Radiobutton(frame_radio, text="10円単位", variable=calc_type, value=2)\
    .pack(side=tk.LEFT, padx=10)

tk.Radiobutton(frame_radio, text="1円単位", variable=calc_type, value=3)\
    .pack(side=tk.LEFT, padx=10)

tk.Button(root, text='実行', command=execute).pack(pady=10)

root.mainloop()
