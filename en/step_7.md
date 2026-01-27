<h2 class="c-project-heading--task">Random shapes</h2>
--- task ---

Experiment with `randint` to make animated patterns

--- /task ---

--- task ---

`randint()` generates a random number. 

Add it to `rect()` to draw rectangles between -100 and 400.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 11
---
def draw():
    # Put code to run every frame here
    for i in range(12):
        fill(255, 0, 255, 255)    
        rect(randint(-100, 400), randint(-100, 400), 120, 100) 
        fill(0, 0, 255)
        ellipse(160, 220, 200, 100) 
        # translate(10,10)
        scale(0.5, 0.5)  # Half size
--- /code ---
</div>

--- task ---
**Test:** Run the code to test it.

Experiment with `randint()` to change other values in your code.

--- /task ---


<div class="c-project-output">
![Visual output screen with two shapes randomly being drawn to the screen.](images/step7.gif)
</div>
