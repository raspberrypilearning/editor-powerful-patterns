<h2 class="c-project-heading--task">Play with scale</h2>
--- task ---
Use `scale()` to change the size of shapes.
--- /task ---

--- task ---
Comment out the `translate` code, and experiment with `scale` in your design. 
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
        rect(50, 50, 120, 100) 
        fill(0, 0, 255)
        ellipse(160, 220, 200, 100) 
        # translate(10,10)
        scale(0.5, 0.5)  # Half size
--- /code ---
</div>

--- task ---
**Test:** Run the code to see how your pattern looks.
--- /task ---


<div class="c-project-output">
![Visual output screen with two shapes in a range of scale.](images/step6.png)
</div>


<div class="c-project-callout c-project-callout--tip">
### Make it big or small

Using numbers bigger than ‘1’ will make the shape bigger, using a number smaller than ‘1’ will make it smaller.
</div>

