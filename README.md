# pypw
![Alt text](/assets/screenshot.jpg?raw=true "pypw")

## (py)thon (p)ass(w)ord - a simple command line utility to generate unique passwords based on desired length and character selection

- `pip install -r requirements.txt`
- `[pypw] [password_length] [capitalizations?] [special_characters?]`

# pypw can be executed with up to 3 command line boolean arguments representing password length, an option for capital letters and an option for special characters.

| CLI Argument | Representation | Description |
| --- | --- | --- |
| `password length` | `non-negative integer` | Represents desired length of generated password |
| `capitalization` | `boolean values` | Option for the inclusion of capitalization within password |
| `special characters` | `boolean values` | Option for the inclusion of special characters (!, @, #, etc.) within password |

