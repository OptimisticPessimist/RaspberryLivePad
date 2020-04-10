# Raspberry Live Pad
ラズパイでカメラ映像見ながらゲームパッド使ってラジコンとして動かすやつ

## 概要
Raspberry PiでWebサーバを立ち上げ、用意しているクラスから関数を取得してゲームパッドの操作に割り振ることができる  
Raspberryに接続されたカメラの映像をブラウザから視認しつつ、ゲームパッドで操作を行う  

## デモ
GIF画像かYouTube動画を用意したい

## 必要なもの
- pipenv
- Raspberry Pi (Zero WHを推奨)
- ゲームパッド（PCで使えるもの）
- 動かす対象物

### あるとよいもの
- ブレッドボード
- Raspberry Pi用カメラ

## 使用方法
### Raspberry Pi側
あらかじめ `src/controller.py` の `GamePad` クラスにRaspberry PiのGPIOを操作する処理を記述しておく

```shell script
# IPアドレスの確認 wlan0 のアドレスを参照する
ip a

# インストール
git clone https://github.com/OptimisticPessimist/RaspberryLivePad.git
cd RaspberryLivePad
pipenv install .
export FLASK_APP=app.py

# ラズパイ内にサーバを立ち上げる
pipenv shell
flask run
```

### リモート側
調べておいたRaspberry Piのアドレスにブラウザから接続し、ゲームパッドの設定をする

## Licence
[GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)