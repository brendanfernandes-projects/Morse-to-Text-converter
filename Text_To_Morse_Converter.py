morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
         'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
         'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
         '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
         '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
         ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
         '$': '...-..-', '@': '.--.-.', ' ': '/'}
morse_code = ''
try:
    option = int(input('Type "1" to encode or type "2" to decode: '))
    if option == 1:
        text = str(input('Enter the text you want to convert into morse-code: ').strip()).upper()
        for i in text:
            morse_code += (morse[i] + ' ')
        print(morse_code)
    if option == 2:
        text = ''
        code = input('Enter the morse-code you want to convert into text: ').strip().split(' ')
        for alphabet in code:
            for key, value in morse.items():
                if value == alphabet:
                    text += key
        if text=='':
            print('Enter a Valid morse')
        else:
            print(text)
except ValueError:
    print("Enter a valid number.")


