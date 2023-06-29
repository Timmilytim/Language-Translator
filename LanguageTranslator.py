import googletrans
import httpcore
from googletrans import Translator
import time

# The function below allows users to search based on the language key and the language itself then it translates
# It also checks if the language key exists in the key list and if the language is in the value list
def trans_index(language, value, keys, sentence):
    if len(language) > 2:
        if language in value:
            idx = value.index(language)
            key = keys[idx]

            trans_late = translator.translate(sentence, dest=key).text
            print("Long Language", key)
            print(trans_late)

        else:
            print("\nThe selected Language doesn't exist\n"
                  "Check the available language in the 'AVAILABLE LANGUAGE CODES' section.\n")
    else:
        if language in keys:
            key = language
            trans_late = translator.translate(sentence, dest=key).text
            print(trans_late)

        else:
            print("\nThe selected language key doesn't exist\n"
                  "Check the available language code in the 'AVAILABLE LANGUAGE CODES' section.\n")


def main():
    if option == 1:
        speaker = input("Are you an English speaker? - YES or NO -\n-> ").lower()
        try:
            if speaker == "yes":  # Speaker understands english
                sentence = input("Enter a sentence to be translated.\n-> ")
                language = input("Enter your preferred translation.\n-> ").lower()
                trans_index(language, Value, Keys, sentence)

            elif speaker == "no":  # Speaker does not understand english
                sentence = input("Enter a sentence to be translated.\n-> ")
                de_tect = translator.detect(sentence)
                if de_tect.lang in Keys:
                    idx = Keys.index(de_tect.lang)
                    language = Value[idx]
                    print(f"Detected language is {language.upper()}")
                else:
                    print('Language not detected!!')
                language = input("Enter your preferred translation.\n-> ").lower()
                trans_index(language, Value, Keys, sentence)
            select = input("Do you want to make another translation? - YES - NO -\n-> ")
            if select == "yes":
                pass
            else:
                print("Exiting program....")
                time.sleep(1)
                exit(0)
        except httpcore.ConnectError:
            print("\nPLEASE CONNECT TO THE INTERNET AND RERUN THE PROGRAM!!!!")
            time.sleep(1)
            exit(0)

    elif option == 2:
        print(f"Available Languages are {len(Keys)}\nPlease wait for the available languages to load...\n")
        time.sleep(2)
        for i in range(len(Keys)):
            print(f"{Keys[i]} -------- {Value[i]}")
            time.sleep(0.05)
        print(f"\nA total of {len(Keys)} languages....")
        time.sleep(1)

    elif option == 3:
        print("Exiting program....")
        exit(0)

    else:
        print("Incorrect input please check for the correct option and try again!!!")


translator = Translator()
LANGUAGES = googletrans.LANGUAGES

Keys = list(LANGUAGES.keys())
Value = list(LANGUAGES.values())

checks = True

while True:
    try:
        option = int(input("""
_____ WELCOME TO TIMI'S LANGUAGE TRANSLATOR _____
1. TRANSLATE
2. AVAILABLE LANGUAGE CODES
3. EXIT
-> """))
        main()
    except ValueError:
        print("\nIncorrect input please check for the correct option and try again!!!")
        time.sleep(1)
