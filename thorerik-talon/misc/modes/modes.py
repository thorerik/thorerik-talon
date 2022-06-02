from talon import Context, Module, actions, app
from talon.grammar import Phrase
from typing import Union

mod_nor = Module()
mod_nor.tag("norwegian")

mod_ger = Module()
mod_ger.tag("german")

ctx = Context()

ctx_norwegian = Context()
ctx_norwegian.matches = r"""
tag: user.norwegian
"""

ctx_norwegian.settings = {
    "speech.engine": "webspeech",
    "speech.language": "nb_NO",
}

ctx_german = Context()
ctx_german.matches = r"""
tag: user.german
"""

ctx_german.settings = {
    "speech.engine": "webspeech",
    "speech.language": "de_DE",
}



@mod_nor.action_class
class Actions:
    def command_mode(phrase: Union[Phrase, str] = None):
        """Enter command mode and re-evaluate phrase"""
        ctx.tags = []
        actions.mode.disable("dictation")
        actions.mode.enable("command")
        if phrase:
            actions.user.rephrase(phrase, run_async=True)

    def dictation_mode(phrase: Union[Phrase, str] = None):
        """Enter dictation mode and re-evaluate phrase"""
        actions.user.dictation_format_reset()
        actions.mode.disable("command")
        actions.mode.enable("dictation")
        if phrase:
            actions.user.rephrase(phrase, run_async=True)

    def norwegian_mode(phrase: Union[Phrase, str] = None):
        """Enter norwegian dictation mode and re-evaluate phrase"""
        ctx.tags = ["user.norwegian"]
        actions.user.dictation_mode(phrase)

    def mixed_mode(phrase: Union[Phrase, str] = None):
        """Enter mixed mode and re-evaluate phrase"""
        actions.user.dictation_format_reset()
        actions.mode.enable("dictation")
        if phrase:
            actions.user.rephrase(phrase, run_async=True)


@mod_ger.action_class
class Actions:
    def command_mode(phrase: Union[Phrase, str] = None):
        """Enter command mode and re-evaluate phrase"""
        ctx.tags = []
        actions.mode.disable("dictation")
        actions.mode.enable("command")
        if phrase:
            actions.user.rephrase(phrase, run_async=True)

    def dictation_mode(phrase: Union[Phrase, str] = None):
        """Enter dictation mode and re-evaluate phrase"""
        actions.user.dictation_format_reset()
        actions.mode.disable("command")
        actions.mode.enable("dictation")
        if phrase:
            actions.user.rephrase(phrase, run_async=True)

    def german_mode(phrase: Union[Phrase, str] = None):
        """Enter norwegian dictation mode and re-evaluate phrase"""
        ctx.tags = ["user.german"]
        actions.user.dictation_mode(phrase)

    def mixed_mode(phrase: Union[Phrase, str] = None):
        """Enter mixed mode and re-evaluate phrase"""
        actions.user.dictation_format_reset()
        actions.mode.enable("dictation")
        if phrase:
            actions.user.rephrase(phrase, run_async=True)

# Disable face mode
app.register("ready", lambda: actions.mode.disable("face"))