import os
import glob

img_files = sorted(glob.glob("../data/Torii/*.jpg"))
txt_files = sorted(glob.glob("../data/Torii/*.txt"))
print("The number of image-files is", len(img_files), ".")
print("The number of annotaion-files is", len(txt_files), ".")


# 例外処理
if len(img_files) != len(txt_files):
    print("the number of files is not same.")
else:

    # Percentage of images to be used for the test set
    percentage_test = 10;
    counter = 1
    index_test = round(100 / percentage_test)


    train_num = 0
    test_num = 0


    # 学習画像，テスト画像を示すパスを以下のテキストファイルに保存する．
    path_train = '../cfg/JapaneseObject-train.txt'
    path_test = '../cfg/JapaneseObject-test.txt'



    train_w = open(path_train, 'w')
    test_w = open(path_test, 'w')

    for i in range(len(img_files)):
        if counter == index_test:
            counter = 1
            test_w.write(img_files[i].split('./')[1]+"\n")
            test_num += 1
        else:
            train_w.write(img_files[i].split('./')[1]+"\n")
            counter = counter + 1
            train_num += 1

    print("train-num is", train_num, ".")
    print("test-imgs is",  test_num,".")
    train_w.close()
    test_w.close()
