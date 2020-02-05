import os
import glob

img_files = sorted(glob.glob("../data/Torii/*.jpg"))
txt_files = sorted(glob.glob("../data/Torii/*.txt"))
print("The number of image-files is", len(img_files), ".")
print("The number of annotaion-files is", len(txt_files), ".")
if len(img_files) != len(txt_files):
    print("the number of files is not same.")

else:
    train_num = round(len(img_files) * 0.7) #70%を学習用に
    test_num = len(img_files)- train_num
    print("train-num is", train_num, ".")
    print("test-imgs is",  test_num,".")

    # 学習画像，テスト画像を示すパスを以下のテキストファイルに保存する．
    path_train = './JapaneseObject-train.txt'
    path_test = './JapaneseObject-test.txt'



    train_w = open(path_train, 'w')
    test_w = open(path_test, 'w')

    for i in range(len(img_files)):
        if i < train_num :
            train_w.write(img_files[i]+"\n")
        else:
            test_w.write(img_files[i]+"\n")

    train_w.close()
    test_w.close()
