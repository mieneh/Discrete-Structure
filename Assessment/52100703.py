#-------------- Tìm một Modulo nghịch đảo n --------------#
#Thuật toán euclid mở rộng
def ExtEuclidean(a, n):
    n0 = n
    y = 0
    x = 1
    while a > 1:
        q = a // n
        a, n = n, a % n
        x, y = y, x - q * y
    if x < 0:
        x = x + n0
    return x
#Do người dùng nhập giá trị vào 
a = int(input("Nhập giá trị của a: "))
n = int(input("Nhập giá trị của n: "))
mod_inverse = ExtEuclidean(a, n)
#In kết quả ra màn hình
if mod_inverse is not None:
    print("Modulo nghịch đảo của {} mod {} là: {}".format(a, n, mod_inverse))
else:
    print("{} và {} không phải là số nguyên tố cùng nhau, vì vậy không tồn tại phép modulo nghịch đảo.".format(a, n))


#-------------- Hệ thống mật mã RSA --------------#
import math
#Bước 1: Chọn hai số nguyên tố lớn (ở bước này em sẽ chọn mặc định số 61 và 52)
p = 61
q = 53
#Bước 2: Tính n = p * q
n = p * q
#Bước 3: Chọn giá trị cho e (public key) (ở bước này em sẽ chọn mặc định số 17)
e = 17
#Step 4: Tính d bằng Thuật toán Euclide mở rộng (private key)
phi_n = (p-1) * (q-1)
d = ExtEuclidean(e, phi_n)
#Bước 5: Xác định chức năng mã hóa và giải mã
#Chức năng mã hóa tin nhắn
def encrypt(message, n, e):
    encrypted_msg = []
    for char in message:
        #Chuyển đổi ký tự thành giá trị ASCII
        char_ascii = ord(char)
        #Áp dụng công thức mã hóa RSA: C = M^e mod n
        encrypted_char = pow(char_ascii, e, n)
        encrypted_msg.append(encrypted_char)
    return encrypted_msg
#Chức năng giải mã tin nhắn
def decrypt(encrypted_msg, n, d):
    decrypted_msg = ""
    for char_ascii in encrypted_msg:
        #Áp dụng công thức giải mã RSA: M = C^d mod n
        decrypted_char = pow(char_ascii, d, n)
        #Chuyển đổi giá trị ASCII thành ký tự
        decrypted_char = chr(decrypted_char)
        decrypted_msg += decrypted_char
    return decrypted_msg
#Bước 6: Mã hóa và Giải mã tin nhắn
#Tin nhắn được mã hóa
message = (input("Nhập tin nhắn cần mã hóa: "))
#Mã hóa tin nhắn
encrypted_message = encrypt(message, n, e)
print("Mã hóa tin nhắn:", encrypted_message)
#Giải mã tin nhắn
decrypted_message = decrypt(encrypted_message, n, d)
print("Giải mã tin nhắn:", decrypted_message)