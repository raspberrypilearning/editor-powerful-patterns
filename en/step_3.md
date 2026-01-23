<h2 class="c-project-heading--task">Create shapes</h2>
--- task ---
Create a design with different shapes. 
--- /task ---

<h2 class="c-project-heading--explainer">Experimenting with shapes</h2>
The two shapes `rect()` and `ellipse()` have four values which are the x, y position on the screen, and the width and height of the shape.

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
line_number_start: 7 
line_highlights: 14-15
---
def draw():
    def setup():
    # Put code to run once here
    size(400, 400)
    background(255, 255, 255)


def draw():
    # Put code to run every frame here
    rect(50, 50, 120, 100) 
    ellipse(160, 220, 200, 100) 
--- /code ---
--- task ---
**Test:** Run your code to see what your design looks like.
--- /task ---
</div>

<div>
![An example of a motif using various shapes to create the motif.](images/motif.png){:width="300px"}
</div>