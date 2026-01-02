# Keyboard Logger (Educational Analysis)

> ⚠️ **Warning**: This script records keystrokes. Running it on a system without explicit permission may be illegal or unethical. This document is for **educational and defensive analysis** only.

---

## Overview

This Python script uses `pynput` to listen for keyboard events and logs pressed keys to a file. It runs continuously and writes captured keystrokes in batches.

The behavior demonstrated here is commonly associated with **keylogging software** and is often flagged by security tools.

---

## What the Script Does

* Listens for all keyboard key presses
* Collects keystrokes in memory
* Writes them to a text file after every 10 keys
* Runs indefinitely until terminated

---

## Platform Behavior

### Windows (`os.name == "nt"`)

* Log file path:

  ```
  C:/Users/<username>/Desktop/log.txt
  ```
* The log file is marked as **hidden** using the Windows `attrib +h` command

### Linux / macOS (`os.name == "posix"`)

* Log file path:

  ```
  ~/log.txt
  ```
* No file-hiding is performed

---

## Key Components

### Keyboard Listener

Uses `pynput.keyboard.Listener` to capture key press events globally.

### Keystroke Buffer

* Stores pressed keys in a list
* Flushes to disk every 10 keystrokes

### Logging Format

Each key is written as:

```
Key.<name>
```

or

```
'a'
```

(depending on the key pressed)

---

## Security Implications

From a defensive or malware-analysis perspective, this script exhibits:

* Keystroke capture (credential harvesting risk)
* Stealth behavior (hidden log file on Windows)
* Persistent background execution

Because of this, antivirus software commonly classifies similar behavior as:

* **Spyware**
* **Keylogger**
* **Credential Access Tool**

---

## Limitations

* No encryption of logged data
* No network exfiltration
* No persistence mechanism
* Logs grow indefinitely

---

## Intended Use

This code is suitable **only** for:

* Learning how keylogging works
* Malware analysis labs
* Defensive security research
* Understanding how endpoint protection detects threats

It should **not** be used on real systems or other people’s machines.

---

## Disclaimer

The author is not responsible for any misuses.
