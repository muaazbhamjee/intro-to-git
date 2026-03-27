# Exercise 5: GitHub CLI (`gh`)

## Goal

Use the `gh` CLI to manage repos, pull requests, issues, and authentication — all from the terminal.

## Prerequisites

- `gh` installed (`gh --version`)
- Authenticated (`gh auth status`)

If not authenticated yet:

```bash
gh auth login
# Choose: GitHub.com → HTTPS → Login with a web browser
```

## Steps

### Part A — Repo management

```bash
# 1. Create a new repo and clone it
gh repo create gh-practice --public --clone --add-readme
cd gh-practice

# 2. View repo info
gh repo view

# 3. Open in browser
gh repo view --web

# 4. List your repos
gh repo list --limit 5
```

### Part B — Issues

```bash
# 5. Create issues
gh issue create --title "Add unit tests" --body "We need pytest tests for all functions." --label "enhancement"
gh issue create --title "Fix divide by zero" --body "The divide function crashes on zero input." --label "bug"

# 6. List open issues
gh issue list

# 7. View a specific issue
gh issue view 1

# 8. Close an issue
gh issue close 2 --comment "Fixed in commit abc1234"

# 9. Reopen
gh issue reopen 2
```

### Part C — Branches and pull requests

```bash
# 10. Create a branch and make changes
git checkout -b feature/add-tests

cat > test_calculator.py << 'EOF'
"""Unit tests for the calculator."""

def test_add():
    assert 2 + 2 == 4

def test_subtract():
    assert 5 - 3 == 2
EOF

git add test_calculator.py
git commit -m "test: add basic unit tests"
git push -u origin feature/add-tests

# 11. Create a PR
gh pr create \
  --title "Add unit tests" \
  --body "Closes #1. Adds basic pytest tests." \
  --base main

# 12. List PRs
gh pr list

# 13. View PR details
gh pr view 1

# 14. View PR diff
gh pr diff 1

# 15. Merge the PR
gh pr merge 1 --squash --delete-branch

# 16. Pull the merged changes
git checkout main
git pull
```

### Part D — Advanced `gh` usage

```bash
# 17. Check auth status and scopes
gh auth status

# 18. Refresh token with additional scopes (if needed)
gh auth refresh --scopes repo,read:org

# 19. Use gh as a credential helper for git
gh auth setup-git

# 20. Create a release
git tag v0.1.0
git push --tags
gh release create v0.1.0 --title "v0.1.0" --notes "Initial test release"

# 21. View the release
gh release view v0.1.0

# 22. Clone someone else's repo
gh repo clone cli/cli    # clones GitHub's own CLI repo
```

### Part E — Useful shortcuts

```bash
# Open current repo in browser
gh browse

# Open a specific file in browser
gh browse test_calculator.py

# Open the issues page
gh browse --issues

# Open the PR page
gh browse --pulls

# View your notifications
gh api /notifications --jq '.[].subject.title'
```

## Challenges

1. **Issue-to-PR workflow:** Create an issue, create a branch that references it, push, create a PR that says "Closes #N", merge it, and verify the issue auto-closes.
2. **Fork and PR:** Use `gh repo fork` to fork a public repo, make a change, and submit a PR.
3. **Custom aliases:** Create a `gh` alias for a common workflow:
   ```bash
   gh alias set pr-ready 'pr create --fill --web'
   gh pr-ready   # opens a pre-filled PR in the browser
   ```
4. **API exploration:** Use `gh api` to fetch data from the GitHub API:
   ```bash
   gh api /user   # your profile
   gh api /repos/{owner}/{repo}/contributors   # repo contributors
   ```
