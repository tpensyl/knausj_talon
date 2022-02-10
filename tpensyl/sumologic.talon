title:/.*Sumo Logic/
-

count by: "| count by "
(where|were): "| where "
parse: "| parse "
(as|ass) [<user.text>]: " as "

slap: key(shift-enter)
run: key(enter)
source category: "_sourceCategory"
time slice: "_timeslice"