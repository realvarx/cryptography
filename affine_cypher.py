def egcd(a, b):
    lastremainder, remainder = abs(a), abs(b)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if a < 0 else 1), lasty * (-1 if b < 0 else 1)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def encriptar(texto, a, b):

    # E(x) = ax + b mod26

    textoCifrado = ""

    for x in texto:

        if x.isupper():

            index = ord(x) - ord('A')
            nuevo = chr((a*index + b) % 26 + ord('A'))
            textoCifrado += nuevo

        elif x.islower():

            index = ord(x) - ord('a') 
            nuevo = chr((a*index + b) % 26 + ord('a'))
            textoCifrado += nuevo

        elif x.isdigit():

            nuevo = (a*int(x) + b) % 10
            textoCifrado += str(nuevo)

        else:
            textoCifrado += x

    return textoCifrado

def desencriptar(texto, a, b):

    # D(y) = (y − b)a^-1 mod26

    textoDescifrado = ""

    for x in texto:

        if x.isupper(): 

            index = ord(x) - ord('A') 
            original = chr(modinv(a, 26)*(index - b) % 26 + ord('A'))
            textoDescifrado += original

        elif x.islower(): 

            index = ord(x) - ord('a') 
            original = chr(modinv(a, 26)*(index - b) % 26 + ord('a'))
            textoDescifrado += original

        elif x.isdigit():

            original = modinv(a, 26)*(int(x) - b) % 10
            textoDescifrado += str(original)

        else:
            textoDescifrado += x

    return textoDescifrado

def main():
    a = 19
    b = 23

    textoAlicia = """yxbvhnitcxctkodirautjxuxrqtekjdkdjtcxjdrdjtqvibv
hnitcxcvbvyaivxivyxjtdkxcxjdkyxtkodirautjxlyxuvy
vrautjxpnvbvvkodjxvkyxwiduvjjtokcvyxtkoixvbuinju
nix jdrwnuxjtdkxyludcdydgtkjnyxcdjdkyxrtbrxlvbwv
jtxyrvkuvyxtkodirxjtokjdkuvktcxvknkxjdrwnuxcdixd
jtijnyxkuvxuixgebcvyxbivcvbcvjdrwnuxcdixbwxixvyy
dvstbuvknkxbvitvcvvbuakcxivbwidudjdydbreudcdbivh
yxbaviixrtvkuxblyvlvbjdkjvqtcxbwxixrtktrtexiydbw
dbtqyvbitvbhdbxyxtkoixvbuinjunixldxyxwidwtxtkodi
rxjtokyx jtqvibvhnitcxcjdrwivkcvbdouzxivqxbvbcvc
xudbrvuxcxudbxijatgdbaxiczxivivcvbcvjdrwnuxcdixb
ludcdydpnvyxdihxktexjtokvkutvkcxlgxydivjdrdnkitv
bhdbtyxtkodirxjtokjdkotcvkjtxytkgdynjixcxwnctvix
yyvhxixrxkdbcvduixbwvibdkxbwdivmvrwydjdkgtiutekc
dbvxbivktkodirxjtokwitgtyvhtxcx
"""
    textoDesencriptado = desencriptar(textoAlicia, a, b)
    print("\n- TEXTO DESCIFRADO - \n\n" + textoDesencriptado)

    textoEncriptado = encriptar(textoDesencriptado, a, b)
    print("¿Son el texto original y el encriptado el mismo? : " + str(textoAlicia == textoEncriptado))

    salir = input("\nPresiona enter para salir")

if __name__ == '__main__':
    main()