Seleniumを使った手動＋自動の対話処理を行うためのサンプル
====
一般的には、Seleniumを使うと完全に自動化されるため、途中に人の手を入れることができないが  
本サンプルでは、Seleniumで起動したChromeに対して、人が操作を行った後に自動処理を行うことを想定している。

# 環境構築
ライブラリインストール
```
pip install -r requirements.txt
```

# 起動方法
```
python main/eel_controller.py
```

Chromeが起動した後、EEL画面が表示するので、  
Chromeを自由に操作することができ、かつEEL画面の「処理実行」ボタンをクリックすると  
execute_function関数が発火して、独自の処理を行うことができる。

# カスタマイズ
engine/crawler.py > exucute_function関数に自動化したい処理を記述すると  
任意の処理を組み込むことができる。