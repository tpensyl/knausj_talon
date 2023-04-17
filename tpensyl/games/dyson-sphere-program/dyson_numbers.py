from talon import Module, Context

mod = Module()
ctx = Context()

mod.list("dyson_number_key", desc="Dyson build keys")

@mod.capture(rule="{self.dyson_number_key}")
def dyson_number_key(m) -> str:
    "One number key"
    return m.dyson_number_key

default_digits = "one two three four five six seven eight nine ten eleven twelve".split(" ")
numbers = [str(i) for i in range(1, 12+1)]
number_key_dict = dict(zip(default_digits, numbers))
ctx.lists["self.dyson_number_key"] = number_key_dict 