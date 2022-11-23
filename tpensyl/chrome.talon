tag: browser
app: chrome
-

(okta|octa): key(alt-o)
(okta|octa) <user.text>:
	key(alt-o)
	sleep(400ms)
	"{text}"
	sleep(400ms)
	key(enter)

#go m v <user.number_string>:
#	app.tab_open()
#	browser.go("https://bandwidth-jira.atlassian.net/browse/MV-{number_string}")
