bannedNames = ["CON", "PRN", "AUX", "NUL" "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"]

for i in bannedNames:
    with open(f"generated/{i}", "w+") as f:
        f.write(i)

bannedChars = "<>:\"\\|?*⁄ "

for i in bannedChars:
    with open(f"generated/{i}", "w+") as f:
        f.write(i)

for i in range(1,32):
    try:
        with open(f"generated/{chr(i)}", "w+") as f:
            f.write(f"{i}")
    except IsADirectoryError:
        pass
