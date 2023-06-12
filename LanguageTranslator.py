import json
import requests

try:
	print("------ WELCOME TO TIMMY'S LANGUAGE TRANSLATOR------")
	while True:
		print("1. TRANSLATOR \n"
			  "2. AVAILABLE LANGUAGE CODES \n"
			  "3. Exit")
		option = input(">>> ")
		if option == "1":
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
		elif option == "2":
			print(''' SOME JARGONS I'M STILL WORKING ON...\n\n
			''')
		elif option == "3":
			print("Exiting...")
			exit(0)
		else:
			print("WRONG INPUT \n"
				  "TRY AGAIN.... \n")
except requests.exceptions.ConnectionError:
	print(" Make sure you are Connected to the internet...")
