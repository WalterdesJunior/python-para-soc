ip = input("Escreva seu IP: ")

partes = ip.split(".")             # "172.20.5.5" vira ['172', '20', '5', '5']

if ip.startswith("10."):
    print("Privado")
elif ip.startswith("192.168."):
    print("Privado")
elif ip.startswith("172.") and 16 <= int(partes[1]) <= 31:
    print("Privado")
else:
    print("Público")