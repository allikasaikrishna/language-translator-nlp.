from deep_translator import GoogleTranslator

text = input("Enter text: ")
source = input("Source language code (en, te, hi): ")
target = input("Target language code (en, te, hi): ")

translated = GoogleTranslator(source=source, target=target).translate(text)
print("Translated Text:", translated)
