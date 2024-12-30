tag: user.draft_editor_active
and tag: user.draft_editor_app_focused
-

(draft submit|draft save): 
    # put in clipboard only as backup
    edit.select_all()
    edit.copy()
    user.draft_editor_submit()
draft discard: user.draft_editor_discard()
