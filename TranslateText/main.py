# The following is a test of using Google's API to translate text
# 


# ================ IMPORTANT LINKS ===============
# get started - https://console.cloud.google.com/translation/dashboard?referrer=search&authuser=1&project=decisive-circle-291519 
# language support - https://cloud.google.com/translate/docs/languages?authuser=1
# how to create a key - https://cloud.google.com/translate/docs/setup?authuser=1#windows


import os


def main():
    # mapping object to access os and set key for google cloud API
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"key.json"

    # take text from user and set a default language
    text = input("Enter a word that will be translated to Spanish: ")
    target_lang = "es"

    # call translate text function which takes a target language and the text to be translated
    translate_text(target_lang, text)


# copied straight from google's tutorial
def translate_text(target, text):
    # six provides smoother support between python 2 and 3 - probably not needed
    import six
    # we are importing the google client cloud translate API
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    # the translate API only accepts utf-8 text
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # get ready to print the result
    result = translate_client.translate(text, target_language=target)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

main()