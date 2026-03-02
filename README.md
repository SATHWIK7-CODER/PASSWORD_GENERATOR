# 🔐 Password Generator

A simple yet powerful command-line password generator built with Python. It generates secure, random passwords with full control over length, quantity, and character types.

---

## 📋 Requirements

- Python 3.x
- No external libraries required (uses built-in modules only)

---

## 🚀 Usage

```bash
python password_generator.py [options]
```

### Basic Example
```bash
python password_generator.py
```
Generates **1 password** of **16 characters** using all character types.

---

## ⚙️ Options

| Flag | Description | Default |
|---|---|---|
| `-l`, `--length` | Set the password length | `16` |
| `-n`, `--count` | Number of passwords to generate | `1` |
| `--no-uppercase` | Exclude uppercase letters | `False` |
| `--no-digits` | Exclude digits (0–9) | `False` |
| `--no-symbols` | Exclude special symbols | `False` |

---

## 💡 Examples

**Generate a single 16-character password:**
```bash
python password_generator.py
```

**Generate a 24-character password:**
```bash
python password_generator.py -l 24
```

**Generate 5 passwords at once:**
```bash
python password_generator.py -n 5
```

**Generate a password without symbols:**
```bash
python password_generator.py --no-symbols
```

**Generate 3 passwords of length 20, no symbols or digits:**
```bash
python password_generator.py -l 20 -n 3 --no-symbols --no-digits
```

---

## 🔧 How It Works

1. Builds a **character pool** based on selected options (lowercase, uppercase, digits, symbols)
2. **Guarantees** at least one character from each enabled group
3. Fills the remaining length with random characters from the full pool
4. **Shuffles** everything so required characters aren't predictably placed
5. Joins and returns the final password string

---

## 📁 Project Structure

```
password_generator.py   # Main script
README.md               # Documentation
```

---

## 📜 License

This project is open-source and free to use.
