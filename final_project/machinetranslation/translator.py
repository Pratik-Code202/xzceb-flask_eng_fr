'''
wrwfr
'''

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
model_id = 'en-fr'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')

language_translator.set_disable_ssl_verification(True)

def englishToFrench(englishText):
    '''
    wrwfr
    '''
    #write the code here
    text_to_translate = englishText
    frenchText = language_translator.translate(
    text=text_to_translate,
    model_id=model_id).get_result()

    return frenchText['translations'][0]['translation']


def frenchToEnglish(frenchText):
    '''
    wrwfr
    '''
    #write the code here
    text_to_translate = frenchText
    englishText = language_translator.translate(
    text=text_to_translate,
    model_id='fr-en').get_result()

    return englishText['translations'][0]['translation']

