print("Welcome to the caesar cypher")
ask_the_user = input("Do you want to encrypt or decrypt(press 0 for encrypt and press 1 for decrypt): ").lower()
shifting = int(input("How may letters do you want to shift: "))
if ask_the_user == '0':
    list_of_encrypting_words = []
    what_word = input("What word do you want to encrypt: ").lower()
    for i in what_word:
        list_of_encrypting_words.append(i)
    res = [ord(ele) for sub in list_of_encrypting_words for ele in sub]
    for i in range(len(res)):
        res[i] = res[i]+shifting
    result_string = ''.join(chr(value) for value in res)
    print(result_string)
elif ask_the_user == '1':
    list_of_encrypting_words = []
    what_word = input("What word do you want to encrypt: ").lower()
    for i in what_word:
        list_of_encrypting_words.append(i)
    res = [ord(ele) for sub in list_of_encrypting_words for ele in sub]
    for i in range(len(res)):
        res[i] = res[i]-shifting
    result_string = ''.join(chr(value) for value in res)
    print(result_string)
else:
    print("Write the correct input")
