import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(10, 8))
lines_on_graph = []
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c']
color_index = 0

def setup_grid():
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='black', linewidth=1.5)
    ax.axvline(x=0, color='black', linewidth=1.5)
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('y', fontsize=14)
    ax.set_xticks(range(-10, 11))
    ax.set_yticks(range(-10, 11))

def draw_slope_triangle(m, b, color):
    if m == 0:
        return
    # pick a nice point to show rise/run
    x1 = 1
    y1 = m * x1 + b
    x2 = x1 + 1  # run = 1
    y2 = y1       # horizontal line (run)
    x3 = x2
    y3 = m * x2 + b  # rise

    # only draw if triangle fits on screen
    if abs(y1) < 9 and abs(y3) < 9:
        # run (horizontal)
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))
        ax.text((x1 + x2) / 2, y1 - 0.5, f'run = 1', fontsize=10,
                ha='center', color=color, fontweight='bold')
        # rise (vertical)
        ax.annotate('', xy=(x3, y3), xytext=(x2, y2),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))
        rise_label = f'rise = {m:g}'
        ax.text(x2 + 0.5, (y2 + y3) / 2, rise_label, fontsize=10,
                ha='left', color=color, fontweight='bold')

def plot_line(m, b, show_triangle=True):
    global color_index
    color = colors[color_index % len(colors)]
    color_index += 1

    x = np.linspace(-10, 10, 400)
    y = m * x + b

    label = f'y = {m:g}x + {b:g}' if b >= 0 else f'y = {m:g}x - {abs(b):g}'
    if m == 0:
        label = f'y = {b:g}'
    elif m == 1:
        label = f'y = x + {b:g}' if b >= 0 else f'y = x - {abs(b):g}'
    elif m == -1:
        label = f'y = -x + {b:g}' if b >= 0 else f'y = -x - {abs(b):g}'
    if b == 0:
        label = f'y = {m:g}x'

    ax.plot(x, y, color=color, linewidth=2.5, label=label)

    # mark y-intercept
    ax.plot(0, b, 'o', color=color, markersize=10, zorder=5)
    ax.annotate(f'  y-int = {b:g}', xy=(0, b), fontsize=10,
                color=color, fontweight='bold')

    if show_triangle:
        draw_slope_triangle(m, b, color)

    lines_on_graph.append((m, b, color, label))
    ax.legend(fontsize=12, loc='upper left')
    ax.set_title(f'slope = {m:g}   y-intercept = {b:g}', fontsize=14)
    fig.canvas.draw()

def clear():
    global color_index, lines_on_graph
    color_index = 0
    lines_on_graph = []
    setup_grid()
    fig.canvas.draw()

def compare_slopes(*slopes, b=0):
    clear()
    for m in slopes:
        plot_line(m, b, show_triangle=False)
    ax.set_title(f'Comparing slopes: {", ".join(str(s) for s in slopes)}', fontsize=14)
    fig.canvas.draw()

def compare_intercepts(*intercepts, m=1):
    clear()
    for b in intercepts:
        plot_line(m, b, show_triangle=False)
    ax.set_title(f'Same slope ({m:g}), different y-intercepts', fontsize=14)
    fig.canvas.draw()

setup_grid()
plt.ion()
plt.show(block=False)

print()
print("=" * 50)
print("  GRAPHING LINES — Interactive Tool")
print("=" * 50)
print()
print("  Commands:")
print("    plot_line(slope, y_intercept)")
print("    clear()")
print("    compare_slopes(1, 2, 3, -1)")
print("    compare_intercepts(0, 2, -3)")
print()
print("  Examples:")
print("    plot_line(2, 3)        # y = 2x + 3")
print("    plot_line(-1, 5)       # y = -x + 5")
print("    plot_line(0.5, -2)     # y = 0.5x - 2")
print()
print("  The slope triangle shows rise/run visually.")
print("  The dot marks the y-intercept.")
print()
