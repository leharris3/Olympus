# Vanilla Chess Python Library
---
*Chess board with encapsulated rule sets for vanilla-chess and support for move/un-move behavior. Intended to provide reasonable framework for mid-tier vanilla chess  engines.*

- **Board Representation**
	- Piece-centric bitboard representation. Board object encapsulates a set of squares, pieces placed on squares.
- **Board Class Methods**
	- *Move Generation*
		- Move generation class function returns *set* of legal-move objects. Searching function probes potential move-to squares beginning at piece square checking against piece set for blocking pieces or invalid (out-of-bounds squares). Separate move objects generated for each potential move.
	- *Move*
		- Accepts move object and updates board position. Checks move against set of legal generated moves. Adds move to move queue.
	- *Pop*
		- Pops move off move queue and returns board to previous position.
	- *Print*
		- Outputs board view to terminal for debugging.
- **Board Subclasses**
	- *Pieces*
		- Encapsulates a 64-bit integer denoting current square occupation. 4-bit piece type value. Piece specific subclasses used.
	- *Move*
		- Move object encapsulates two 64-bit move-to and move-from squares. Contains reference to piece object moved and an optional reference to a captured piece object.