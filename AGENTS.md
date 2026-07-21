# AGENTS.md

## Architecture

- **`keyboard.vil`** — Canonical source layout (4 Vial layers). **Do NOT modify directly** unless changing the base layer.
- **`make_mac_win_vil.py`** — Reads `keyboard.vil`, generates `keyboard-mac-win.vil` with Mac/Windows dual-system layout.
- **`keyboard-mac-win.vil`** — Generated output. Always regenerate via script, never hand-edit.
- **`keyboard.vil copy`** — Backup file, not part of the build.

## Layer layout

| Layer | keyboard.vil | keyboard-mac-win.vil |
|---|---|---|
| 0 | Base | Mac base (Cmd/Option swapped) |
| 1 | Fn + RGB | Mac Fn + arrows (HJKL) + nav (UIOP) + overrides |
| 2 | Transparent | Windows base |
| 3 | Transparent | Windows Fn (same as Mac Fn, M=DF(0) instead of DF(2)) |

## Workflow

```
# 1. Modify layout (source of truth only)
edit keyboard.vil

# 2. Regenerate Mac/Win variant
python3 make_mac_win_vil.py

# 3. Commit both
git add keyboard.vil keyboard-mac-win.vil && git commit
```

## Rules

- **`keyboard.vil` is read-only for Fn layer changes.** All Fn-layer adjustments (Esc/Backspace/Y overrides, nav keys, modifier swaps) go in the script, not in `keyboard.vil`.
- **`.vil` files are single-line JSON.** Use `python3 -c "import json; ..."` to read/write — never string-replace on these files.
- **Run `make_mac_win_vil.py` after every `keyboard.vil` change** before committing.
- **No build/test/lint tooling.** Pure data + script repo. Verification is manual inspection of generated output.
