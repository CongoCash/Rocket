#JavaScript Games
What cooler way could there be to learn about building interactive content than to create some classic games using JavaScript? In this repo you will flex those DOM manipulation muscles and code up some classics.

###[Tic-Tac-Toe](http://en.wikipedia.org/wiki/Tic-tac-toe)
Everyone knows how to play this game for a reason. It's simple enough to learn when you're 4 years old, and you were probably tired of playing it before you turned 5. The rules are easy:

  * The 3 x 3 board starts off blank
  * The players markers are designated by __X__ and __O__
  * Either player can start by marking any square
  * Play continues in turn until:
    * One of the players wins by connecting a line of three of their markers
    * The game is a draw if all squares are filled without a winner

##Your Mission
There are starter files for you in the `tictactoe` folder. Using HTML, CSS and native JavaScript methods, create a Tic-Tac-Toe game with the following features:
  * Show a 3 x 3 grid for the board.
    * You can hardcode this in HTML several different ways, or you could create the markup programatically in JavaScript and write it into the DOM.
    * Use any styling that you choose to dress it up.
    * Consider how you can keep track of which squares are empty and which have been played. You may want to think about adding a unique attribute to each square as an identifier.
  * Allow a click event on an empty square to insert a players marker.
    * Start with whichever marker you like.
    * Automatically alternate markers.
    * Do not allow a marker to be changed once a square is played.
    * Consider how you can keep track of which squares have been played by each player.
      * You may be able to re-purpose the unique square identifiers that were discussed in the previous section.
  * Automatically detect a winner or a tie.
    * Announce the winner or tie.
    * Do not allow any further board selections after a win or tie.
  * Add a __Reset__ button that 
    * clears the board
    * Resets any variables for a new game
    * You should not have to reload the web page to begin a new game

###Extra-Credit
Add the following features, or dream up some of your own
  * Add styling that renders the player markers in different colors.
  * Add a "Wins" counter that keeps track of __X__ wins, __O__ wins and Draws.
  * Style your board using CSS, image files or other stuff to make your UI the best.

Too easy for you? Check this version out and create code for it if you can:
####[3d Tic-Tac-Toe](http://en.wikipedia.org/wiki/3-D_Tic-Tac-Toe)

Here's another variation on the theme, with a significantly larger playing board. This one will require a more sophisticated strategy to detect a win:
####[Connect6](http://en.wikipedia.org/wiki/Connect6)

##Double Kick-Butt Extra Credit
You say that it just took you about 30 minutes for Tic-Tac-Toe? No problem. Here's you're chance to take your 'games' game up a notch. 

###[Checkers (also known as Draughts)](http://en.wikipedia.org/wiki/Draughts)
Check out this wiki for more rules and variations on this simple game than you ever expected. 
  * For your implementation, use the 8 x 8 American style board.
  * Remember that the board is typically laid out with a dark square at the bottom left.
  * Each player starts with 12 checkers.
  * Light color checkers plays first.
  * Play proceeds in turn.
    * Only the dark squares are used.
    * Players can move forward on the diagonal, one square at a time.
    * If an opposing player's checker is immediately adjacent, and there is a vacant spot directly across, the opponent is jumped and their piece is removed from the board.
  * Play continues until 
    * One player loses all pieces.
    * One player cannot move.
  * How will you move each piece? You could:
    * Click a piece to indicate that you intend to move it, then click the destination square.
    * Or, you could drag the piece. Check out the [Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Drag_and_drop)
  * There are some checkers-related images for you to use in the `images` folder. Feel free to use something else if you prefer.
  * Starter files for this project are in the `checkers` repo. We've provided a skeleton `html` file and not much else. Use your imagination for this one and have fun with it!

