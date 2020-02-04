import glob
import os

files = glob.glob("./五重の塔/*.*")


for i, old_name in enumerate(files):
    # ファイル名の決定
    new_name = "./五重の塔/五重の塔_{0:06d}.jpg".format(i + 1)
    # ファイル名の変更
    os.rename(old_name, new_name)
    # 変更の表示
    print(old_name + " → " + new_name)
    num = i
