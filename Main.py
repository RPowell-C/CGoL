import matplotlib.pyplot as plt # Plot the graphs
import numpy # Number stuff
import matplotlib.animation as anim # Animation

# Grid settings
N = 200
on = 255
off = 0
vals = [on, off]

# Populate the grid
grid = numpy.random.choice(vals, N*N, p=[.2, .8]).reshape(N,N)

def update(data):
    global grid
    # Copy Grid
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
                grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
                grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255
            # Apply Conway's rules
            if grid[i, j] == on:
                if (total < 2) or (total >3):
                    newGrid[i, j] = off
            else:
                if total == 3:
                    newGrid[i, j] = on
    # Update the data
    mat.set_data(newGrid)
    grid = newGrid
    return [mat]

# Set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = anim.FuncAnimation(fig, update, interval=50,
                              save_count=50)
plt.show()