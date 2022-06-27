# pypw
![Alt text](/assets/screenshot.jpg?raw=true "pypw")

## (py)thon (p)ass(w)ord - a simple command line utility to generate unique passwords based on desired length and character selection

- git clone the repository
- cd into the root of the repository and run ```'python -m venv pypw' && 'source bin/activate'```
- ensure pip is up-to-date: ```'python -m pip install --upgrade pip'```
- pip install pyperclip dependency: ```'python -m pip install pyperclip'```
- ./pypw can be executed with up to 3 command line boolean arguments representing password length, option for capital letters and an option for special characters.

| Order of arguments | Representation | Description |
| --- | --- | --- |
| `password length` | non-negative integer | Represents desired length of generated password |
| 'capitalization' | `boolean values` | Option for the inclusion of capitalization within password |
| 'special characters' | `boolean values` | Option for the inclusion of special characters (!, @, #, etc.) within password |

