tag: browser
app: chrome
-

^(okta | octa): key(alt-o)
(okta | octa) <user.text>: user.open_okta_extension("{text}")
(okta | octa) (sumo|sumologic): user.open_okta_extension("sumologic")
# amazon=shared accounts, aws=glorg
(okta | octa) (amazon|a w s): user.open_okta_extension("amazon")
(okta | octa) (glorg): user.open_okta_extension("global org")

# made this a global command instead
#go m v <user.number_string>:
#    app.tab_open()
#    browser.go("https://bandwidth-jira.atlassian.net/browse/MV-{number_string}")
