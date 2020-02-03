![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

# Darknet #
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).


----
### 日本語解説
本レポジトリではYOLOv3をFineTuningすることで日本の伝統的なオブジェクトの検出を行う．  
検出対象を以下に示す．

#### 検出対象オブジェクト
- [x] Torii(鳥居(赤))
- [ ] Torii(鳥居(赤以外))
- [ ] Pagoda(五重の塔)
- [ ] Gate(門)
- [ ] Yanagi(柳)

現状では鳥居の認識のみが可能となっている．  
学習用データセッットにはPythonのパッケージであるiclawlerをもちいてスクレイピングを行なった．  
アノテーション作業にはLabelmgを用いた．  
データセットの90%を学習用に，10%を検証用に分割した．  
検出対象を増やす際は[1]を参考に，学習時にエラーが出た際は[2]を参考にせよ． 


#### 参考文献

[1] https://eng-memo.info/blog/yolo-original-dataset/  
[2] https://eng-memo.info/blog/yolo-stb-image-open-error/


