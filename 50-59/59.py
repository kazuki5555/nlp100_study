# 59. S式の解析
# Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．

import xml.etree.ElementTree as ET

tree = ET.parse("tmp/nlp.txt.xml")