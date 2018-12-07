from google.cloud import translate
import os
credential_path = 'Fill your path to json google key'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def translation(text, target='en'):
	translate_client = translate.Client()
	result = translate_client.translate(text, target_language=target)
	return result


# input_ = input('Enter the content you want to translate:')
# while  input_ !='quit':
# 	translation(input_, target='en')
# 	input_ = input('Enter the content you want to translate:')
# print('Bye')