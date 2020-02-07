# 2020SpringSeminar
Hi there✌️ this repository is for Spring Seminar 2020 in Ubi Lab<br>
Schedule is [here](http://isw3.naist.jp/IS/PubWG/Spring2020/index-ja.html#schedule)

# Contents
<pre>
.
├── ObjectDetection #YoLov3によるファインチューニングディレクトリ
│   ├── cfg
│   ├── data
│   │   └── Torii #学習用・テスト用データセットを配置する．
│   ├── examples
│   ├── include
│   ├── python
│   ├── scripts
│   └── src
├── Resource #オリジナル画像データセット
│   ├── CarNumberPlate #共同研究先の京都ドラレコ動画を140フレーム(13.98fps x 10frame)ごとに保存したもの
│   ├── Pagoda #スクレイピングにより取得(keyword：五重の塔，三重の塔)
│   ├── Torii #スクレイピングにより取得(keyword：鳥居)
│   └── Validation #検証用データセット(上記のデータとの重複無し）
│      ├── CarNumberPlate #共同研究先の沖縄ドラレコ動画
│      └── Pagoda #共同研究先の京都ドラレコ動画
└── labelImg #アノテーションソフト
    ├── build-tools
    ├── data
    ├── demo
    ├── libs
    ├── requirements
    ├── resources
    │   ├── icons
    │   └── strings
    └── tests

</pre>
 
 
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
####  0.  ターミナルを開く．
  
#### 1. 任意のディレクトリに本リポジトリをクローンする．
    $git clone https://github.com/yohe4274/2020SpringSeminar.git

- 各コマンドの説明    
    - git clone：リモートリポジトリをローカルリポジトリに複製する．
+ [ ]  **確認2**：NAISTディレクトリ以下に2020SpringSeminarフォルダが作成されていることを確認する．

#### 2. クローンしたローカルリポジトリについて，プロジェクトの枝分かれを行い自分の作業場所を確保する．(ブランチを切る)
     $cd ./2020SpringSeminar/
     $git branch 
     * master
     $git branch yohei  #yoheiは自分の名前に変える
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
#### 1. Labelimgのビルド
- Macユーザは以下の手順で行う．<br>
```
$cd ./2020SpringSeminar/labelImg
$pip3 install pyqt5 lxml # Install qt and lxml by pip
$make qt5py3
$python3 labelImg.py 
#GUIで実行可能か確認. 確認できたら閉じてメンターに知らせる．
```    


- Windowsユーザは以下の手順で行う．<br>
```
$cd ./2020SpringSeminar/labelImg
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
$cd 2020SpringSeminar
$rm -rf ./ObjectDetection/data/Torii
$mkdir ./ObjectDetection/data/CarNumberPlate
```
2. ObjectDetectionディレクトリ内のcfgフォルダと,dataフォルダにある各ファイルの名前について，JapaneseObject〜.〜をCarNumberPlate〜.〜に変更する．
3. LabelImgを起動し，アノテーション付け．
```
$cd labelImg
$python3 labelImg.py ../Resource/CarNumberPlate ../Resource/CarNumberPlate.txt
```
- 出力先フォルダは ./2020SpringSeminar/Resource/CarNumberPlate_VB

4. YOLOv3に学習させるデータセットをObjectDetection/data以下に配置する．
```
$cd 2020SpringSeminar
$cp Resource/CarNumberPlate/* ObjectDetection/data/CarNumberPlate/
$cp Resource/CarNumberPlate_VB/* ObjectDetection/data/CarNumberPlate/
```

##### **for Pagoda Team**
1. ObjectDetectionディレクトリ内のdataフォルダ内に新規フォルダを作成．(名前:Pagoda)
```
$cd 2020SpringSeminar
$ mkdir ./ObjectDetection/data/Pagoda
```

2. LabelImgを起動し，アノテーション付け．
```
$cd labelImg
$python3 labelImg.py ../Resource/Pagoda ../Resource/JapaneseObject.txt   
```
- 出力先フォルダは ./2020SpringSeminar/Resource/Pagoda_VB

4. YOLOv3に学習させるデータセットをObjectDetection/data以下に配置する．
```
$cd 2020SpringSeminar
$cp Resource/Pagoda/* ObjectDetection/data/Pagoda/
$cp Resource/Pagoda_VB/* ObjectDetection/data/Pagoda/
```
-----------

## Step 3
ObjectDetection内のdata,cfgフォルダを編集して，リモートリポジトリにアップロード(push)する．<br>
- ObjectDetection/README.mdの参考文献[1]を参考に変更する．
```
# 編集が必要なファイル
./2020SpringSeminar/ObjectDetection/cfg/~~-frozen.cfg
./2020SpringSeminar/ObjectDetection/cfg/~~.cfg
./2020SpringSeminar/ObjectDetection/cfg/~~.data
./2020SpringSeminar/ObjectDetection/cfg/~~-test.txt #split.pyが便利(自分で実装してもOK)
./2020SpringSeminar/ObjectDetection/cfg/~~-train.txt #split.pyが便利
./2020SpringSeminar/ObjectDetection/data/.names
```
- 各コマンドの説明 (基本的にadd→commit→pushの順に行う)
    - git add ファイル名：ファイルを選択し，ローカルリポジトリで更新する．
    - git add \*：全てのファイルをローカルリポジトリで更新する．
    - git commit -m "message"：ローカルリポジトリを更新(コミット)する．""で囲まれた中にコミットメッセージを記入する．
    - git push origin ブランチ名：ローカルリポジトリの変化をリモートリポジトリの指定のブランチで更新する．

-----------
## Step 4-1
Google Colabを用いてYoLov3をファインチューニングする．<br>
Step4-1ができない場合はStep4-2を行う．
#### 1. GitHubにてYOLOv3FineTuning.ipynbのファイルをクリックする.
#### 2. 画面中央・青ボタンのOpen in Colabボタンを押し，別タブでGoogle Colabを開く
- 以降の操作はファイル内部にコメントあり．


## Step 4-2
#### 1. ./YOLOv3FineTuning.ipynbをGoogle Driveにアップロードする．
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




