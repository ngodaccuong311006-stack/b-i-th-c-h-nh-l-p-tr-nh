print("sinh viên: ngô đắc cường")
print("msv: 245752021610035")
passwords = input("Nhập mật khẩu: ").split(",")
valid = []

for p in passwords:
    if len(p) < 6 or len(p) > 12:
        continue

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for ch in p:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in "$#@":
            has_special = True

    if has_lower and has_upper and has_digit and has_special:
        valid.append(p)

print(",".join(valid))
