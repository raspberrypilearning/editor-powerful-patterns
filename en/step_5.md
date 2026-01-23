<h2 class="c-project-heading--task">Move the shapes</h2>
--- task ---
Put your shapes into a loop, and use `translate` to make some repeated patterns.
--- /task ---

<h2 class="c-project-heading--explainer">Translate</h2>
`translate` changes the `x` and `y` starting position. The shapes on the screen will move with it but their appearance will not change.

--- task ---
Put your code into a loop, every time it runs the starting position will change by the numbers you use in `translate()`. 
--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 11
line_highlights: 
---
def draw():
    # Put code to run every frame here
    for i in range(12):  # Loop 15 times
        fill(255, 0, 255, 255)    
        rect(50, 50, 120, 100) 
        fill(0, 0, 255)
        ellipse(160, 220, 200, 100) 
        translate(10, 10)  # Change the position by 10
--- /code ---
</div>

--- task ---
**Test:** Run the code to see how your pattern looks.
--- /task ---

