from talon import Module, Context

mod = Module()
mod.tag("game_repeater", desc="tag for enabling repeater commands")

ctx = Context()
ctx.matches = r"""
tag: user.game_repeater
"""
