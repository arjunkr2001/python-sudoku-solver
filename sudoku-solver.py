grid = [
[5,2,0,0,0,6,3,0,8],
[0,7,0,3,8,0,2,0,5],
[8,4,3,0,0,5,1,6,7],
[4,0,0,0,0,0,7,8,3],
[9,8,5,0,0,3,4,1,2],
[7,3,2,1,4,8,6,5,9],
[3,9,0,0,0,0,8,0,0],
[0,5,7,8,0,0,9,2,4],
[2,0,8,0,0,0,5,0,0]
]
def show():
	print('\n')
	for i in range(9):
		for j in range(9):
			print(f' {grid[i][j]} ', end="")
		print('\n')

def check(x,y,n):
	global grid
	for i in range(9):
		if n == grid[x][i]:
			return False
			
	for i in range(9):
		if n == grid[i][y]:
			return False
		
	x0 = (x//3)*3
	y0 = (y//3)*3
	for i in range(3):
		for j in range(3):
			if grid[x0+i][y0+j] == n:
				return False
	return True
				
def solve():
	global grid
	for x in range(9):
		for y in range(9):
			if grid[x][y] == 0:
				for n in range(1,10):
					if check(x,y,n):
						grid[x][y] = n
						solve()
					grid[x][y] = 0
				return
	show()
solve()
		
					