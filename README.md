## Bomberman

### Starting the Game:
 *python3 main.py*

### Controls:

	q --> quit the game
	b --> generate a bomb
	a --> move left
	s --> move down
	d --> move right
	w --> move up

### Description:
- Initially the bomberman is at top left corner and he has 3 lives
- There are 4 enemies
- 10-15 bricks will be generated randomly
- Bomberman can drop a bomb at the current position by pressing 'b'
- The bomb explodes after 3 frames, i.e., after pressing 3 keys
- If the bomberman gets caught in an explosion, he dies(loses a life)
- If an enemy gets caught in an explosion, the enemy dies and the bomberman gets 100 points
- The bricks can be destroyed in explosion and the bomberman gets 20 points for each brick
- The game ends when we press 'q' or whwn all the enemies are destroyed or when the bomberman loses all the 3 lives

### Classes used:
	Board
	Walls
	Enemy
	Person
	Bomberman
	Bricks
	Bomb

### External packages:
	termcolor
	sys
	os
	random
	click
	time
