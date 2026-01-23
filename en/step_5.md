<h2 class="c-project-heading--task">Turn the shapes</h2>
--- task ---
Put your shapes into a loop, and use `translate` to make some repeated patterns.
--- /task ---

<h2 class="c-project-heading--explainer">Translate</h2>
`translate` changes the starting position. In a loop these turns the shape a different amount each time.

--- task ---
Put your code into a loop, every time it runs the starting position will change by the numbers you use in `translate()`. 
--- /task ---

Make use you indent the code in the loop.

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
    for i in range(12):  # Loop 12 times
        fill(255, 0, 255, 255)    
        rect(50, 50, 120, 100) 
        fill(0, 0, 255)
        ellipse(160, 220, 200, 100) 
        translate(10, 10)  # Change the position by 10
--- /code ---
--- task ---
**Test:** Run the code and make a pattern.
--- /task ---
</div>

<div class="c-project-output">
![Examples of finished projects that have the motif used repeatedly to form a full pattern.](images/step5.png)
</div>
