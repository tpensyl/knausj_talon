title: /.*Jira/
-
log work:
    key('.')
    sleep(1100ms)
    "log\n"

[log] date: key(tab:2)

[log] type:
    key(enter)
    key(tab:9)

([log] done | hard slap):
    key(tab)
    key(enter)
