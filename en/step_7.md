<h2 class="c-project-heading--task">Random shapes</h2>
--- task ---
Experiment with `randint` to make animated patterns
--- /task ---

<h2 class="c-project-heading--explainer">Make it big or small</h2>
Using numbers bigger than ‘1’ will make the shape bigger, using a number smaller than ‘1’ will make it smaller.

--- task ---
Use random numbers to draw shapes in different positions:
--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 11
line_highlights: 19
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
**Test:** Run the code to see how your pattern looks.
--- /task ---


