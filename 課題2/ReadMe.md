課題2-2をやりました。
途中、どん詰まりしたところもコメントアウトして残しているので、頑張りを見てください。


1.重複のないよう、ランダムで手札の配列に格納(このとき、内部処理用の記号と出力用の記号に分けて出力結果を見やすくしました)

2.見やすくかつ処理しやすくなるよう、手札のランダムのカードをソートする

3.役の判定をする。このとき、より強力な役が優先して結果として出るよう、複雑な判定を先に行って成立していればフラグを立てて移行の判定をスキップするようにした。
