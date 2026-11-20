"""MASAR Development Studio — first Python program."""


def greet(name: str) -> str:
    """Return a friendly greeting."""
    clean_name = name.strip() or "Developer"
    return f"Hello, {clean_name}! Welcome to MASAR Development Studio."


def main() -> None:
    print("=" * 52)
    print("          MASAR DEVELOPMENT STUDIO")
    print("=" * 52)
    print(greet("Salem"))
    print("Your cloud Python workspace is ready.")
    print("Next: edit this file, save it, and run it again.")


if __name__ == "__main__":
    main()
