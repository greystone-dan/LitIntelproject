# AI-Friendly Dev Environment — Setup Guide

Document role: environment bootstrap and workstation setup.
After setup, use `OVERNIGHT.md` for unattended run operations and `DOCS_INDEX.md` for documentation authority.

> **Goal:** Get your machine ready so Microsoft Copilot (and GitHub Copilot) can directly read, understand, and edit code inside your project. This guide covers every step from a clean machine to a fully connected AI dev workspace.

---

## Table of Contents

1. [Prerequisites Overview](#1-prerequisites-overview)
2. [Install Python 3.11+](#2-install-python-311)
3. [Install PostgreSQL](#3-install-postgresql)
4. [Install pgvector Extension](#4-install-pgvector-extension)
5. [Install VS Code](#5-install-vs-code)
6. [Clone & Configure the Project](#6-clone--configure-the-project)
7. [Connect Copilot to Your Project](#7-connect-copilot-to-your-project)
8. [Verify Everything Works](#8-verify-everything-works)
9. [Troubleshooting](#9-troubleshooting)
10. [Overnight Processing](#10-overnight-processing)

---

## 1. Prerequisites Overview

| Tool | Minimum Version | Purpose |
|---|---|---|
| Python | 3.11 | Application runtime & AI libraries |
| PostgreSQL | 15 | Relational database |
| pgvector | 0.7 | Vector similarity search inside Postgres |
| VS Code | Latest | Editor with Copilot integration |
| Git | 2.40 | Version control |
| GitHub Account | — | Required for GitHub Copilot |

---

## 2. Install Python 3.11+

### Windows
1. Download the installer from **python.org → Downloads → Windows**.
2. Run the installer. **Check "Add Python to PATH"** before clicking Install.
3. Verify:
   ```
   python --version
   pip --version
   ```

### macOS
```bash
# Using Homebrew (recommended)
brew install python@3.11
echo 'export PATH="/opt/homebrew/opt/python@3.11/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
python3.11 --version
```

### Ubuntu / Debian
```bash
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3.11-dev python3-pip
python3.11 --version
```

### Create a Virtual Environment (do this inside your project folder)
```bash
python -m venv .venv

# Activate — Windows:
.venv\Scripts\activate

# Activate — macOS/Linux:
source .venv/bin/activate

# Install project dependencies
pip install -r requirements.txt
```

> **Tip:** Always activate the virtual environment before running any project commands.

---

## 3. Install PostgreSQL

### Windows
1. Download the installer from **postgresql.org → Downloads → Windows**.
2. Run the installer, choose version **15 or 16**.
3. Remember the **superuser (postgres) password** you set — you'll need it.
4. After install, add the PostgreSQL `bin` folder to your PATH (e.g., `C:\Program Files\PostgreSQL\15\bin`).
5. Verify:
   ```
   psql --version
   ```

### macOS
```bash
brew install postgresql@15
brew services start postgresql@15
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
psql --version
```

### Ubuntu / Debian
```bash
sudo apt install -y postgresql postgresql-contrib
sudo systemctl enable postgresql
sudo systemctl start postgresql
psql --version
```

### Create the Project Database & User
```sql
-- Connect as superuser
psql -U postgres

-- Run these SQL commands:
CREATE USER myai_user WITH PASSWORD 'your_db_password_here';
CREATE DATABASE myai_db OWNER myai_user;
GRANT ALL PRIVILEGES ON DATABASE myai_db TO myai_user;
\q
```

> Replace `myai_user` and `your_db_password_here` with the values from your `.env` file.

---

## 4. Install pgvector Extension

pgvector adds vector column support to PostgreSQL so you can store and search AI embeddings.

### Windows
1. Download the pre-built release for your PostgreSQL version from:
   **github.com/pgvector/pgvector/releases**
2. Copy the `.dll` and `.sql` files into your PostgreSQL install directories as described in the release notes.

### macOS
```bash
brew install pgvector
```

### Ubuntu / Debian
```bash
sudo apt install -y postgresql-server-dev-15
git clone --branch v0.7.0 https://github.com/pgvector/pgvector.git
cd pgvector
make
sudo make install
cd .. && rm -rf pgvector
```

### Enable the Extension in Your Database
```sql
-- Connect to your project database
psql -U myai_user -d myai_db

-- Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- Verify
SELECT * FROM pg_extension WHERE extname = 'vector';
\q
```

You should see `vector` listed. Your database is now AI-ready.

---

## 5. Install VS Code

1. Download from **code.visualstudio.com** and run the installer.
2. During install on Windows, check **"Add to PATH"**.
3. Open VS Code and install these essential extensions (press `Ctrl+Shift+X`):

| Extension | Publisher | Purpose |
|---|---|---|
| GitHub Copilot | GitHub | AI code completion |
| GitHub Copilot Chat | GitHub | Copilot inline chat & edits |
| Python | Microsoft | Python language support |
| Pylance | Microsoft | Fast Python IntelliSense |
| PostgreSQL | Chris Kolkman | DB explorer inside VS Code |
| Even Better TOML | tamasfe | Config file support |
| GitLens | GitKraken | Git history & blame |
| EditorConfig | EditorConfig | Consistent code style |

---

## 6. Clone & Configure the Project

```bash
# Clone your repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

# Copy the environment template
cp .env.example .env

# Open in VS Code
code .
```

Now edit `.env` and fill in all values marked `your_..._here`:

```
POSTGRES_PASSWORD=your_db_password_here
DATABASE_URL=postgresql://myai_user:your_db_password_here@localhost:5432/myai_db
OPENAI_API_KEY=sk-your-openai-key-here
GITHUB_TOKEN=ghp_your-github-token-here
```

Install Python dependencies:
```bash
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 7. Connect Copilot to Your Project

This section explains how to connect both **GitHub Copilot** (code completions in VS Code) and **Microsoft Copilot** (conversational AI assistant) so they can directly read and edit files in your project.

---

### 7a. GitHub Copilot in VS Code

**Step 1 — Sign in to GitHub Copilot**
1. In VS Code, click the **Accounts icon** (bottom-left, person silhouette).
2. Select **"Sign in with GitHub to use GitHub Copilot"**.
3. Complete browser authentication with your GitHub account.
4. Verify: the Copilot icon appears in the VS Code status bar (bottom right).

**Step 2 — Open Your Project as a Workspace**
- Always open the **root project folder** in VS Code (`File → Open Folder`), not individual files.
- Copilot indexes all files in the open folder based on the patterns in `config.yaml → copilot.include_patterns`.

**Step 3 — Add a `.github/copilot-instructions.md` File**

This is the key file that tells Copilot about your project context:
```
mkdir -p .github
touch .github/copilot-instructions.md
```

Paste the following into `copilot-instructions.md` and customize it:
```markdown
# Copilot Project Instructions

## Project Overview
This is a Python/FastAPI application using PostgreSQL with pgvector for AI-powered semantic search.

## Stack
- Language: Python 3.11
- Framework: FastAPI
- Database: PostgreSQL 15 + pgvector 0.7
- AI: OpenAI GPT-4o + text-embedding-3-small
- ORM: SQLAlchemy 2.0 + Alembic migrations

## Coding Conventions
- Use type hints on all functions
- Follow PEP 8; max line length 88 (Black formatter)
- Write docstrings for all public classes and functions
- Use async/await for all I/O operations
- Store config in environment variables, never hardcode secrets

## Key Files
- `config.yaml` — static app configuration
- `.env` — secrets and environment variables (never commit)
- `requirements.txt` — Python dependencies
- `alembic/` — database migrations

## Important: Never edit .env directly. Use .env.example as the template.
```

**Step 4 — Use Copilot Chat to Edit Code**
- Press `Ctrl+I` anywhere in a file to open **Copilot Inline Chat** — type a request and Copilot edits that file directly.
- Press `Ctrl+Shift+I` to open the **Copilot Chat panel** — ask questions or request multi-file edits.
- Use `@workspace` in the chat to give Copilot context about the entire project:
  ```
  @workspace Create a SQLAlchemy model for storing vector embeddings using pgvector
  ```

**Step 5 — Allow Copilot to Edit Multiple Files**
- In Copilot Chat, use the **Edit mode** (pencil icon or `/edit` command).
- Copilot will show a diff of proposed changes — review and accept/reject each file.

---

### 7b. Microsoft Copilot Access to Project Files

To allow Microsoft Copilot to read and work with your project files in conversation:

**Option 1 — Paste file contents directly**
Copy and paste specific files into the Copilot chat when asking for help. Best for focused, single-file tasks.

**Option 2 — Use VS Code + GitHub Copilot Chat (recommended)**
The GitHub Copilot Chat panel inside VS Code has full access to all open workspace files. Use `@workspace` prefix for project-wide context.

**Option 3 — Connect via OneDrive/SharePoint**
1. Sync your project folder to OneDrive.
2. In Microsoft Copilot, connect your OneDrive.
3. Reference files by name: *"Open my config.yaml from OneDrive and review the pgvector settings."*

**Option 4 — GitHub Repository Access**
- Keep your project on GitHub (private repo is fine).
- Microsoft Copilot can be directed to reference specific files by sharing snippets or file paths in chat.

---

### 7c. Recommended VS Code Settings for Copilot

Create or update `.vscode/settings.json` in your project:
```json
{
  "editor.inlineSuggest.enabled": true,
  "github.copilot.enable": {
    "*": true,
    "plaintext": false,
    "markdown": true,
    "yaml": true,
    "python": true
  },
  "github.copilot.chat.localeOverride": "en",
  "python.defaultInterpreterPath": ".venv/bin/python",
  "editor.formatOnSave": true,
  "python.formatting.provider": "black",
  "files.exclude": {
    "**/__pycache__": true,
    "**/.venv": true,
    "**/logs": true
  }
}
```

---

## 8. Verify Everything Works

Run through this checklist after setup:

```bash
# 1. Python virtual environment
source .venv/bin/activate
python --version          # Should show 3.11.x or higher

# 2. Dependencies installed
pip list | grep -E "fastapi|sqlalchemy|pgvector|openai"

# 3. Database connection
psql -U myai_user -d myai_db -c "SELECT version();"

# 4. pgvector available
psql -U myai_user -d myai_db -c "SELECT extname FROM pg_extension WHERE extname='vector';"

# 5. App starts (if you have a main.py)
uvicorn main:app --reload
```

**In VS Code:**
- Copilot icon visible in status bar ✓
- `.github/copilot-instructions.md` present ✓
- Python interpreter set to `.venv` (bottom-right of VS Code) ✓
- Try pressing `Ctrl+I` on any Python file and typing a request ✓

---

## 9. Troubleshooting

| Problem | Fix |
|---|---|
| `pip` not found | Ensure virtual environment is activated |
| `psql: command not found` | Add PostgreSQL bin directory to PATH |
| pgvector install fails on Ubuntu | Install `postgresql-server-dev-XX` matching your PG version |
| Copilot not suggesting | Check sign-in status; try `Developer: Reload Window` in VS Code |
| `DATABASE_URL` connection refused | Ensure PostgreSQL service is running (`brew services list` or `systemctl status postgresql`) |
| Embeddings dimension mismatch | Ensure `VECTOR_DIMENSION` in `.env` matches `pgvector.dimension` in `config.yaml` and your model's output size |
| `.env` values not loading | Confirm `python-dotenv` is installed and `load_dotenv()` is called at app startup |

---

## 10. Overnight Processing

The current workspace uses `venv` as its project virtual environment. Preflight
the complete free, local-AI overnight profile from the repository root:

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --profile safe --preflight
```

Start the run:

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --profile safe --continue-on-error
```

Resume the latest interrupted or failed run:

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --resume --continue-on-error
```

This profile excludes CanLII and all paid hosted-AI operations. Chunk creation is
ordinary Python processing. BGE-M3 embeddings run locally through
`sentence-transformers`, use CPU by default, and may download the model on first
use. See `OVERNIGHT.md` for job order, logs, state, lock handling, and source
limitations.

---

*Last updated: August 2026 | Stack: Python 3.12 · FastAPI · PostgreSQL · pgvector · local BGE-M3 · VS Code*
