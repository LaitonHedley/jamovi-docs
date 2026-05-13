Coordinate parallel documentation work across multiple independent sections.

Tasks: $ARGUMENTS

If no tasks are specified, ask the user what sections they want to work on and what should be done to each.

Steps:
1. Parse the arguments into a list of independent tasks, each tied to a specific file or section.
2. Confirm the task list with the user before proceeding if anything is ambiguous.
3. For each task, spawn a sub-agent with `isolation: "worktree"`. Brief each agent to:
   - Read `CLAUDE.md` first for project context, audience, and RST conventions
   - Complete the specified task
   - Run `source .venv/bin/activate && make html` and note any warnings or errors
4. Run all agents in parallel.
5. Report back for each task: the worktree branch, a short summary of what changed, and whether the build passed.
