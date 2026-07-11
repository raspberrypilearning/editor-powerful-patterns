## Challenges

Upgrade your design with emojis and animations.

## Use `randint()`

**Use `randint()`** to change the `ellipse()` or other values in your code.

## Remove the shape outline

**Remove the shape outline** by adding `no_stroke()` before the shapes.

```python filename="main.py" line_numbers="true" line_number_start="8"
def draw():
    no_stroke()
    fill(255, 0, 255, 255)    
    rect(randint(-100, 400), randint(-100, 400), 120, 100)
```

## Experiment with a new pattern

**Experiment with a new pattern** by adding `frame_count`. This animates your pattern.

```python filename="main.py" line_numbers="true" line_number_start="8"
def draw():
    no_stroke()
    fill(255, 0, 255, +frame_count) 
    rect(5*frame_count, 50, 120, 100) 
```

## Add text

**Add text** with `print()`. This will show in the **Text output** tab.

```python filename="main.py" line_numbers="true" line_number_start="20"
print('🟪 󠁢Look at these shapes! 🔵')
```