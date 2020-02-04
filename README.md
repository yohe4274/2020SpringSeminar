# 2020SpringSeminar
Hi there✌️ this repository is for Spring Seminar 2020 in Ubi Lab<br>
Schedule is [here](http://isw3.naist.jp/IS/PubWG/Spring2020/index-ja.html#schedule)

# Contents

.<br>
├── ObjectDetection<br>
│   ├── cfg<br>
│   ├── data<br>
│   │   └── Torii：YOLOv3に学習させる画像データとラベルデータ<br>
│   ├── examples<br>
│   ├── include<br>
│   ├── python<br>
│   ├── scripts<br>
│   └── src<br>
└── Resource：画像データ群<br>
    └── Torii<br>
    └── Pagoda<br>
    └── CarNumberPlate<br>

-----------
# How to Use

## Step 0
Git, GitHub, Python3.xの導入．
#### 1. Gitの導入
- Gitとはローカル環境でバージョン管理をする開発システムである．
- まず，Gitが入っているかを確認する．
```
$git --version
```
入っていない場合は以下を参考にインストールする．
- Install for [Mac](https://tracpath.com/bootcamp/git-install-to-mac.html)
- Install for [Windows](https://prog-8.com/docs/git-env-win)

#### 2. GitHubの導入
- GitHubとはリモート上でバージョン管理をするOSS(Open Sourcce Software)である．
- 登録していない場合は，[ここ](https://qiita.com/okumurakengo/items/848f7177765cf25fcde0)を参考に登録する．*2段階認証はしない*

+ [ ]  **確認0**：登録できたらメンターに確認してもらい，本プロジェクトに招待してもらう．

#### 3. Python3系の導入
まずPythonの3系が入っているかを以下のコマンドで確認する．
```
$python --version
$python3 --version
```
~python3系がインストールされていない人は[ここ](https://qiita.com/Yohey32/items/6684c7cf05dac2d42a11)を参考にpython3.xをインストールする．~<br>
python3系がインストールされていない人は[Anaconda3](https://qiita.com/t2y/items/2a3eb58103e85d8064b6)系を入れる．

+ [ ]  **確認1**：python3系が入っていることをメンターに確認してもらった後，以下に進む．


-----------

## Step 1
GitHubの基本を押さえて，環境を構築する． 
#### 1. デスクトップに新規フォルダ(ディレクトリ)を作成．(ディレクトリ名：NAIST)
```
$mkdir /Users/〜〜/Desktop/NAIST
$cd /Users/〜〜/Desktop/NAIST
```    
#### 2. 本リポジトリをクローンする．
    $git clone https://github.com/yohe4274/2020SpringSeminar.git

- 各コマンドの説明    
    - git clone：リモートリポジトリをローカルリポジトリに複製する．
+ [ ]  **確認2**：NAISTディレクトリ以下に2020SpringSeminarフォルダが作成されていることを確認する．

#### 3. クローンしたローカルリポジトリについて，プロジェクトの枝分かれを行い自分の作業場所を確保する．(ブランチを切る)
     $cd /Users/〜〜/Desktop/NAIST/2020SpringSeminar/
     $git branch 
     * master
     $git branch yohei
     * master
       yohei
     $git checkout yohei
       master
     * yohei
     $git branch 
       master
     * yohei

- 各コマンドの説明    
    - git branch：ブランチを確認する．
    - git branch 名前：新しくブランチを作成する．
    - git checkout 名前：ブランチの切り替えを行う．(作業場所をかえる🐸重要！)

-----------

## Step 2
OSSのアノンテーションツールである，LabelImgを用いて物体検出に必要なアノテーションを付ける．<br>
#### 1. Labelimgのインストール
- Macユーザは以下の手順で行う．<br>
```
$cd /Users/〜〜/Desktop/NAIST
$git clone https://github.com/tzutalin/labelImg.git
$cd /Users/〜〜/Desktop/NAIST/labelImg
$pip3 install pyqt5 lxml # Install qt and lxml by pip
$make qt5py3
$python3 labelImg.py 
#GUIで実行可能か確認. 確認できたら閉じてメンターに知らせる．
```    


- Windowsユーザは以下の手順で行う．<br>
```
$cd /Users/〜〜/Desktop/NAIST
$git clone https://github.com/tzutalin/labelImg.git
$cd /Users/〜〜/Desktop/NAIST/labelImg
$pip3 install pyqt5 lxml # Install qt and lxml by pip
$pyrcc5 -o resources.py resources.qrc
$python labelImg.py  
#GUIで実行可能か確認. 確認できたら閉じてメンターに知らせる．
```

+ Windowsでエラーが出たら[ここ](https://stackoverflow.com/questions/58140305/labelimg-pyrcc5-is-not-recognized-as-an-internal-or-external-command)を参考にする．

#### 2. LabelImgを用いて画像にアノテーション付け
- [ここ](https://demura.net/misc/14350.html)を参考にして，チーム内で作業分担しながらラベル付けをする．


##### **for Car-Number-Plate Team**
1. ObjectDetectionディレクトリ内のdataフォルダにあるToriiフォルダを削除し，dataフォルダ内に新規フォルダを作成．(名前:CarNumberPlate)
```
$rm -rf /Users/〜〜/Desktop/NAIST/2020SpringSeminar/ObjectDetection/data/Torii
$mkdir /Users/〜〜/Desktop/NAIST/2020SpringSeminar/ObjectDetection/data/CarNumberPlate
```
2. ObjectDetectionディレクトリ内のcfgフォルダと,dataフォルダにある各ファイルの名前について，JapaneseObject〜.〜をCarNumberPlate〜.〜に変更する．
3. 以下のコマンドでLabelImgを起動し，アノテーション付け．
```
$python3 /Users/〜〜/Desktop/NAIST/LabelImg/labelImg.py ../2020SpringSeminar/Resource/CarNumberPlate ./2020SpringSeminar/Resource/CarNumberPlate.txt
```
- 出力先フォルダは/Users/〜〜/Desktop/NAIST/2020SpringSeminar/ObjectDetection/data/CarNumberPlate


##### **for Pagoda Team**
1. ObjectDetectionディレクトリ内のdataフォルダ内に新規フォルダを作成．(名前:Pagoda)
```
$ mkdir /Users/〜〜/Desktop/NAIST/2020SpringSeminar/data/Pagoda
```

2. 以下のコマンドでLabelImgを起動し，アノテーション付け．
```
$python3 /Users/〜〜/Desktop/NAIST/LabelImg/labelImg.py ../2020SpringSeminar/Resource/Pagoda ./2020SpringSeminar/Resource/JapaneseObject.txt   
```
- 出力先フォルダは/Users/〜〜/Desktop/NAIST/2020SpringSeminar/ObjectDetection/data/Pagoda
-----------

## Step 3
ObjectDetection内のdata,cfgフォルダを編集して，リモートリポジトリにアップロード(push)する．<br>
- ObjectDetection/README.mdの参考文献[1]を参考に変更する．


- 各コマンドの説明    
    - git add ファイル名：ファイルを選択し，ローカルリポジトリで更新する．
    - git add \*：全てのファイルをローカルリポジトリで更新する．
    - git commit -m "message"：ローカルリポジトリを更新(コミット)する．""で囲まれた中にコミットメッセージを記入する．
    - git push origin ブランチ名：ローカルリポジトリの変化をリモートリポジトリの指定のブランチで更新する．

-----------
## Step 4
Google Colabを用いてYoLov3をファインチューニングする．<br>
#### 1. Users/〜〜/Desktop/NAIST/2020SpringSeminar/YOLOv3FineTuning.ipynbをGoogle Driveにアップロードする．
好きなアカウント，場所にアップロードしてOK

#### 2. Google Colabをインストール
- [ここ](https://qiita.com/shoji9x9/items/0ff0f6f603df18d631ab)を参考にColabを入れる．

#### 3. 上記のファイルをGoogleColabで操作する．
- Google ColabとはGoogleが無償で提供するGPUインスタンス．(タイムアウトがあることに注意)
- "Shif + Enter"でセル単位での実行が可能．
- 以降の操作はファイル内部にコメントあり．

-----------


## Step 5(時間があったら)
- 各自がアノテーション付けした画像を共有して，学習データセットの枚数を増加させる．
- ファインチューニングをもう一度行い，検証してみる．




