# Fill-4x3-numbre-grid
A game made in python using tkinter (ik, horrible). The objective is to fill all grids with a number from 1-8, but it cant be consecutive.

# How it works?

The code starts at a grid, then checks for all directions (vertical, horizontal and diaognal) if there is a consecutive number, e.g: if the actual grid is 7 and the up-left grid is 6, then it fails and is a game over.

# How do i solve it?

There is only one way to solve it, and is:

.  .╔═══╦═══╗  
.  .║ 3 ║ 5 ║  
╔═══╬═══╬═══╬═══╗  
║ 7 ║ 1 ║ 8 ║ 2 ║  
╚═══╬═══╬═══╬═══╝  
.  .║ 4 ║ 6 ║  
.  .╚═══╩═══╝  

Note: order can be reversed.
