from icrawler.builtin import GoogleImageCrawler
import sys
import os
#python3 scraping_icrawler.py 保存フォルダ名 検索ワード 最大取得枚数


argv = sys.argv
 
if os.path.isdir(argv[1]):
    print("フォルダがすでに存在します．")
os.makedirs(argv[1], exist_ok=False)

print("make dir")

crawler = GoogleImageCrawler(storage = {"root_dir" : argv[1]})
crawler.crawl(keyword = argv[2], max_num = int(argv[3])) 
