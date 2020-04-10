整数閉区間を示すクラス（あるいは構造体）をつくりたい。
整数閉区間オブジェクトは下端点と上端点を持ち、
文字列表現も返せる（例: 下端点 3, 上端点 8 の整数閉区間の文字列表記は "[3,8]"）。
ただし、上端点より下端点が大きい閉区間を作ることはできない。
整数の閉区間は指定した整数を含むかどうかを判定できる。
また、別の閉区間と等価かどうかや、完全に含まれるかどうかも判定できる。

# TODO
* [✅] ２つの整数を引数にclassをつくる
    * [✅] class"section"では[3,8]を作れる
    * [✅] class"section"では[3,3]を作れる
    * [✅] 引数(a,b)について、a>bは例外
    * [✅] 引数(a,b)について、小数は例外
    * [✅] 引数(a,b)について、文字列は例外
* [✅] classは文字列表現を返す
    * [✅] "str" method [3,8]を返せる
* [✅] classは指定した整数を含むかどうかを判定できる。
    * [✅] "num_in" methodで、2 in [3,8]はFalseを返す
    * [✅] "num_in" methodで、3 in [3,8]はTrueを返す(境界)
    * [✅] "num_in" methodで、8 in [3,8]はTrueを返す(境界)
    * [✅] "num_in" methodで、9 in [3,8]はFalseを返す
* [ ] classは別の閉区間と等価かどうかを判定できる。
    * [✅] "section_equal" methodで、([3,8],[3,8])はTrueを返す
    * [ ] "section_equal" methodで、([3,9],[3,8])はFalseを返す
* [ ] classは別の閉区間かどうかを判定できる。
    * [ ]"section_in" methodで、([4,7],[3,8])はTrueを返せる

## memo
@Kawauchi_Yusuke pytest fixture https://docs.pytest.org/en/latest/fixture.html#fixtures-as-function-arguments
:grinning:
2

twada:lion_face:  4:50 PM
@masafumi_hayashi エラーのテスト https://docs.pytest.org/en/latest/assert.html#assertions-about-expected-exceptions

https://github.com/tddbc/python_pytest

document(English) https://docs.pytest.org/en/latest/getting-started.html
