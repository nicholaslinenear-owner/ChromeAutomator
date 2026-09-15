# Quick Reference - File Sync

One-page guide for ChromeAutomator file sync automation.

## 🚀 Setup (5 minutes)

```bash
# 1. Initialize sync
bash scripts/setup-file-sync.sh

# 2. Configure (optional)
vim .sync-config.json

# 3. Start watching
python scripts/sync-files.py watch
```

## 📁 Directory Structure

Your local directories automatically sync to repo:

```
~/projects/       → repo/src/projects/
~/configs/        → repo/config/
~/scripts/        → repo/scripts/
~/docs_local/     → repo/docs/local/
```

## 🔄 Commands

```bash
# Preview files to sync
python scripts/sync-files.py scan

# One-time sync
python scripts/sync-files.py sync

# Watch continuously (recommended)
python scripts/sync-files.py watch

# Init configuration
python scripts/sync-files.py init
```

## ⚙️ Configuration

Edit `.sync-config.json`:

```json
{
  "watch_directories": ["./projects", "./configs"],
  "include_patterns": ["*.py", "*.md"],
  "exclude_patterns": ["*.pyc", "__pycache__"],
  "sync_interval": 300,
  "auto_commit": true
}
```

## 📊 Features

✅ Auto-sync on file change
✅ Smart pattern matching
✅ Only syncs changed files (hash-based)
✅ Auto-commits to git
✅ Tracks sync history in `.sync-meta/`
✅ CI/CD integration (GitHub Actions)

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Files not syncing | Run `python scripts/sync-files.py scan` |
| Watch directories missing | Run `bash scripts/setup-file-sync.sh` |
| Auto-commit failing | Check git config: `git config user.name` |
| Too slow/fast | Edit `sync_interval` in `.sync-config.json` |

## 📖 Full Docs

- `docs/FILE_SYNC.md` - Complete guide
- `.sync-config.json.example` - All config options
- `scripts/sync-files.py --help` - Script help

## 💡 Pro Tips

```bash
# Sync only Python files
# Edit .sync-config.json:
# "include_patterns": ["*.py", "*.md"]

# Faster sync (every minute)
# Edit .sync-config.json:
# "sync_interval": 60

# Disable auto-commit
# Edit .sync-config.json:
# "auto_commit": false
```

---

**Next:** `python scripts/sync-files.py watch`
