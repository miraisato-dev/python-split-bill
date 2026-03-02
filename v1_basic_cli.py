import TkEasyGUI as eg
import math

layout = [
    eg.align_center([eg.Text('参加人数を入力してください >>'), eg.Input('', key = "in", size=(10, 1))]),
    eg.align_center([eg.Text('合計金額を入力してください >>'), eg.Input('', key = 'in2', size=(10, 1))]), # pysimpleGUIではBと省略可能
    eg.align_center([eg.Text('', key = "txt")]), # pysimpleGUIはTなど省略可能 パーツを操作したい場合はkey, Kとして名前を付ける(htmlでいうidのようなものだと思う)
    eg.align_center([eg.Button('実行', key = 'btn')])
]

win = eg.Window('割り勘計算アプリ', layout, size = (300, 150)) # winはwindowの略でつけた変数名

def calc_payment(total, num):
    dnum = total / num
    ind_payment = math.ceil(dnum / 100) * 100
    # 幹事支払額 = 総額 - 一人当たりの支払額 * 人数
    payorg = total - ind_payment * (num - 1)
    return ind_payment, payorg

def execute(): # ボタンを押したらこれを実行などの場合は基本的に関数を作成すると思って構わない
    win['txt'].update()

while True:
    event, values = win.read()

    if event == eg.WINDOW_CLOSED:
        break

    if event == 'btn':
        try:
            num = int(values['in'])
            total = int(values['in2'])

            ind, org = calc_payment(total, num)

            win['txt'].update(
                f'一人 {ind} 円\n幹事 {org} 円'
            )
        except:
            win['txt'].update('数字を入力してください')

win.close()
