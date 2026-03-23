# BinaryTest/test04.py

ip_addr = input("ip 주소 입력: ")

ip_parts = ip_addr.split(".")

print(ip_parts)

binary_parts = []
for item in ip_parts:
    print(f"{int(item):08b}")
    
    binary_parts.append(f"{int(item):08b}")

print(binary_parts)

result = ".".join(binary_parts)

print(result)

print(f"입력한 ip: {ip_addr}")
print(f"2진수 변환 한 ip: {result}")