# Start Here — MASAR Development Studio

## Where do I write code?

Open **main.py** from the Explorer on the left. The large editor in the middle is where you write Python.

## Your first edit

Find this line:

```python
print(greet("Salem"))
```

Change the name inside the quotation marks, for example:

```python
print(greet("MASAR"))
```

Save with **Ctrl + S**.

## How do I run the code?

1. Choose **Terminal → New Terminal** from the top menu.
2. In the terminal panel at the bottom, type:

```bash
python main.py
```

3. Press Enter. The result appears in the terminal.

## How do I run the checks?

```bash
python -m unittest discover -s tests -v
```

All tests should pass.

## A few important areas

- Explorer (left): project files.
- Editor (middle): write and edit code.
- Terminal (bottom): run commands.
- Source Control (branch icon on the left): review and commit changes.

Do not delete or overwrite files in the older MASAR repositories while learning here. This studio is your safe practice workspace.
