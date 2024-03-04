import subprocess


print('''
Türkçe  [1]
İngilizce   [2]
''')
a = int(input(""))
if a == 1:
    subprocess.run(["python", "tr.py"])
elif a == 2:
    subprocess.run(["python", "eng.py"])