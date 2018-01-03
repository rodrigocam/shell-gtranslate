from googletrans import Translator


translator = Translator()

def translate(text, src_lng=None, dest_lng=None):
    if src_lng and dest_lng:
        translated = translator.translate(text, src=src_lng, dest=dest_lng)
    elif src_lng:
        translated = translator.translate(text, src=src_lng)
    elif dest_lng:
        translated = translator.translate(text, dest=dest_lng)
    else:
        translated =  translator.translate(text)

    return translated