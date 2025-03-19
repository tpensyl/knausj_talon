new line: "\n"
double dash: "--"
triple quote: "'''"
triple grave | triple back tick | gravy: "```"
(dot dot | dotdot): ".."
ellipsis: "..."
(comma and | spamma): ", "
arrow: "->"
left arrow: "<-"
dub arrow: "=>"
empty dub string: user.insert_between('"', '"')
empty escaped (dub string | dub quotes): user.insert_between('\\"', '\\"')
empty string: user.insert_between("'", "'")
empty escaped string: user.insert_between("\\'", "\\'")
(inside parens | args): user.insert_between("(", ")")
args right: "()"
args dot: "()."
inside (squares): user.insert_between("[", "]")
square args: user.insert_between("[", "]")
# inside (angles): user.insert_between("<", ">")
# inside (bracket | braces): user.insert_between("{", "}")
# inside percent: user.insert_between("%", "%")
# inside (quotes | string): user.insert_between("'", "'")
# inside (double quotes | dub quotes): user.insert_between('"', '"')
inside (graves | back ticks): user.insert_between("`", "`")
# angle that:
#     text = edit.selected_text()
#     user.paste("<{text}>")
# (square | bracket | square bracket) that:
#     text = edit.selected_text()
#     user.paste("[{text}]")
# (brace | curly bracket) that:
#     text = edit.selected_text()
#     user.paste("{{{text}}}")
# (parens | args) that:
#     text = edit.selected_text()
#     user.paste("({text})")
# percent that:
#     text = edit.selected_text()
#     user.paste("%{text}%")
# quote that:
#     text = edit.selected_text()
#     user.paste("'{text}'")
# (double quote | dub quote) that:
#     text = edit.selected_text()
#     user.paste('"{text}"')
(grave | back tick) that:
    text = edit.selected_text()
    user.paste("`{text}`")

# Insert delimiter pairs
# tpensyl: inside or empty?
inside <user.delimiter_pair>: user.delimiter_pair_insert(delimiter_pair)

#tpensyl TODO replaces some of above commands??
# Wrap selection with delimiter pairs
<user.delimiter_pair> wrap that: user.delimiter_pair_wrap_selection(delimiter_pair)
