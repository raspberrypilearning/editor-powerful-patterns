<h2 class="c-project-heading--task">Play with scale</h2>

Use the `scale()` code below to change the size of shapes.

Comment out the `translate()` code, and experiment with `scale()`. Using numbers bigger than 1 will make the shape bigger, and using numbers smaller than 1 will make it smaller.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 14-15
---
def draw():
    for i in range(5):  # Loop 5 times
        fill(255, 0, 255, 255)    
        rect(50, 50, 120, 100) 
        fill(0, 0, 255, 75)
        ellipse(160, 220, 200, 100) 
        # translate(10,10)
        scale(0.5, 0.5)  # Half-size
--- /code ---
</div>

## Now run your code

See how your pattern looks.

<div class="c-project-output">
![A pattern of pink rectangles and blue ellipses climbing diagonally to the left in the Visual output. The shapes are large at the start and the sizes decrease throughout the pattern.](images/step6.png)
</div>



### Tip

<div class="c-project-callout c-project-callout--tip">

`scale()` changes the drawing each time the loop runs, so the shapes get smaller and appear in different places.

</div>

Run your project and check that the repeated shapes get smaller across the pattern.
