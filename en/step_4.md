<h2 class="c-project-heading--task">Play with colour</h2>
--- task ---
Add some colour to your designs
--- /task ---

<h2 class="c-project-heading--explainer">Fill first and then shape</h2>
Each time you make a new shape, change the colour first with `fill()`, then add the code for the shape.

--- task ---
Adjust the numbers in `rect` and `ellipse` to make your design.

Copy and paste more rectangles and ellipses in the code to add shapes. 
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
    fill(255, 0, 255)    
    rect(50, 50, 120, 100) 
    fill(255, 0, 255) 
    ellipse(160, 220, 200, 100) 
--- /code ---
--- task ---
**Test:** Run your code to see what your design looks like.
--- /task ---
</div>