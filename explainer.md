### Levenshtein Row W7E4
Turning the table into two rows
Start from the lecture's code you copied, and change one piece at a time:

Table version	Two-row version	Why
X = [[0] * ...] (whole grid)	delete it	that's the memory being saved
X[0][j] = j loop (top row)	prev = list(range(len(b) + 1))	the top row is just 0, 1, 2, …, len(b)
X[i][0] = i loop (left column)	curr = [i] at the start of each row	each row starts with its own i
X[i - 1][j] (above)	prev[j]	"row above" = prev
X[i - 1][j - 1] (above-left)	prev[j - 1]	also in the row above
X[i][j - 1] (left)	curr[j - 1]	the cell just written in this row
X[i][j] = min(...)	curr.append(min(...))	build the row left to right
(nothing)	prev = curr after each row	the finished row becomes "the row above"
return X	return prev[-1]	the last cell of the last row is the answer