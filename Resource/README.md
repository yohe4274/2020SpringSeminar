### Torii
- icrawlerからスクレイピングした画像データセット．
- 各画像ファイルには検索ワードと通番号が付与されている．

### Pagoda
- icrawlerからスクレイピングした画像データセット．
- 各画像ファイルには検索ワードと通番号が付与されている．

### CarNumberPlate
- 京都のroute動画1~3について140フレーム(fps13.98 x 10s)ごとに画像化したデータセット
- 各画像ファイルにはオリジナル動画のファイル名とフレーム番号が付与されている．

### rename_files.py
- あるフォルダ内のファイルの名前を通し番号に変える．

### scrapying_iclawler.py
- pythonのpackageのicrawlerを用いてウェブから画像をスクレイピングする．
- 第１引数は保存先
- 第２引数は検索ワード
- 第３引数は最大ダウンロード枚数
- [ここ](https://qiita.com/NakaokaRei/items/8c7e7b1f2c0c7ef8b3a3)を参考に実装．