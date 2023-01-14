from talon import Module, Context

mod = Module()
ctx = Context()

repeat_num_list = "two three four five six seven eight nine".split()
repeat_num_map = {word: str(i + 2) for i, word in enumerate(repeat_num_list)}

mod.list("repeat_num", desc="List of numbers used for repeating")
ctx.lists["self.repeat_num"] = repeat_num_map  