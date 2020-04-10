import section
import pytest

# 作成
class Test_２つの整数を引数に閉区間オブジェクトをつくる:
    def test_3から8の閉区間を作れる(self):
        x=section.Section(3,8)
        assert [3,8] == x.val
    def test_3から8の閉区間を作れる(self):
        x=section.Section(3,3)
        assert [3,3] == x.val

# 作成(例外処理)
class Test_整数以外では閉区間オブジェクトをつくれない:
    def test_小数3_1から8_1の閉区間は作れない(self):
        with pytest.raises(ValueError):
            x=section.Section(3.1,8.1)

    def 文字列_あ_や_い_では閉区間は作れない(self):
        try:
            x=section.Section("あ","い")
            assert False
        except:
            assert True

class Test_始点の方が大きい閉区間は作れない:
    def test_8から3の閉区間は作れない(self):
        try:
            x=section.Section(8,3)
            assert False
        except:
            assert True

# 文字列表現を返す
class Test_閉区間オブジェクトは文字列表現を返す:
    def test_3から8の閉区間の文字列表現を返せる(self):
        x=section.Section(3,8)
        #assert isinstance(x.toString(),str)
        assert str([3,8]) == x.toString()

class Test_閉区間オブジェクトは指定した整数を含むかどうかを判定できる:
    def test_2は3から8の閉区間には含まれない(self):
        x=section.Section(3,8)
        assert (not x.num_in(2))

    def test_3は3から8の閉区間には含まれる(self):
        x=section.Section(3,8)
        assert (x.num_in(3))

    def test_8は3から8の閉区間には含まれる(self):
        x=section.Section(3,8)
        assert (x.num_in(8))

    def test_9は3から8の閉区間には含まれる(self):
        x=section.Section(3,8)
        assert (not x.num_in(9))

class Test_閉区間オブジェクトは別の閉区間と等価かどうかを判定できる:
    
    def test_3から8の閉区間と3から8の閉区間は等価(self):
        x=section.Section(3,8)
        y=section.Section(3,8)
        assert x.equal(y)
    
    def test_3から8の閉区間と4から8の閉区間は等価(self):
        x=section.Section(3,8)
        y=section.Section(4,8)
        assert (not x.equal(y))
