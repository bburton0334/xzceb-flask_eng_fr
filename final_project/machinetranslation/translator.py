""" This file holds the functions to translate english to french, and french to english """

#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

def english_to_french(englishText):
    """ This function translates english to french """

    # if englishText is empty, return
    if not englishText:
        return englishText

    language_translator.set_service_url(url)
    frenchText = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()

    return frenchText

def french_to_english(frenchText):
    """ This function translates french to english """

    #if frenchText is empty, return
    if not frenchText:
        return frenchText

    language_translator.set_service_url(url)
    englishText = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()

    return englishText
