a = 10
b = 20
c = a + b
print(c)

# List
l = [1, 2, 3, 4]
print(l)

# ถ้าเราต้องการที่จะดูค่าใน List ตัวแรก เราจะอ้างอิงโดยเริ่มจาก Index ที่ 0
print(l[0])

# Tuple
my_tuple = (1, "hello", 3.14)
print(my_tuple)
print(my_tuple[1])

# Dict
d = {
    "a": 1,
    "b": 2,
}
print(d)

# คำสั่งในการดึงค่าของแต่ละ Key ทำได้ 2 แบบ
print(d["a"])
print(d.get("a"))

# Set
my_set = set()
my_set.add(10)
my_set.add(10)