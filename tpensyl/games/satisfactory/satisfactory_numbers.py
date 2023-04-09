from talon import Module, Context

mod = Module()
ctx = Context()

mod.list("satisfactory_number_key", desc="Satisfactory build keys")

@mod.capture(rule="{self.satisfactory_number_key}")
def satisfactory_number_key(m) -> str:
    "One number key"
    return m.satisfactory_number_key
    
default_digits = "zero one two three four five six seven eight nine".split(" ")
numbers = [str(i) for i in range(10)]
number_key_dict = dict(zip(default_digits, numbers))
number_key_dict["ocho"] = "8"
number_key_dict["ladder"] = "9"
number_key_dict["belt"] = "1"
number_key_dict["power"] = "2"
number_key_dict["lift"] = "3"
number_key_dict["pipe"] = "4"
ctx.lists["self.satisfactory_number_key"] = number_key_dict 