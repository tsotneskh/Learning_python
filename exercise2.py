seconds = int(input("შეიყვანეთ წამების რაოდენობა: "))
hours = seconds//3600
something1 = seconds %3600
minutes = something1 // 60
second = something1 %60
print (hours,"საათი", minutes, "წუთი ", second, "წამი")
