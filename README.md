# Reversi Game

![N|Solid](https://lh3.googleusercontent.com/proxy/ZknX1_RX_A3dHBSlvQnfVj5a0kh8JxxldqUfCJfBDJHW3WX0wd73FQ9logh7glI_PXXy8rK766i-pUW-81-LpNC3yfIa4nr6Q0VHj0_6HFC-PaG_CVQQ7A)

Reversi is a game for two players (Black and White), which is played on a squared board of 8 rows/columns with stones that are white on one side and black on the other. In the beginning of the game, stones of Player 1 (B) and Player 2 (W) are placed in a cross arrangement at the center of the board as shown in Table 1. Then the players take turns placing stones on empty fields on the board with their colour facing up according to the
following rules:
1. All opponent’s stones that are enclosed in a straight line (horizontal, vertical, or diagonal) between the newly placed stone and another stone of the same color are flipped (see Table 3).
2. A move is only valid if it turns at least one opponent’s stone.
3. If a player has no valid moves, their turn is skipped (see example in Table 4).
4. The game ends when both players have no legal moves.
When the game ends, each player scores points equal to the number of stones which have their colour face up, and the player with a higher score wins (draw if scores equal). In this task you will create a Python program that allows one or two players to play a game of Reversi.
