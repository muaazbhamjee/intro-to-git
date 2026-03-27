# Exercise 3: Collaboration

## Goal

Practise the collaborative workflow: clone, branch, push, and open a pull request.

## Setup

Work in pairs if possible. If working solo, you'll simulate collaboration using a GitHub repo and the web UI.

## Steps

### Part A — Set up a shared repo

**Person A** (or solo):

```bash
# 1. Create a repo with a starter file
mkdir collab-demo && cd collab-demo
git init
cat > calculator.py << 'EOF'
"""A simple calculator module."""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b
EOF

git add . && git commit -m "feat: add and subtract functions"

# 2. Push to GitHub
gh repo create collab-demo --public --source=. --push
```

**Person A:** Add Person B as a collaborator:
GitHub → repo Settings → Collaborators → Add people.

### Part B — Clone and branch

**Person B** (or simulate by cloning into a different directory):

```bash
# 3. Clone the repo
git clone git@github.com:PERSON-A-USERNAME/collab-demo.git collab-demo-b
cd collab-demo-b

# 4. Create a feature branch
git checkout -b feature/multiply

# 5. Add a new function
cat >> calculator.py << 'EOF'

def multiply(a, b):
    """Return the product of a and b."""
    return a * b
EOF

# 6. Commit and push the branch
git add calculator.py
git commit -m "feat: add multiply function"
git push -u origin feature/multiply
```

### Part C — Open a pull request

```bash
# 7. Create a PR with gh
gh pr create \
  --title "Add multiply function" \
  --body "Adds a multiply() function to the calculator module."
```

Or do it on github.com: you'll see a banner to open a PR for the recently pushed branch.

### Part D — Review and merge

**Person A** reviews:

```bash
# 8. List and view the PR
gh pr list
gh pr view 1

# 9. Check out the PR locally to test
gh pr checkout 1
python3 -c "from calculator import multiply; print(multiply(3, 4))"

# 10. Approve and merge
gh pr merge 1 --squash --delete-branch
```

### Part E — Stay in sync

**Person B** updates their local main:

```bash
git checkout main
git pull origin main
git log --oneline    # should include the merged commit
```

## Challenges

1. **Fork workflow:** Instead of being added as a collaborator, Person B forks the repo, clones their fork, pushes to the fork, and opens a PR from the fork to the original.
2. **Add a `divide` function** via a new PR. Include a check for division by zero.
3. **Review on GitHub:** Leave a comment on the PR, request changes, then approve.
4. **Try in VS Code:** Install the "GitHub Pull Requests and Issues" extension. Create and review PRs directly inside VS Code.
