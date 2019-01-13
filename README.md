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
* git clone
```
$ git clone https://github.com/hatakeyamayuta/robosyskadai2.git
```
* 始めに「ワークスペース」を作る
```
$ cd
$ mkdir -p catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace
$ cd ~/catkin_ws
$ catkin_make
$ source ~/.bashrc
```
* パッケージの生成しmypkg内にcloneしてきたscriptsとlanchを入れる
```
$ cd ~/catkin_ws/src
$ catkin_create_pkg mypkg rospy
$ cd mypkg/
$ cp -r /home/username/robosyskadai2/* .
```
