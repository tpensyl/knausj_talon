app: vscode
-
box run above: user.vscode("notebook.cell.executeCellsAbove")
box run: user.vscode("notebook.cell.executeAndFocusContainer")
(cell | box) (del | delete): 
	user.vscode("notebook.cell.quitEdit")
	user.vscode("notebook.cell.delete")