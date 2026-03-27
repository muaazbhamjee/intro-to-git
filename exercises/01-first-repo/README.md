# Exercise 1: Your First Repository

## Goal

Create a Git repository from scratch, make commits, and push to GitHub.

## Prerequisites

- Git installed (`git --version`)
- GitHub account
- Authentication set up (SSH key or `gh auth login`)

## Steps

### Part A — Create and initialise

```bash
# 1. Create a project folder
mkdir my-first-repo && cd my-first-repo

# 2. Initialise Git
git init

# 3. Check status (should say "No commits yet")
git status
```

### Part B — First commit

```bash
# 4. Create a README
echo "# My First Repo" > README.md
echo "Learning Git for the first time." >> README.md

# 5. Stage the file
git add README.md

# 6. Check status again — README should be green (staged)
git status

# 7. Commit
git commit -m "Initial commit: add README"

# 8. View the log
git log --oneline
```

### Part C — Add a .gitignore

```bash
# 9. Create a Python file and some junk
echo 'print("hello")' > hello.py
mkdir __pycache__
echo "bytecode" > __pycache__/hello.cpython-312.pyc

# 10. Create a .gitignore
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.env
EOF

# 11. Stage and commit both files
git add .
git status    # __pycache__ should NOT appear
git commit -m "Add hello.py and .gitignore"
```

### Part D — Push to GitHub

```bash
# Option 1: Using gh (easiest)
gh repo create my-first-repo --public --source=. --push

# Option 2: Manual
# - Create a repo on github.com (DON'T initialise with README)
# - Then:
git remote add origin git@github.com:YOUR-USERNAME/my-first-repo.git
git push -u origin main
```

### Part E — Verify

```bash
# Open in browser
gh repo view --web
# or visit https://github.com/YOUR-USERNAME/my-first-repo
```

## Challenges

1. **Add more files:** Create a `notes.txt`, stage, and commit it.
2. **Selective staging:** Edit both `README.md` and `hello.py`, but only commit the README change. Then commit the `hello.py` change separately.
3. **View the diff:** Before staging, run `git diff` to see what changed.
4. **Amend a commit:** Make a typo in a commit message, then fix it with `git commit --amend`.
