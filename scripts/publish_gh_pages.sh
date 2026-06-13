#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
source_dir="${1:-$repo_root/.files}"
branch="${GH_PAGES_BRANCH:-gh-pages}"
message="${GH_PAGES_COMMIT_MESSAGE:-Update generated downloads}"

if [[ ! -d "$source_dir" ]]; then
  echo "Missing source directory: $source_dir" >&2
  exit 1
fi

if [[ ! -f "$source_dir/index.html" ]]; then
  echo "Missing $source_dir/index.html. Run scripts/generate_download_html.py first." >&2
  exit 1
fi

tmpdir="$(mktemp -d "${TMPDIR:-/tmp}/archive-test-files-gh-pages.XXXXXX")"
cleanup() {
  if git -C "$repo_root" worktree list --porcelain | grep -Fq "worktree $tmpdir"; then
    git -C "$repo_root" worktree remove --force "$tmpdir" >/dev/null 2>&1 || true
  else
    rm -rf "$tmpdir"
  fi
}
trap cleanup EXIT

if git -C "$repo_root" show-ref --verify --quiet "refs/heads/$branch"; then
  git -C "$repo_root" worktree add "$tmpdir" "$branch" >/dev/null
else
  git -C "$repo_root" worktree add --detach "$tmpdir" >/dev/null
  git -C "$tmpdir" switch --orphan "$branch" >/dev/null
fi

find "$tmpdir" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
rsync -a --delete --exclude .git "$source_dir"/ "$tmpdir"/

git -C "$tmpdir" add -A

if git -C "$tmpdir" diff --cached --quiet; then
  echo "No changes to publish on $branch"
else
  git -C "$tmpdir" commit -m "$message"
fi

echo "Published .files contents to $branch without switching $(git -C "$repo_root" branch --show-current)"
