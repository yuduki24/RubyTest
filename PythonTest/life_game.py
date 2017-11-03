from random import randint
from tkinter import *

# ステージサイズ.
COLS, ROWS = [30, 20]
CW = 20 # セルの描画サイズ.
data = [] # ステージデータ.

 # ステージをランダムに初期化.
for y in range(0, ROWS):
	data.append([(randint(0, 9) == 0) for x in range(0, COLS)])

# ルールの実装.
def check(x, y):
	# 周囲の生存セルを数える.
	count = 0
	table = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

	for t in table:
		xx, yy = [x + t[0], y + t[1]]
		if 0 <= xx < COLS and 0 <= yy < ROWS:
			if data[yy][xx]: count += 1

	# ルールに沿って次世代の生死を決める.
	if count == 3: return True # 誕生.
	if data[y][x]:
		if 2 <= count <= 3: return True # 生存.
		return False # 過疎/過密.
	return data[y][x]

# データを次の世代に進める.
def next_turn():
	global data
	data2 = []
	for y in range(0, ROWS):
		data2.append([check(x, y) for x in range(0, COLS)])
	data = data2 # データの内容を次世代へ差し替える.

# 画面を構築.
window = Tk()
cv = Canvas(window, width = 600, height = 400)
cv.pack()

# ステージを描画.
def draw_stage():
	cv.delete('all')
	for y in range(0, ROWS):
		for x in range(0, COLS):
			if not data[y][x]: continue
			x1, y1 = [x * CW, y * CW]
			cv.create_oval(x1, y1, x1 + CW, y1 + CW,
				fill = "red", width = 0) # 生きているセルを描画.

# 500ミリ秒ごとに世代を進める.
def game_loop():
	next_turn()
	draw_stage()
	window.after(500, game_loop)

game_loop()
window.mainloop()




