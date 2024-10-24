file_path = './books/frankenstein.txt'

with open(file_path, "r") as file:
    content = file.read()

count = 0
for c in content.split(' '):
     count += 1

# print(content)
print("total words", count)