import os
import re

#----------------------------------
# オプション
#----------------------------------

#処理対象拡張子
ext = '.log'
#処理対象サブディレクトリ名
src_dir = '.'
#処理結果格納用サブディレクトリ名
kekka_dir = './処理結果'
#分割する行を判定する文字列定義
icchi_list = [
    '# sh',
    '#sh'
]

#----------------------------------
if not os.path.isdir(kekka_dir):
    os.makedirs(kekka_dir)

bf_dir = os.listdir(src_dir)
s_block = ""
for log in bf_dir:
    if ext in log:
        #ソースファイル名出力
        print('\r\n\r\n'); print('file:' + log)
        file_name1 = log.split( ext )
        path1 = src_dir + '/' + log
        path2 = kekka_dir + '/' + file_name1[0] + '_0' + ext

        with open(path1, encoding="utf-8") as f:
            line_num = 0
            for s_line in f:
                for icchi_content in icchi_list:
                    if icchi_content in s_line:
                        with open (path2, mode="w", encoding="utf-8") as ffw:
                            ffw.write(s_block)
                            #結果ファイル名出力
                            print('  --> ' + path2)
                        s_head = re.sub('\n|\s|.*#', '_', s_line)
                        path2 = kekka_dir + '/' + file_name1[0] + "_" + str(line_num).zfill(5) + "_" + s_head[:30] + ext
                        s_block = ""
                s_block = s_block + s_line
                line_num = line_num + 1
            
