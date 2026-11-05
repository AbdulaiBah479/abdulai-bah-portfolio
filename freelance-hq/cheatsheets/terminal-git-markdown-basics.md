# Terminal, Git and Markdown basics (for non-programmers)

## Terminal: move around
| Command | Meaning |
|---|---|
| `pwd` | Where am I? |
| `ls` | List files here (`ls -la` shows hidden ones too) |
| `cd folder` | Go into a folder (`cd ..` goes up, `cd ~` goes home) |
| `mkdir name` | Make a folder |
| `cat file.md` | Show a file's text |
| `cp a b` / `mv a b` | Copy / move or rename |
| `rm file` | Delete a file (no recycle bin!). Ask before using `rm -r` |
| `clear` | Clean the screen |
| `Ctrl+C` | Stop a running command |
| Up arrow | Previous command |
Tab key autocompletes names. Paste in Ubuntu terminal: right-click or `Ctrl+Shift+V`.

## Git: save versions (like "Save as" with history)
| Command | Meaning |
|---|---|
| `git status` | What changed? |
| `git add -A` | Prepare all changes |
| `git commit -m "message"` | Save a version with a note |
| `git push` | Upload to GitHub (backup) |
| `git pull` | Download updates |
| `git log --oneline` | History |
| `git diff` | See exact changes |
Never commit passwords, `.env` files or client data. `clients/`, `.env`, your tracker data and `my-plan.md` are git-ignored here.

## Markdown (.md): simple formatting
```
# Big title          ## Section          ### Subsection
**bold**   *italic*   `code`
- bullet        1. numbered
[link text](https://example.com)   ![image alt](image.png)
> quote
| table | header |
|---|---|
| a | b |
```

## Pandoc: files into ebooks/PDF
```bash
pandoc chapter1.md chapter2.md -o book.epub --toc
bash scripts/build_ebook.sh ebooks/<slug>
```

## CSV: spreadsheets as text
Open `tracker/*.csv` in Excel/Google Sheets/VS Code. Keep the header row. Do not use commas inside cells unless the cell is in quotes.

## Python scripts here
```bash
python3 scripts/income_report.py
python3 scripts/price_calc.py rate --income 12000 --costs 1200 --tax 0.2 --hours 20 --weeks 46
```

## VS Code basics
`code .` opens the folder (from WSL). Use the Explorer on the left, search with `Ctrl+Shift+F`, preview Markdown with `Ctrl+Shift+V`.

## When something fails
Read the last 5 lines of the error, copy them, and ask Claude: "What does this mean and what exactly should I type?"
