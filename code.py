import numpy as np
import matplotlib.pyplot as plt
import random

# Define the bin dimensions
BIN_WIDTH = 80
BIN_HEIGHT = 40

# Define the number of rectangles
NUM_RECTANGLES = 9

# Generate random rectangles
rectangles = []
for i in range(NUM_RECTANGLES):
    width = random.randint(5, 15)
    height = random.randint(5, 15)
    rectangles.append((width, height))

# Define the positions of the rectangles
positions = [(0, 0)] * NUM_RECTANGLES

# Function to check if a rectangle can be placed
def can_place(pos, rect, positions):
    x, y = pos
    w, h = rect
    # Check boundaries
    if x < 0 or y < 0 or x + w > BIN_WIDTH or y + h > BIN_HEIGHT:
        return False
    # Check for overlaps
    for (px, py), (pw, ph) in zip(positions, rectangles):
        if not (x + w + 1 < px or x > px + pw + 1 or y + h + 1 < py or y > py + ph + 1):
            return False
    return True

# Function to place rectangles
def place_rectangles():
    for i in range(NUM_RECTANGLES):
        placed = False
        for x in range(BIN_WIDTH):
            for y in range(BIN_HEIGHT):
                if can_place((x, y), rectangles[i], positions):
                    positions[i] = (x, y)
                    placed = True
                    break
            if placed:
                break

# Place rectangles
place_rectangles()

# Visualization
def plot_bin():
    plt.figure(figsize=(10, 5))
    plt.xlim(0, BIN_WIDTH)
    plt.ylim(0, BIN_HEIGHT)
    plt.gca().set_aspect('equal', adjustable='box')
    
    for i, (pos, rect) in enumerate(zip(positions, rectangles)):
        x, y = pos
        w, h = rect
        plt.gca().add_patch(plt.Rectangle((x, y), w, h, fill=True, edgecolor='black', alpha=0.5))
        plt.text(x + w / 2, y + h / 2, str(i + 1), ha='center', va='center')

    plt.title('Rectangle Placement in Bin')
    plt.grid()
    plt.show()

# Plot the result
plot_bin()