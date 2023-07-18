from wordcloud import WordCloud
import os
import re
import MeCab as mc
 
def strip_CRLF_from_Text(text):
    """テキストファイルの改行，タブを削除し，形態素解析を実行する．
    改行前後が日本語文字の場合は改行を削除する．
    それ以外はスペースに置換する．
    """
    # 改行前後の文字が日本語文字の場合は改行を削除する
    plaintext = re.sub('([ぁ-んー]+|[ァ-ンー]+|[\\u4e00-\\u9FFF]+|[ぁ-んァ-ンー\\u4e00-\\u9FFF]+)(\n)([ぁ-んー]+|[ァ-ンー]+|[\\u4e00-\\u9FFF]+|[ぁ-んァ-ンー\\u4e00-\\u9FFF]+)',
                       r'\1\3',
                       text)
    # 残った改行とタブ記号はスペースに置換する
    plaintext = plaintext.replace('\n', ' ').replace('\t', ' ')
    return plaintext
 
def mecab_wakati(text):
    """
    MeCabで分かち書き
    ただし品詞は名詞だけに限定．
    """
    t = mc.Tagger()
    # t = mc.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
 
    node = t.parseToNode(text)
#print(node)
    sent = ""
    while(node):
#print(node.surface, node.feature)
        if node.surface != "":  # ヘッダとフッタを除外
            word_type = node.feature.split(",")[0]
            # 名詞だけをリストに追加する
            if word_type in ["名詞"]:
                 sent += node.surface + " "  # node.surface は「表層形」
            # 動詞（の原型），形容詞，副詞もリストに加えたい場合は次の２行を有効にする
            if word_type in [ "動詞", "形容詞","副詞"]:
                sent += node.feature.split(",")[6] + " " # node.feature.split(",")[6] は形態素解析結果の「原型」
        node = node.next
        if node is None:
            break
    return sent
 
# テキストファイル読み込み
f = open(os.path.sep.join(['corpora', 'ja_annkert.txt']), encoding='utf-8')
raw = f.read()
f.close()
print(raw)
text = strip_CRLF_from_Text(raw)
print(text)
sent = mecab_wakati(text)
print(sent)
 
# フォントの保存先を指定する（環境によって書き換えてください）
font_path = "C:\\WINDOWS\\FONTS\\MEIRYO.TTC"    ## Windows 版はこちら
 
# WordCloud画像を生成する
wc = WordCloud(max_font_size=36, font_path=font_path).generate(sent)
wc.to_file("ann.png")