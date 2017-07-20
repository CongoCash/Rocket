#Rock Paper Scissors Lizard Spock
---------
###If you're not a fan of "The Big Bang Theory", then
  1. What the heck are you doing in this class?
  1. Check this out to get with the program! 

  <a href="https://www.youtube.com/watch?v=cSLeBKT7-sM" target="_blank"><img src="rpsls.jpg"></a>

####If you didn't quite get that, it's the same as "Rock, Paper, Scissors" but with a couple of additions. Here are the rules:
 - Scissors cuts Paper
 - Paper covers Rock
 - Rock crushes Lizard
 - Lizard poisons Spock
 - Spock smashes Scissors
 - Scissors decapitates Lizard
 - Lizard eats Paper
 - Paper disproves Spock
 - Spock vaporizes Rock
 - and as it always has, Rock crushes scissors
 - ####Simple, right?

##The Challenge

 - For a given number of __hands__ represented by _n_, return a list of all possible combinations of 'Rock, Paper, Scissors, Lizard, Spock'

So for example, if the value of _n_= 1, the correct returned value would be something like:

````
['rock'],
['paper'],
['scissors'],
['lizard'],
['spock']

````
For _n_= 2, you would get:

````
['rock','rock'],
['rock','paper'],
['rock','scissors'],
['rock','lizard'],
['rock','spock'],
['paper','rock']...

````

Okay, you get the idea, right? 


##The Goals

In this exercise, you will be implementing algorithms in both __Python__ and __JavaScript__ to solve the challenge. 

1. Write the steps of your algorithm in *pseudocode*.
  - Don't try to be fancy at this stage. Write the easiest solution that you can think of.
  - Use consistent formatting to make your code easy to read.
1. Convert your pseudocode into actual working code, starting with the language that you are most familiar with.
  - Verify that the code is running correctly.
  - Use different values for _n_ to verify. 
    - Hint - Because there are 5 possible plays for each hand, the correct total for any value of _n_ will always be 5<sup>n</sup>. So even for larger values of _n_, you can at least verify that you have the correct number of solutions.
1. When it's working correctly, convert it into the other language.
  - Make sure to re-verify the new version!

###Extra Credit
1. Analyze your code for possible optimizations.
  - Can you make your code more succinct?
  - How easy is it for other programmers to read and understand your code?
  - What is the time complexity of the algorithms you've written?

