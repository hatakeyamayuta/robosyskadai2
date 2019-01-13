# 2018ロボットシステム学課題2
## 動作説明
 ROSのノードで指令を送りLED点滅させ,ウェブサーバに指令を表示させる <p> 
動画 

### 動作環境

|||
|:--:|:--:|
|Raspberry Pi|Raspberry Pi Model 3B+|
|OS| Ubuntu16.04|
## 回路説明
* GPIO25とGNDの間にLEDを接続
  * GPIO25: 22番ピン
  * GND: 39番ピン
![](./kairo.PNG)
## インストール方法
```
$ git clone https://github.com/hatakeyamayuta/robosyskadai1.git
$ cd robosyskadai2
```
