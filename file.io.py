file = open("Task.txt","w+")
noi = int(input("Enter the no.of lines: "))
list1 = []
for i in range(noi):
    data = input("Enter the data: ")
    list1.append(data)
    file.write(data + '\n')
c = file.read()
print(c)
file.close()
file2 = open("dummy.txt","w+")
for j in list1[::-1]:
    file2.write(j + '\n')
h = file2.read()
print(h)
file2.write('\n')
file2.write("Replaced data")
file2.write('\n')
g = input('Do you want to replace Any word or Sentences(Yes/No): ')
lst = []
if g == 'Yes' or g == 'yes':
    a = " ".join(list1)
    word = input('Enter the Word you want to replace: ')
    if word in a:
        a.find(word)
        replce = input(f'replace {word} with: ')
        b = a.replace(word, replce)
        c = b.split(' ')
        lst.append(c)
        file2.write(b)
        print(f"{word} word is replaced with {replce}please check the dummy file to find the Replacements")
    else:
        print(f'{word} not found\nplease try again.')
else:
    print('Enter the correct')
file2.close()