<h2 class="c-project-heading--task">Style the background</h2>
--- task ---

Get started by adding the code below to make a background.

--- /task ---

--- task ---

Change the `background` colour by experimenting with different values in the starter code.

--- /task ---

<div class="c-project-callout c-project-callout--tip">
### Red, green, blue
The maximum amount of red, green, or blue is `255`. Make sure all your `background` colour values are between `0` and `255`.
</div> 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 5-6
---
from p5 import *
from random import randint

def setup():
    size(400, 400)
    background(0, 255, 255) # change background colour
--- /code ---

--- task ---

**Test:** Run your project and see the background change the colours in the **Visual output** tab.

--- /task ---
</div>

<div class="c-project-output">
![Visual output screen with coloured background](images/step2.png)
</div>

