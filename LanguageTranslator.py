from googletrans import Translator
import json
import requests


def timi():
	try:
		print("------ WELCOME TO TIMMY'S LANGUAGE TRANSLATOR------")
		while True:
			option = input("1. TRANSLATOR\n2. AVAILABLE LANGUAGE CODES\n3. Exit\n-> ")

			if option == "1":		# First Option for the Translation
				try:
					url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

					sentence = str(input("Enter Sentence: "))
					language = str(input("Enter Language Code: "))
					payload = {
						"q": sentence,
						"target": language,
						"source": "en"
					}
					headers = {
						"content-type": "application/x-www-form-urlencoded",
						"Accept-Encoding": "application/gzip",
						"X-RapidAPI-Key": "16d35def64msh61682f7697de9a3p1ec241jsnedffd87d0759",
						"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
					}
					response = requests.request("GET", url, headers=headers, params=sentence)
					response = requests.post(url, data=payload, headers=headers)
					betterView = json.loads(response.text)["data"]["translations"][0]["translatedText"]

					print("TRANSLATION: ", betterView, " \n")
				except KeyError:
					print("LANGUAGE NOT AVAILABLE....\n",
						  "GO TO THE 'LANGUAGE CODES' OPTION BELOW TO CHECK OUT THE CODES AVAILABLE LANGUAGES.... \n" )

			elif option == "2":		# Available Language code
				print('''SOME JARGONS I'M STILL WORKING ON...\n\n
				''')

			elif option == "3":		# Exit option
				print("Exiting...")
				exit(0)

			else:
				print("WRONG INPUT \n"
					  "TRY AGAIN.... \n")
	except requests.exceptions.ConnectionError:
		print("Make sure you are Connected to the internet...")


"""
BEGINNING OF PROGRAM
	Welcome user to our translation portal
	Then ask what they wanna do
		1. Translate
		2. View Available Langs
		3. Exit

if input is 1 (Translate)...
	- Ask if the individual is an english speaker if yes...
		- FOR TRANSLATION FROM ENGLISH:
			- Collect user input in ENGLISH
			- Ask user to type in the Language the want to translate to
				- if preferred lang is > 2
				- preferred lang.lower() then check if Language exists in the list of Languages
				- If it exists in the lang.values() get the corresponding key in the lang.Keys()
			- Then perform translation

	- If individual isn't an English speaker			
		- FOR DETECTING LANGUAGES (use the .detect()):
			- Collect user input in desired language
			- Ask user to type in the Language the want to translate to
			- Check if Language exists in the list of Languages
			- If it does perform translation

if input is 2 (View available Langs)...
	- Prompt user that the available languages are len(Keys) in total
	- Print loading language translations
	- Use a time.sleep(2)
	- Print the available langs and their keys
	- Tell user that they can also use the Keys directly
"""


def OG():
	translator = Translator()
	LANGUAGES = {
		'af': 'afrikaans',
		'sq': 'albanian',
		'am': 'amharic',
		'ar': 'arabic',
		'hy': 'armenian',
		'az': 'azerbaijani',
		'eu': 'basque',
		'be': 'belarusian',
		'bn': 'bengali',
		'bs': 'bosnian',
		'bg': 'bulgarian',
		'ca': 'catalan',
		'ceb': 'cebuano',
		'ny': 'chichewa',
		'zh-cn': 'chinese (simplified)',
		'zh-tw': 'chinese (traditional)',
		'co': 'corsican',
		'hr': 'croatian',
		'cs': 'czech',
		'da': 'danish',
		'nl': 'dutch',
		'en': 'english',
		'eo': 'esperanto',
		'et': 'estonian',
		'tl': 'filipino',
		'fi': 'finnish',
		'fr': 'french',
		'fy': 'frisian',
		'gl': 'galician',
		'ka': 'georgian',
		'de': 'german',
		'el': 'greek',
		'gu': 'gujarati',
		'ht': 'haitian creole',
		'ha': 'hausa',
		'haw': 'hawaiian',
		'iw': 'hebrew',
		'he': 'hebrew',
		'hi': 'hindi',
		'hmn': 'hmong',
		'hu': 'hungarian',
		'is': 'icelandic',
		'ig': 'igbo',
		'id': 'indonesian',
		'ga': 'irish',
		'it': 'italian',
		'ja': 'japanese',
		'jw': 'javanese',
		'kn': 'kannada',
		'kk': 'kazakh',
		'km': 'khmer',
		'ko': 'korean',
		'ku': 'kurdish (kurmanji)',
		'ky': 'kyrgyz',
		'lo': 'lao',
		'la': 'latin',
		'lv': 'latvian',
		'lt': 'lithuanian',
		'lb': 'luxembourgish',
		'mk': 'macedonian',
		'mg': 'malagasy',
		'ms': 'malay',
		'ml': 'malayalam',
		'mt': 'maltese',
		'mi': 'maori',
		'mr': 'marathi',
		'mn': 'mongolian',
		'my': 'myanmar (burmese)',
		'ne': 'nepali',
		'no': 'norwegian',
		'or': 'odia',
		'ps': 'pashto',
		'fa': 'persian',
		'pl': 'polish',
		'pt': 'portuguese',
		'pa': 'punjabi',
		'ro': 'romanian',
		'ru': 'russian',
		'sm': 'samoan',
		'gd': 'scots gaelic',
		'sr': 'serbian',
		'st': 'sesotho',
		'sn': 'shona',
		'sd': 'sindhi',
		'si': 'sinhala',
		'sk': 'slovak',
		'sl': 'slovenian',
		'so': 'somali',
		'es': 'spanish',
		'su': 'sundanese',
		'sw': 'swahili',
		'sv': 'swedish',
		'tg': 'tajik',
		'ta': 'tamil',
		'te': 'telugu',
		'th': 'thai',
		'tr': 'turkish',
		'uk': 'ukrainian',
		'ur': 'urdu',
		'ug': 'uyghur',
		'uz': 'uzbek',
		'vi': 'vietnamese',
		'cy': 'welsh',
		'xh': 'xhosa',
		'yi': 'yiddish',
		'yo': 'yoruba',
		'zu': 'zulu'}

	Keys = list(LANGUAGES.keys())
	Value = list(LANGUAGES.values())

	option = int(input("""
_____ WELCOME TO TIMI'S LANGUAGE TRANSLATOR _____
	1. TRANSLATE
	2. AVAILABLE LANGUAGE CODES
	3. EXIT"""))

	if option == 1:
		speaker = input("Are you an English speaker?\n-> ")
		if speaker.lower() == "yes":
			sentence = input("Enter a sentence to be translated.\n-> ")
			language = input("Enter your preferred translation.\n-> ").lower()
			# print(len(language))
			if len(language) > 2:
				if language in Value:
					idx = Value.index(language)
					key = Keys[idx]
					# print(key)
					# Translation goes here
				else:
					print("Doesn't exist")
			else:
				if language in Keys:
					key = language
					# print(key)
					# Translation goes here
				else:
					print("Doesn't exist")
		elif speaker.lower() == "no":
			"""LANGUAGE DETECT"""
			# use the translator.detect()





