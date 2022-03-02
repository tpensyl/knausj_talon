title:/.*Sumo Logic/
-

time slice: "| timeslice "
time slice <number_small> (day|days):
	"| timeslice {number_small}d "
time slice <number_small> (hour|hours):
	"| timeslice {number_small}h "
time slice <number_small> (minute|minutes):
	"| timeslice {number_small}m "
time slice <number_small> (second|seconds):
	"| timeslice {number_small}s "
count by: "| count by "
count by time slice: "| count by _timeslice "
count that by time slice:
	text = edit.selected_text()
	key(end)
	key(shift-enter)
	"| count by {text}, _timeslice "
	"| transpose row _timeslice column {text} "
transpose:
	"| transpose row _timeslice column "

(where|were): "| where "
parse: "| parse "
(as|ass) [<user.text>]: " as "

slap:
	edit.line_end()
	key(shift-enter)

(hard slap | run): key(enter)
source category: "_sourceCategory"
field time slice: "_timeslice"
field source host: "_sourceHost"