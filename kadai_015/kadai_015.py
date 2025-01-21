class Human:
  #コンストラクタの定義
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  #メソッドの定義
  def printinfo(self):
    print(f"Name: {self.name}, Age: {self.age}")
  
#インスタンス化
taro = Human("侍太郎", 36)

#メソッドの呼び出し
taro.printinfo()