from talon import Context, Module, actions, settings
from typing import Union
from talon.grammar import Phrase

ctx = Context()
mod = Module()
ctx.matches = r"""
tag: user.java
"""


@mod.action_class
class Actions:
    def declare_mock(name: Union[str, Phrase]):
        "declare a class-level mock variable"
        type = actions.user.reformat_text(name, "hammer")
        var = actions.user.reformat_text(name, "camel") 
        result = "private final {} {} = mock({}.class);".format(type, var, type)
        actions.insert(result)