# card-board-game
Card game in progress

# Instructions

Any number of players can play. We'll start with 2 players.

Energy - A resource that is analogous to time. Energy is used to move, attack, create, and act.
Card - An item in your hand. Cards can represent units, actions, or anything you want.

Unit - A piece on your board, usually able to attack, move, and becomes destroyed. Units have a cost to move, to attack, and to create.

Action - A card you can change the board with. These might be spells, commands, or the like.

Many cards don't fit into these categories. These cards can have unique effects and interactions with each other. It's best to read them before you use them.


Begin the game by calling a coin toss. The winning player determines who goes first.
On the first turn, "energy" starts at 2. Energy will increase logarithmically by every turn change, to avoid stale games.

You can spend energy to use cards. Cards may require a special resource to activate.
Energy can also be spent to attack with a unit. Reducing a unit's HP to 0 destroys it.
By destroying all of your opponent's infrastructure AND units, you win the game.

## On units

Most units have HP, MV, Move Cost, ATK, Attack Cost, and Attack Range.

HP - When HP is reduced to 0, the unit is destroyed.

MV - How far the unit can move in one movement.

Move Cost - The resource cost to initiate a unit's movement.

ATK - The damage the unit will do.

Attack Cost - The resource cost to attack.

Attack Range - The range the unit can attack with. Most units will have a specially shaped attack range. A unit with a 5 attack range in the front needs to line up with the target, face the target, then attack. Units with these limited attack shapes are usually cumbersome, but powerful.