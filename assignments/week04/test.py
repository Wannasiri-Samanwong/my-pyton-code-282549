# รับข้อมูล "ชื่อจริง (เป็นภาษาอังกฤษ)" จากผู้ใช้
# นับจํานวนสระในข้อความดังกล่าว

# ตัวอย่างหน้าจอ
# What is your name?: Wannasiri
# You have 4 vowel in your tex

# name = input("What is your name?:")
name = "Wannasiri"
letters = list(name)
print(letters)
counter = 0

for char in letters:
    if char == 'a': or char == 'A':
        counter = counter + 1

    elif char =='e': or char == 'E':
        counter = counter + 1

    elif char =='i': or char == 'I':
        counter = counter + 1

    elif char =='o': or char == 'O': 
         counter = counter + 1

    elif char =='u': or char == 'U': 
         counter = counter + 1

a = letter.count('a')
e = letter.count('e')
i = letter.count('i')
o = letter.count('o')
u = letter.count('u')


A = letter.count('A')
E = letter.count('E')
I = letter.count('I')
O = letter.count('O')
U = letter.count('U')

vowels = a + e + i + o + u

    print("You have", counter, "vowels in your text.")
    print(f"You have {vowels} vowels in your text.")