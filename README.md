# 2020SpringSeminar
Hi there✌️ this repository is for Spring Seminar 2020 in Ubi Lab<br>
Schedule is [here](http://isw3.naist.jp/IS/PubWG/Spring2020/index-ja.html#schedule)

## Contents



## Step 0
GitHubの基本を押さえて，環境を構築する．
#### 0. デスクトップに新規フォルダ(ディレクトリ)を作成．
(ディレクトリ名：NAIST)
```
$mkdir /Users/〜〜/Desktop/NAIST
$cd /Users/〜〜/Desktop/NAIST
```    
#### 1. 本リポジトリをクローンする．
    $git clone https://github.com/yohe4274/2020SpringSeminar.git
- git clone：リモートリポジトリをローカルリポジトリに複製する．
##### [確認0]:NAISTディレクトリ以下に2020SpringSeminarフォルダが作成されていることを確認する．

#### 2. クローンしたローカルリポジトリについて，プロジェクトの枝分かれを行い自分の作業場所を確保する．(ブランチを切る)
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
- git branch：ブランチを確認する．
- git branch 名前：新しくブランチを作成する．
- git checkout 名前：ブランチの切り替えを行う．(作業場所をかえる🐸重要！)

## Step 1
OSS(Open Sourcce Software)のアノンテーションツールである，LabelImgを用いて物体検出に必要なアノテーションを付ける．<br>
#### 0. Labelimgのインストール
まずPythonの3系が入っているかを以下のコマンドで確認する．
```
$python --version
$python3 --version
```
~python3系がインストールされていない人は[ここ](https://qiita.com/Yohey32/items/6684c7cf05dac2d42a11)を参考にインストールする．~<br>

[New]Anaconda3系を入れる．

##### [確認1]:python3系が入っていることをメンターに確認してもらった後，以下に進む．
- Macユーザは以下の手順で行う．<br>
```
$cd /Users/〜〜/Desktop/NAIST
$git clone https://github.com/tzutalin/labelImg.git
$cd /Users/〜〜/Desktop/NAIST/labelImg
$pip3 install pyqt5 lxml # Install qt and lxml by pip
$make qt5py3
$python3 labelImg.py #GUIで実行可能か確認．確認できたら閉じる
```    


- Windowsユーザは以下の手順で行う．<br>
```
$cd /Users/〜〜/Desktop/NAIST
$git clone https://github.com/tzutalin/labelImg.git
$cd /Users/〜〜/Desktop/NAIST/labelImg
$pip3 install pyqt5 lxml # Install qt and lxml by pip
$pyrcc5 -o resources.py resources.qrc
$python labelImg.py  #GUIで実行可能か確認．確認できたら閉じてメンターに知らせる．
$python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```
[エラー１](https://stackoverflow.com/questions/58140305/labelimg-pyrcc5-is-not-recognized-as-an-internal-or-external-command)

#### 1. LabelImgを用いて画像にアノテーション付け
- [ここ](https://demura.net/misc/14350.html)を参考にして，チーム内で作業分担しながらラベル付けをする．


### for Car-Number-Plate Team
1. ObjectDetectionディレクトリ内のcfgフォルダと,dataフォルダにある各ファイルの名前について，JapaneseObject〜.〜からCarNumberPlate〜.〜に変更する．
2. ObjectDetectionディレクトリ内のdataフォルダにあるToriiフォルダを削除し，dataフォルダ内に新規フォルダを作成．(名前:CarNumberPlate)
3. 以下のコマンドでLabelImgを起動し，アノテーション付け．
```
$python3 /Users/〜〜/Desktop/NAIST/LabelImg/labelImg.py ../2020SpringSeminar/Resource/Car-Number-Plate ./2020SpringSeminar/Resource/Car-Number-Plate.txt
```
- 出力先フォルダは/Users/〜〜/Desktop/NAIST/2020SpringSeminar/ObjectDetection/data/CarNumberPlate


### for Pagoda Team
1. ObjectDetectionディレクトリ内のdataフォルダ内に新規フォルダを作成．(名前:Pagoda)
```
$ mkdir /Users/〜〜/Desktop/NAIST/2020SpringSeminar/data/Pagoda
```

2. 以下のコマンドでLabelImgを起動し，アノテーション付け．
```
$python3 /Users/〜〜/Desktop/NAIST/LabelImg/labelImg.py ../2020SpringSeminar/Resource/Pagoda ./2020SpringSeminar/Resource/JapaneseObject.txt   
```
- 出力先フォルダは/Users/〜〜/Desktop/NAIST/2020SpringSeminar/ObjectDetection/data/Pagoda


## Step 2
ObjectDetection内のdata,cfgフォルダを編集して，リモートリポジトリにアップロード(push)する．<br>
- ObjectDetection/README.mdの参考文献[1]を参考に変更する．





## Step 3
Google Colabを用いてYoLov3をファインチューニングする．<br>
#### 0. YOLOv3FineTuning.ipynbをGoogle Driveにアップロードする．
好きなアカウント，場所にアップロードしてOK

#### 1. 上記のファイルをGoogleColabで操作する．今後の操作はファイル内部にコメントあり．
- Google ColabとはGoogleが無償で提供するGPUインスタンス．(タイムアウトがあることに注意)
- "Shif + Enter"でセル単位での実行が可能．


## Step 4
- 各自がアノテーション付けした画像を共有して，学習データセットの枚数を増加させる．
- ファインチューニングをもう一度行い，検証してみる．




