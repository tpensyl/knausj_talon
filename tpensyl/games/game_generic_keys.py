from talon import Module, Context

mod = Module()
mod.tag("game_generic_keys", desc="tag for enabling explicit key commands")

ctx = Context()
ctx.matches = r"""
tag: user.game_generic_keys
"""
