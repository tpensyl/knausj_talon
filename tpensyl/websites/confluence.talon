app.name: /Google Chrome/
win.doc: /https://bandwidth-jira.atlassian.net/*/
#win.title: /Edit.*Confluence.*/
-

# maybe should just be the same file as JIRA, currently they're basically both matching same thing?

link: key(ctrl-k)
paste link:
    key(ctrl-k)
    sleep(30ms)
    edit.paste()
    sleep(30ms)
    key(enter)

#bold: key(cmd-b)