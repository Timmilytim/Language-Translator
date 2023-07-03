import os
from typing import Optional

import httpx

from language_translator.utils import HTTPMethod, Language, Format, LanguageModel


# try:
#     print("------ WELCOME TO TIMMY'S LANGUAGE TRANSLATOR------")
#     while True:
#         print("1. TRANSLATOR \n" "2. AVAILABLE LANGUAGE CODES \n" "3. Exit")
#         option = input(">>> ")
#         if option == "1":
#             try:
#                 url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
#
#                 sentence = str(input("Enter Sentence: "))
#                 language = str(input("Enter Language Code: "))
#                 payload = {"q": sentence, "target": language, "source": "en"}
#                 headers = {
#                     "content-type": "application/x-www-form-urlencoded",
#                     "Accept-Encoding": "application/gzip",
#                     "X-RapidAPI-Key": "16d35def64msh61682f7697de9a3p1ec241jsnedffd87d0759",
#                     "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
#                 }
#                 response = httpx.get(url, headers=headers, params=sentence)
#                 response = httpx.post(url, data=payload, headers=headers)
#                 betterView = json.loads(response.text)["data"]["translations"][0][
#                     "translatedText"
#                 ]
#
#                 print("TRANSLATION: ", betterView, " \n")
#             except KeyError:
#                 print(
#                     "LANGUAGE NOT AVAILABLE....\n",
#                     "GO TO THE 'LANGUAGE CODES' OPTION BELOW TO CHECK OUT THE CODES AVAILABLE LANGUAGES.... \n",
#                 )
#         elif option == "2":
#             print(
#                 """ SOME JARGONS I'M STILL WORKING ON...\n\n
# 			"""
#             )
#         elif option == "3":
#             print("Exiting...")
#             exit(0)
#         else:
#             print("WRONG INPUT \n" "TRY AGAIN.... \n")
# except httpx.ConnectError:
#     print(" Make sure you are Connected to the internet...")


class GoogleTranslateAPI:
    API_KEY_ENV_NAME = "X_RAPID_API_KEY"

    def __init__(
        self,
        api_key: Optional[str] = None,
    ):
        if api_key:
            self.api_key = api_key
        else:
            self.api_key = os.getenv(self.API_KEY_ENV_NAME)
        if not self.api_key:
            raise ValueError(
                f"api_key not provided and {self.API_KEY_ENV_NAME} not set in environmental variables"
            )

    def _api_call(
        self, end_point: str, method: HTTPMethod, data: Optional[dict | list] = None
    ):
        http_method_call_kwargs = self._parse_call_kwargs(
            end_point=end_point,
            data=data,
            method=method,
        )
        http_methods_mapping = {
            HTTPMethod.GET: httpx.get,
            HTTPMethod.POST: httpx.post,
        }
        http_method_callable = http_methods_mapping.get(method)
        if not http_method_callable:
            raise ValueError(f"{method} is not a supported HTTP method")
        try:
            response = http_method_callable(**http_method_call_kwargs)
            return response.json()
        except httpx.ConnectError:
            raise ValueError(
                "Unable to connect to server. Please ensure you have an internet connection"
            )
        except (httpx.ConnectTimeout, httpx.ReadTimeout):
            raise ValueError("Server refused to respond")

    def _parse_call_kwargs(
        self, end_point: str, data: Optional[dict | list], method: HTTPMethod
    ):
        kwargs = {
            "url": self._base_url + end_point,
            "data": data,
            "headers": self._headers,
        }
        if method == HTTPMethod.GET:
            kwargs.pop("data")
        return kwargs

    @property
    def _headers(self) -> dict:
        return {
            "Accept-Encoding": "application/json",
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com",
        }

    @property
    def _base_url(self):
        return "https://google-translate1.p.rapidapi.com/language/translate/v2"

    def detect(self, query: str):
        """detects the language of the provided query string"""
        data = {"q": query}
        return self._api_call(end_point="/detect", method=HTTPMethod.POST, data=data)

    def languages(self):
        return self._api_call(end_point="/languages", method=HTTPMethod.GET)

    def translate(
        self,
        query: str,
        target: Language,
        format: Format = Format.TEXT,
        source: Language = Language.EN,
        model: LanguageModel = LanguageModel.NMT,
    ):
        data = {
            "q": query,
            "target": target.value,
            "format": format.value,
            "source": source.value,
            "model": model.value,
        }
        return self._api_call(end_point="", method=HTTPMethod.POST, data=data)
