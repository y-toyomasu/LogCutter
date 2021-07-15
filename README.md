# LogCutter
Cisco機器のshowコマンドが複数実行されているログファイルを、各showコマンドごとに分割します。

# 使い方
## Windows
* logcutter.py と logcutter.bat を対象のログファイルと同じフォルダに格納します。
* logcutter.batを実行します。
分割後のファイルがprocessedフォルダに格納されます。

## カスタマイズ
logcutter.py のこの辺のパラメータで多少カスタマイズ可能です。

```python
#----------------------------------
# オプション
#----------------------------------

#処理対象拡張子
ext = '.log'
#処理対象サブディレクトリ名
src_dir = '.'
#処理結果格納用サブディレクトリ名
kekka_dir = './processed'
#分割する行を判定する文字列定義
icchi_list = [
    '# sh',
    '#sh'
]

#----------------------------------
```

# 動作確認環境
Windows10 Python3.9 ( Microsoft Store からインストール )


# 

# What's This
LogCutter divides the log file in which multiple show commands of Cisco equipment are executed for each show command.

# How to use
## Windows
* Store logcutter.py and logcutter.bat in the same folder as the target log file.
* Run logcutter.bat.
The split files will be stored in the "processed" folder.

# Executable environment 
Windows10 Python3.9 (installed from Microsoft Store)
