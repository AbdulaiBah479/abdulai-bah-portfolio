# Clients

Each client gets an isolated folder copied from `_template/`:

```bash
cp -r clients/_template clients/green-vital
```

Everything in `clients/` except this README and the template is **ignored by
Git**, because client data is private. Back it up with `scripts/backup.sh`.
