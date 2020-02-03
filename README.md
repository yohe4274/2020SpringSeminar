# 2020SpringSeminar
Hi there✌️ this repository is for Spring Seminar 2020 in Ubi Lab

## Contents



## First steps
#### 0. デスクトップに新規フォルダ(ディレクトリ)を作成．
(ディレクトリ名：NAIST)
```
$mkdir /Users/〜〜/Desktop/NAIST
$cd /Users/〜〜/Desktop/NAIST
```    
#### 1. 本レポジトリをクローンする．
    $git clone https://github.com/yohe4274/2020SpringSeminar.git
##### [確認0]:NAISTディレクトリ以下に2020SpringSeminarフォルダが作成されていることを確認する．

#### 2. ブラウザのGitHubページにて自分のアカウントにログインし，新規リモートレポジトリを作成します．
  (レポジトリ名：Ubi_ObjectDetection)

#### 3. 作成したリモートレポジトリをローカルレポジトリにクローンします．(2020SpringSeminarディレクトリの外で以下のコマンド)
    $git clone https://github.com/GitHubアカウント名/Ubi_ObjectDetection.git
##### [確認1]:NAISTディレクトリ内に2020SpringSeminar, Ubi_ObjectDetectionの2フォルダがあることを確認．

#### 4. 2020SpringSeminar内のすべてのファイル，フォルダをUbi_ObjectDetectionに移します．
    $mv 2020SpringSeminar/* Ubi_ObjectDtection
    
#### 5. ローカルリポジトリの情報をリモートリポジトリにアップロード(push)する．
    $cd /Users/〜〜/Desktop/NAIST/Ubi_ObjectDetection
    $git add *
    $git commit -m "メッセージを自分で適当に書く"
    $git push origin master
    
#### 6. 不要なフォルダを削除する．
    $rm -rf /Users/〜〜/Desktop/NAIST/2020SpringSeminar

## How to Use
