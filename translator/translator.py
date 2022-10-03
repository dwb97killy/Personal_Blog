from googletrans import Translator

def tranlation(input):
    translator = Translator()
    output = translator.translate(text=input, src='en', dest='zh-cn')
    print(output.text)
    return output.text