# for i in range(len(Keys)):
	# print(list(Keys)[i], "---", list(Value)[i])

# print(len(Keys))

# OG()

# LANGUAGES = {
# 		'af': 'afrikaans',
# 		'sq': 'albanian',
# 		'am': 'amharic',
# 		'ar': 'arabic',
# 		'hy': 'armenian',
# 		'az': 'azerbaijani',
# 		'eu': 'basque',
# 		'be': 'belarusian',
# 		'bn': 'bengali',
# 		'bs': 'bosnian',
# 		'bg': 'bulgarian',
# 		'ca': 'catalan',
# 		'ceb': 'cebuano',
# 		'ny': 'chichewa',
# 		'zh-cn': 'chinese (simplified)',
# 		'zh-tw': 'chinese (traditional)',
# 		'co': 'corsican',
# 		'hr': 'croatian',
# 		'cs': 'czech',
# 		'da': 'danish',
# 		'nl': 'dutch',
# 		'en': 'english',
# 		'eo': 'esperanto',
# 		'et': 'estonian',
# 		'tl': 'filipino',
# 		'fi': 'finnish',
# 		'fr': 'french',
# 		'fy': 'frisian',
# 		'gl': 'galician',
# 		'ka': 'georgian',
# 		'de': 'german',
# 		'el': 'greek',
# 		'gu': 'gujarati',
# 		'ht': 'haitian creole',
# 		'ha': 'hausa',
# 		'haw': 'hawaiian',
# 		'iw': 'hebrew',
# 		'he': 'hebrew',
# 		'hi': 'hindi',
# 		'hmn': 'hmong',
# 		'hu': 'hungarian',
# 		'is': 'icelandic',
# 		'ig': 'igbo',
# 		'id': 'indonesian',
# 		'ga': 'irish',
# 		'it': 'italian',
# 		'ja': 'japanese',
# 		'jw': 'javanese',
# 		'kn': 'kannada',
# 		'kk': 'kazakh',
# 		'km': 'khmer',
# 		'ko': 'korean',
# 		'ku': 'kurdish (kurmanji)',
# 		'ky': 'kyrgyz',
# 		'lo': 'lao',
# 		'la': 'latin',
# 		'lv': 'latvian',
# 		'lt': 'lithuanian',
# 		'lb': 'luxembourgish',
# 		'mk': 'macedonian',
# 		'mg': 'malagasy',
# 		'ms': 'malay',
# 		'ml': 'malayalam',
# 		'mt': 'maltese',
# 		'mi': 'maori',
# 		'mr': 'marathi',
# 		'mn': 'mongolian',
# 		'my': 'myanmar (burmese)',
# 		'ne': 'nepali',
# 		'no': 'norwegian',
# 		'or': 'odia',
# 		'ps': 'pashto',
# 		'fa': 'persian',
# 		'pl': 'polish',
# 		'pt': 'portuguese',
# 		'pa': 'punjabi',
# 		'ro': 'romanian',
# 		'ru': 'russian',
# 		'sm': 'samoan',
# 		'gd': 'scots gaelic',
# 		'sr': 'serbian',
# 		'st': 'sesotho',
# 		'sn': 'shona',
# 		'sd': 'sindhi',
# 		'si': 'sinhala',
# 		'sk': 'slovak',
# 		'sl': 'slovenian',
# 		'so': 'somali',
# 		'es': 'spanish',
# 		'su': 'sundanese',
# 		'sw': 'swahili',
# 		'sv': 'swedish',
# 		'tg': 'tajik',
# 		'ta': 'tamil',
# 		'te': 'telugu',
# 		'th': 'thai',
# 		'tr': 'turkish',
# 		'uk': 'ukrainian',
# 		'ur': 'urdu',
# 		'ug': 'uyghur',
# 		'uz': 'uzbek',
# 		'vi': 'vietnamese',
# 		'cy': 'welsh',
# 		'xh': 'xhosa',
# 		'yi': 'yiddish',
# 		'yo': 'yoruba',
# 		'zu': 'zulu'}

""" """
# seun = "google.com"
# lst = [i for i in seun]
# nlst = set(lst)
# for i in nlst:
# 	print(i, "-----", lst.count(i))

# print(nlst)