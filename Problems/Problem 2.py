ans = 0
newx = 1
oldx = 0
while newx <= 4000000:
	newx = oldx + newx
	oldx = newx - oldx
	if newx%2 == 0:
		ans = ans + newx

print(ans)