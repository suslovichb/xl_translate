from googletrans import Translator

translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

def clear_format(text):
    text = text.replace('</ ', '</')
    return text

print(clear_format(translator.translate(['<h3> Купить </h3>'], dest='uk')[0].text))
