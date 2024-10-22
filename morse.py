class Translator():
    def toMorse(self,msg):
        message_in_morse = ''
        letters = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'..-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', '?':'..--..', '!':'-.-.--', '.':'.-.-.-', ',':'--..--', ' ':' '}
        for letter in msg:
            try:
                message_in_morse += letters[letter.lower()]
            except:
                message_in_morse += '#'
            message_in_morse += ' '
        return message_in_morse
    def fromMorse(self,msg):
        letters = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', '--..':'z', '.----':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8', '----.':'9', '-----':'0', '..--..':'?', '-.-.--':'!', '.-.-.-':'.', '--..--':',', '   ':' ', ';':' '}
        message_in_english = ''
        message_words = msg.split('   ')
        print(message_words)
        for word in message_words:
            letters_in_word = word.split(' ')
            for letter in letters_in_word:
                try:
                    message_in_english += letters[letter]
                except:
                    message_in_english += '#'
            message_in_english += ' '
        return message_in_english

if __name__ == "__main__":
    translator = Translator()
    msg = input("Enter message to translate to morse: ")
    print(translator.toMorse(msg))
    msg = input("Enter message in morse to translate to English: ")
    print(translator.fromMorse(msg))