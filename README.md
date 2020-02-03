# 2020SpringSeminar
Hi there✌️ this repository is for Spring Seminar 2020 in Ubi Lab<br>
Schedule is [here](http://isw3.naist.jp/IS/PubWG/Spring2020/index-ja.html#schedule)

## Contents



## Step 0
GitHubの基本を押さえて，環境を構築しよう．
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
OSS(Open Sourcce Software)のアノンテーションツールである，LabelImgを用いて物体検出に必要なアノテーションをつけよう．<br>
#### 0. Labelimgのインストール
python3系がインストールされていない人は[ここ](https://qiita.com/Yohey32/items/6684c7cf05dac2d42a11)を参考にインストールする．

- Macユーザは以下の手順で行う．<br>
```
$cd /Users/〜〜/Desktop/NAIST
$git clone https://github.com/tzutalin/labelImg.git
$cd /Users/〜〜/Desktop/NAIST/labelImg
$pip3 install pyqt5 lxml # Install qt and lxml by pip
$make qt5py3
$python3 labelImg.py
$python3 labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```    


- Windowsユーザは以下の手順で行う．<br>
```
$cd /Users/〜〜/Desktop/NAIST
$git clone https://github.com/tzutalin/labelImg.git
$cd /Users/〜〜/Desktop/NAIST/labelImg
$pip3 install pyqt5 lxml # Install qt and lxml by pip
$pyrcc5 -o resources.py resources.qrc
$python labelImg.py
$python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```
[エラー１](https://stackoverflow.com/questions/58140305/labelimg-pyrcc5-is-not-recognized-as-an-internal-or-external-command)

- [ここ](https://demura.net/misc/14350.html)を参考にして，チーム内で作業分担しながらラベルづけをする．
     
   
## Step 2
ObjectDetectionフォルダを編集して，リモートリポジトリにアップロード(push)しよう．<br>
#### 0. ObjectDetection/cfgを編集
ObjectDetection/README.mdの参考文献[1]を参考に変更する．

#### 1. ObjectDetection/dataを編集
ObjectDetection/README.mdの参考文献[1]を参考に変更する．




## Step 3
Google Colabを用いてYoLov3をファインチューニングしよう．<br>
#### 0. YOLOv3FineTuning.ipynbをGoogle Driveにアップロードする．
好きなアカウント，場所にアップロードしてOK

#### 1. 上記のファイルをGoogleColabで操作する．今後の操作はファイル内部にコメントあり．
- Google ColabとはGoogleが無償で提供するGPUインスタンス．(タイムアウトがあることに注意)
- "Shif + Enter"でセル単位での実行が可能．




