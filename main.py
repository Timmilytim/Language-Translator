from language_translator.language_translator import GoogleTranslateAPI
from language_translator.tui import LanguageTranslator
from language_translator.utils import Language

if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    app = LanguageTranslator()
    app.run()
