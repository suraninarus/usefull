from collections import Counter

path = r"C:\Users\Zsolt\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\names.txt"
counter = 0
with open(path, "r", encoding="UTF-8") as names:
    content_of_names = names.readlines()
    for name in content_of_names:
        # print(name)
        counter += 1

print(counter)