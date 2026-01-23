<h2 class="c-project-heading--task">Play with colour</h2>
--- task ---
Add some colour and make your shapes transparent.
--- /task ---

<h2 class="c-project-heading--explainer">Fill first, then add the shape</h2>
Each time you make a new shape, change the colour first with `fill()`, then add the code for the shape.

<h2 class="c-project-heading--explainer">fill(red, green, blue, opacity)</h2>
The first three numbers change the colour. The fourth changes the opacity, so the shape becomes more or less transparent.

--- task ---
Adjust the numbers in `fill` to make different colours.
--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 12
line_highlights: 14, 16
---
def draw():
    # Put code to run every frame here
    fill(255, 0, 255, 200)    
    rect(50, 50, 120, 100) 
    fill(0, 0, 255)
    ellipse(160, 220, 200, 125) 

--- /code ---
--- task ---
**Test:** Run your code to see what your design looks like.
--- /task ---
</div>