<h2 class="c-project-heading--task">Challenges</h2>
--- task ---
Upgrade your design with emojis and animations.
--- /task ---

--- task ---
Use text and emojis to `print()` a description of your pattern in the **Text output** tab.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 1
---
print('🟪 󠁢Look at these shapes! 🔵')
--- /code ---
</div>
--- /task ---

--- task ---
Experiment with adding `frame_count` to animate your pattern.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 1-4
---
def draw():
    # Put code to run every frame here
    fill(255, 0, 255, +frame_count) 
    rect(5*frame_count, 50, 120, 100) 
--- /code ---
</div>
--- /task ---

