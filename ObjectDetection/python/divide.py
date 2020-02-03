import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

current_dir = '../data/JapaneseObject/'
g_colab_full_path='/cotent/JapaneseObjectDetection/data/JapaneseObject'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('JapaneseObject-train.txt', 'w')
file_test = open('JapaneseObject-test.txt', 'w')# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
print(current_dir)
# for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    print(pathAndFilename)
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        # file_test.write(g_colab_full_path + "/" + title + '.jpg' + "\n")
        file_test.write(g_colab_full_path + "/" + title  + "\n")
    else:
        # file_train.write(g_colab_full_path + "/" + title + '.jpg' + "\n")
        file_train.write(g_colab_full_path + "/" + title + "\n")
        counter = counter + 1
