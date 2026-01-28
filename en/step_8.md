<h2 class="c-project-heading--task">Challenges</h2>
--- task ---

Upgrade your design with emojis and animations.

--- /task ---

--- task ---

**Use `randint()`** to change the `ellipse()` or other values in your code.

--- /task ---


--- task ---

**Remove the shape outline** by adding `no_stroke()` before the shapes.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9
line_highlights: 
---
def draw():
    no_stroke()
    rect(randint(-100, 400), randint(-100, 400), 120, 100)
    rect(5*frame_count, 50, 120, 100) 
--- /code ---
</div>

--- /task ---


--- task ---

**Experiment with a new pattern** by adding `frame_count`. This animates your pattern.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9
line_highlights: 
---
def draw():
    no_stroke()
    fill(255, 0, 255, +frame_count) 
    rect(5*frame_count, 50, 120, 100) 
--- /code ---
</div>

--- /task ---


--- task ---

**Add text** with `print()`, this will show in the **Text ouput** tab.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 
---
print('🟪 󠁢Look at these shapes! 🔵')
--- /code ---
</div>

--- /task ---