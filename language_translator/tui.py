from dotenv import load_dotenv
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.reactive import reactive
from textual.widgets import (
    Header,
    Footer,
    TabbedContent,
    Markdown,
    Static,
    Label,
    Input,
    Button,
    Select,
    LoadingIndicator,
)

from language_translator.language_translator import GoogleTranslateAPI

HOME_MARKDOWN = """
# Welcome
This is a terminal based langauge translation app. see other tabs to try it out...
## Features
* Translate: convert text between different languages.
* Language Detection: detect the language of a query text.
* See available languages: See all the languages you can convert from or convert to.
"""

ABOUT_MARKDOWN = """
# About Language Translator
Language Translator is a terminal based translating app that uses google translate api for translation.

### Version
0.1.0

### License
MIT

### Author
* TIMMY

### Contributors
* Gbenga Adeyi [https://github.com/gray-adeyi](https://github.com/gray-adeyi)
"""
load_dotenv()
TRANSLATOR = GoogleTranslateAPI()


class TranslateTab(Static):
    def compose(self) -> ComposeResult:
        # TODO: layout
        yield Label(
            "Translates your input from your source language to target language"
        )

        yield Label("Input text")
        yield Input(id="input_text")

        yield Label("Source")
        yield Select((("en", "es"),))
        yield Label("Target")
        yield Select((("en", "es"),))

        yield Label("Format")
        yield Select((("en", "es"),))
        yield Label("Language Model")
        yield Select((("en", "es"),))

        yield Button(label="TRANSLATE", variant="success")


class DetectLanguageTab(Static):
    def compose(self) -> ComposeResult:
        # TODO: layout
        yield Label("Detect the langauge text provided")

        yield Label("Input")
        yield Input()

        yield Button("DETECT", variant="success")


class AvailableLanguageTab(Static):
    def compose(self) -> ComposeResult:
        # TODO: layout
        yield Label("See languages you can translate from or translate to")
        yield Button("SEE AVAILABLE LANGUAGES", variant="success")


class LanguageTranslator(App):
    """A textual app for GoogleTranslateAPI"""

    TITLE = "Langauge Translator"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets or the app."""
        yield Header()
        with TabbedContent(
            "Home", "Translate", "Detect a langauge", "Available languages", "About"
        ):
            yield Markdown(HOME_MARKDOWN)
            yield TranslateTab()
            yield DetectLanguageTab()
            yield AvailableLanguageTab()
            yield Markdown(ABOUT_MARKDOWN)
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.dark = not self.dark
