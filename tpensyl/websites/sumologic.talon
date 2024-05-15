title: /.*Sumo Logic/
-

index V two: "_index=msg_api "
index argo: "_index=argo_infrequent"

time slice: "| timeslice "
time slice <number_small> (day | days): "| timeslice {number_small}d "
time slice <number_small> (hour | hours): "| timeslice {number_small}h "
time slice <number_small> (minute | minutes): "| timeslice {number_small}m "
time slice <number_small> (second | seconds): "| timeslice {number_small}s "
count by: "| count by "
count distinct [by]:
    "| count_distinct() by "
    key(left:5)
count by time slice: "| count by _timeslice "
count that by time slice:
    text = edit.selected_text()
    key(end)
    key(shift-enter)
    "| count by {text}, _timeslice "
    "| transpose row _timeslice column {text} "
transpose: "| transpose row _timeslice column "
concat:
    "| concat() as "
    key(left:5)

comment [line]:
    key(home)
    "//"

(where | were): "| where "
parse:
    '| parse ""'
    key(left)
(as | ass) [<user.text>]: " as "

slap:
    edit.line_end()
    key(shift-enter)

(hard slap | run [that]): key(enter)
[field] source category: "_sourceCategory"
field time slice: "_timeslice"
[field] source host: "_sourceHost"
[field] source name: "_sourceName"
field count: "_count"

no drop: " nodrop "