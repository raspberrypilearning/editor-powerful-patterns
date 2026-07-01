<h2 class="c-project-heading--task">Challenges</h2>

Upgrade your design with emojis and animations.

## Use `randint()

**Use `randint()`** to change the `ellipse()` or other values in your code.

## Remove the shape outline

**Remove the shape outline** by adding `no_stroke()` before the shapes.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 
---
def draw():
    no_stroke()
    fill(255, 0, 255, 255)    
    rect(randint(-100, 400), randint(-100, 400), 120, 100)
--- /code ---
</div>

## Experiment with a new pattern

**Experiment with a new pattern** by adding `frame_count`. This animates your pattern.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 
---
def draw():
    no_stroke()
    fill(255, 0, 255, +frame_count) 
    rect(5*frame_count, 50, 120, 100) 
--- /code ---
</div>

## Add text

**Add text** with `print()`. This will show in the **Text ouput** tab.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 
---
print('🟪 󠁢Look at these shapes! 🔵')
--- /code ---
</div>