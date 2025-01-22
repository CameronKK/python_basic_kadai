class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def check_adult(self):
    if self.age >= 20:
      print (f"{self.name}さんは大人です。")
    else:
      print(f"{self.name}さんは大人ではありません。")

user_info = {
  "侍一郎": 36,
  "侍花子": 19,
  "侍次郎": 50,
  "侍三郎": 16
}

humans_list = []

for name, age in user_info.items():
  human =Human(name, age)
  humans_list.append(human)
  
for human in humans_list:
  human.check_adult()