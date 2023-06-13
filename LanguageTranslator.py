import json
import requests

try:
	print("------ WELCOME TO TIMMY'S LANGUAGE TRANSLATOR------")
	while True:
		option = input("1. TRANSLATOR\n2. AVAILABLE LANGUAGE CODES\n3. Exit\n-> ")

		if option == "1":	# First Option for the Translation
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
