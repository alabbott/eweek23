# Game Challenge 1: Maze

You are presented with a 1000 by 40 maze (maze.txt) where each cell in the maze contains a number between 1 and 9.

Find the path through the maze between the top-left cell and the bottom right cell (only one solution exists per maze).

Output the sum of all of the numbers along the solution path.

## Example Maze
*Disclaimer*: The example maze in the challenge is much smaller than the challenge maze


```
+   +---+---+---+---+---+---+---+---+---+
| 4   3   3 | 8   7   6   6 | 8   2   4 |
+---+---+   +---+   +---+---+   +---+   +
| 6   5   1 | 2   8 | 4   6   1 | 5 | 9 |
+   +---+---+   +   +   +---+---+   +   +
| 2   2   2 | 9 | 2 | 6   9 | 3   4 | 3 |
+---+---+   +   +---+---+   +   +   +   +
| 9 | 9   8 | 6   3   7 | 7 | 8 | 5 | 8 |
+   +   +---+   +---+   +   +   +---+   +
| 4 | 7 | 1 | 5 | 8 | 5 | 7   4 | 6   5 |
+   +   +   +   +   +   +---+   +   +   +
| 3   5 | 2   1 | 8 | 8   2   5 | 3 | 2 |
+   +---+---+   +   +---+---+   +   +   +
| 3   9   5 | 9   3 | 9   9 | 5 | 3 | 1 |
+---+---+   +---+   +   +   +---+   +---+
| 5   9 | 6 | 9   4 | 6 | 5   9 | 7   2 |
+   +   +   +---+---+   +---+   +---+   +
| 5 | 5   2 | 8   8   2 | 7 | 3 | 7   2 |
+   +---+---+   +---+---+   +   +   +   +
| 9   1   6   4 | 2   5   3   1   2 | 1
+---+---+---+---+---+---+---+---+---+---+
```

## Solution

```
+   +---+---+---+---+---+---+---+---+---+
| 4   3   3 |               |           |
+---+---+   +---+   +---+---+   +---+   +
| 6   5   1 |       |           |   |   |
+   +---+---+   +   +   +---+---+   +   +
| 2   2   2 |   |   |       |       |   |
+---+---+   +   +---+---+   +   +   +   +
|   | 9   8 |           |   |   |   |   |
+   +   +---+   +---+   +   +   +---+   +
|   | 7 |   |   |   |   |       |       |
+   +   +   +   +   +   +---+   +   +   +
| 3   5 |       |   |           |   |   |
+   +---+---+   +   +---+---+   +   +   +
| 3   9   5 |       | 9   9 |   |   |   |
+---+---+   +---+   +   +   +---+   +---+
| 5   9 | 6 |       | 6 | 5   9 |       |
+   +   +   +---+---+   +---+   +---+   +
| 5 | 5   2 | 8   8   2 |   | 3 | 7   2 |
+   +---+---+   +---+---+   +   +   +   +
| 9   1   6   4 |             1   2 | 1
+---+---+---+---+---+---+---+---+---+---+
```

## Output

```
201

```


## Flag

Compute the md5 checksum of the output file. Make sure the output file contains only the numeric answer and a newline.

For the example output above, the flag is:

```
9417bd061f365a7b4bd13783c878de86
```
