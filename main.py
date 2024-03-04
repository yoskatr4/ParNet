import subprocess


print('''
Sesli (Voice)  [1]
Yazılı (Text)   [2]
''')
a = int(input(""))
if a == 1:
    subprocess.run(["python", "voice.py"])
elif a == 2:
    subprocess.run(["python", "text_main.py"])