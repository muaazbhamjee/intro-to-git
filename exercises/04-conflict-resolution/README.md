# Exercise 4: Conflict Resolution

## Goal

Deliberately create a merge conflict and resolve it — in the terminal and in VS Code.

## Setup

```bash
mkdir conflict-lab && cd conflict-lab
git init

cat > config.py << 'EOF'
"""Simulation configuration."""

VELOCITY = 1.0       # m/s
DENSITY = 1.225      # kg/m^3
VISCOSITY = 1.8e-5   # Pa.s
MAX_ITERATIONS = 1000
TOLERANCE = 1e-6
EOF

git add . && git commit -m "Initial config"
```

## Steps

### Part A — Create the conflict

```bash
# 1. Create branch A and change VELOCITY
git checkout -b experiment/high-speed
sed -i 's/VELOCITY = 1.0/VELOCITY = 10.0/' config.py
git add config.py
git commit -m "experiment: increase velocity to 10 m/s"

# 2. Go back to main and change the SAME line differently
git checkout main
sed -i 's/VELOCITY = 1.0/VELOCITY = 5.0/' config.py
git add config.py
git commit -m "update: set velocity to 5 m/s for validation"

# 3. Try to merge — this WILL conflict
git merge experiment/high-speed
```

You'll see:
```
Auto-merging config.py
CONFLICT (content): Merge conflict in config.py
Automatic merge failed; fix conflicts and then commit the result.
```

### Part B — Resolve in the terminal

```bash
# 4. See which files are conflicted
git status

# 5. Open the file — you'll see conflict markers
cat config.py
```

The file will contain something like:

```python
<<<<<<< HEAD
VELOCITY = 5.0       # m/s
=======
VELOCITY = 10.0      # m/s
>>>>>>> experiment/high-speed
```

```bash
# 6. Edit the file: pick the correct value (or combine)
#    Remove the <<<<<<< , ======= , and >>>>>>> markers
#    For example, choose 10.0:
nano config.py    # or your preferred editor

# 7. Stage the resolved file
git add config.py

# 8. Complete the merge
git commit -m "Resolve conflict: use velocity = 10 m/s"

# 9. Clean up
git branch -d experiment/high-speed
```

### Part C — Resolve in VS Code

Repeat the setup, but this time open the conflicted file in VS Code:

```bash
# Recreate the conflict (reset and repeat Part A steps)
# Then:
code .
```

1. VS Code will highlight the conflict in colour.
2. Click **Accept Current Change**, **Accept Incoming Change**, or **Accept Both**.
3. Or right-click → **Open in Merge Editor** for the 3-way view.
4. Stage and commit from the Source Control panel.

### Part D — Abort a merge

If you want to back out of a merge instead of resolving:

```bash
git merge --abort    # returns to the state before the merge
```

## Challenges

1. **Multi-file conflict:** Change the same line in two different files on two branches. Merge and resolve both.
2. **Three-way conflict:** Have three branches all modify the same function. Merge them sequentially into main, resolving each conflict.
3. **Rebase conflict:** Instead of `git merge`, try `git rebase main` from the feature branch. Resolve the conflict, then `git rebase --continue`.
4. **Use `git mergetool`:** Configure a visual merge tool (VS Code, meld, or kdiff3) with `git config --global merge.tool <tool>` and run `git mergetool`.
