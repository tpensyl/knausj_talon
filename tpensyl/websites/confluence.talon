app.name: /Google Chrome/
win.doc: /https://bandwidth-jira.atlassian.net/*/
#win.title: /Edit.*Confluence.*/
-

# maybe should just be the same file as JIRA, currently they're basically both matching same thing?
bullet: key(cmd-shift-8)
strike through: key(cmd-shift-S)
italics: key(cmd-i)
bold: key(cmd-b)
link: key(ctrl-k)
paste link:
    key(ctrl-k)
    sleep(30ms)
    edit.paste()
    sleep(30ms)
    key(enter)