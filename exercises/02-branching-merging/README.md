# Exercise 2: Branching & Merging

## Goal

Learn to create branches, switch between them, and merge changes.

## Setup

Use the repo from Exercise 1, or create a fresh one:

```bash
mkdir branch-practice && cd branch-practice
git init
echo "# Branch Practice" > README.md
git add . && git commit -m "Initial commit"
```

## Steps

### Part A — Create and use a branch

```bash
# 1. See current branches
git branch

# 2. Create a new branch
git branch feature/greeting

# 3. Switch to it
git checkout feature/greeting
# (or in one step: git checkout -b feature/greeting)

# 4. Verify you're on the new branch
git branch    # asterisk shows current branch

# 5. Create a new file on this branch
cat > greet.py << 'EOF'
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
EOF

# 6. Commit
git add greet.py
git commit -m "feat: add greeting function"
```

### Part B — Make a parallel change on main

```bash
# 7. Switch back to main
git checkout main

# 8. Notice greet.py does NOT exist here
ls    # only README.md

# 9. Add something to main
echo "This project demonstrates Git branching." >> README.md
git add README.md
git commit -m "docs: expand README"
```

### Part C — Merge

```bash
# 10. Merge the feature branch into main
git merge feature/greeting

# 11. Check — both changes are now on main
ls              # README.md AND greet.py
cat README.md   # has the expanded text
git log --oneline --graph
```

### Part D — Clean up

```bash
# 12. Delete the merged branch
git branch -d feature/greeting

# 13. Verify
git branch    # only main remains
```

## Visual check

```bash
git log --oneline --graph --all
```

You should see a fork-and-merge pattern in the graph.

## Challenges

1. **Multiple branches:** Create two feature branches from main, commit different files on each, then merge both back into main one at a time.
2. **Branch from a branch:** Create `feature/a`, commit, then create `feature/b` from `feature/a`. Merge `feature/a` into main first, then `feature/b`.
3. **Use VS Code:** Open the repo in VS Code. Use the branch indicator (bottom-left) to create and switch branches. Use the Source Control panel to stage, commit, and see the diff.
4. **Try `git log --graph`:** After multiple merges, inspect the history graph.
