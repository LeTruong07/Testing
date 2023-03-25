task = input()
shift = int(input())
rotor1 = input()
rotor2 = input()
rotor3 = input()
message = input()
answer = ''
APB = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if task == 'ENCODE':
    for i in range(len(message)):
        shifted_char = APB[(APB.index(message[i]) + shift + i) % 26]
        rotor1_index = APB.index(shifted_char)
        rotor2_index = APB.index(rotor1[rotor1_index])
        rotor3_index = APB.index(rotor2[rotor2_index])
        encrypted_char = APB[APB.index(rotor3[rotor3_index])]
        answer += encrypted_char
elif task == 'DECODE':
    for i in range(len(message)):
        char = message[i]
        rotor3_index = rotor3.index(char)
        rotor2_index = rotor2.index(APB[rotor3_index])
        rotor1_index = rotor1.index(APB[rotor2_index])
        decrypted_char = APB[(APB.index(APB[rotor1_index]) - shift - i) % 26]
        answer += decrypted_char
print(answer)
