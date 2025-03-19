empty dub string:
    user.deprecate_command("2024-11-24", "empty dub string", "quad")
    user.insert_between('"', '"')

empty string:
    user.deprecate_command("2024-11-24", "empty string", "twin")
    user.insert_between("'", "'")

empty escaped string:
    user.deprecate_command("2024-11-24", "empty escaped string", "escaped twin")
    user.insert_between("\\'", "\\'")

inside (parens | args):
    user.deprecate_command("2024-11-24", "inside (parens | args)", "round")
    user.insert_between("(", ")")

inside (braces | curly brackets):
    user.deprecate_command("2024-11-24", "inside (braces | curly brackets)", "curly")
    user.insert_between("{", "}")

inside (quotes | string):
    user.deprecate_command("2024-11-24", "inside (quotes | string)", "twin")
    user.insert_between("'", "'")

inside (double quotes | dub quotes):
    user.deprecate_command("2024-11-24", "inside (double quotes | dub quotes)", "quad")
    user.insert_between('"', '"')

inside (graves | back ticks):
    user.deprecate_command("2024-11-24", "inside (graves | back ticks)", "skis")
    user.insert_between("`", "`")

