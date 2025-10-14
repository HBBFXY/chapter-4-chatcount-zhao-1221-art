s = input()
letter = 0
digit = 0
space = 0
other = 0
for ch in s:
  if ch.isalpha():
    letter += 1
  elif ch.isdigit():
    digit += 1
  elif ch.isspace():
    space += 1
  else:
    other += 1
print(f'英文字符:{letter}')
print(f'数字:{digit}')
print('空格:{space}')
print(f'其他:{other}')
