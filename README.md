# CCIT4020_Space

Python programming assignments for **CCIT4020 Introduction to Computer Programming (ICP)** at HKU SPACE Community College, 2020–21. Both programs are small menu-driven scripts.

These are my assignment solutions, kept with the original briefs — please do not copy them for your own submissions.

## Files

### `ass1/` — Programming Assignment 1

[`icpA1.py`](ass1/icpA1.py) is a menu that loops until you exit:

1. Add two integers  
2. Concatenate two strings  
3. Show the last message that was printed  
4. Exit  

Unknown options print an error and return to the menu.

```bash
cd ass1
python3 icpA1.py
```

The folder also has the official brief (`icp_Assign1_2020.pdf`) and submission form.

### `ass2/` — Programming Assignment 2

[`icpA2.py`](ass2/icpA2.py) is a simple item-record system that reads and writes [`a2.txt`](ass2/a2.txt). Each line is `ID,name,weight` (for example `2345,Joystick ICPJ 2012X,1.23`).

1. Display all records and the total weight  
2. Append a new record  
3. Exit  

Run this from the `ass2` folder so the program can find `a2.txt`:

```bash
cd ass2
python3 icpA2.py
```

The official brief is `icp_ProgAssign2_2020.pdf`. `test1.py`, `test2.py`, and `test3.py` are short scratch scripts used while building the file I/O — the submitted program is `icpA2.py`.

## Requirements

Python 3 only (standard library). No extra packages.

## Licence

MIT — see [LICENSE](LICENSE).
