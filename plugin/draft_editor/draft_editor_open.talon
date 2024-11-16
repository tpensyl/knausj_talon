tag: user.draft_editor_active
and tag: user.draft_editor_app_focused
-

(draft submit|run that|draft save): 
    # put in clipboard only as backup
    user.copy_all()
    user.draft_editor_submit()
draft discard: user.draft_editor_discard()
