



















# เขียนโปรแกรม นับจํานวนอักขระที่สนใจในข้อความที่กําหนดโดยผู้ใช้
# 1. รับข้อความที่กําหนดให้จากผู้ใช้ (text)
# 2. รับอักขระที่สนใจจากผู้ใช้ (char)
# 3. แสดงผลการนับอักขระที่สนใจในข้อความออกทางหน้าต่าง

# ตัวอย่างหน้าจอ
# Insert the text:
# character to find: r
# 3 letter 'r' found in 'Kasetsart Sriracha'


print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input(Insert the text:)
text = input(character to find: r)
"""print("\n=== ITERATING THROUGH STRING ===")
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in ' {text}'")"""

#เขียนโปรแกรม ตรวจสอบความแข็งแรงของ password
# password ที่แข็งแรงคือ ยาวมากกว่า 8ตัว และผสมระหว่างกับตัวเลข ตัวอักษร และอัขระพิเศษ

# ตัวอย่างหน้าจอ
# Insert your password: Test123
# Your password is not strong

# Insert your password: Test1234;
# Your password is strong

password = input("Insert your password: ")
lenght = len(password)
check = password.isalnum()

if lenght > 8 and check == False:
    print("Your password is strong!")
else:
    print("Your password is not strong!")