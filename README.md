# Wordle Game (Python Console Version)

This project is a Python implementation of a two-player **Wordle-style guessing game** played in the console. One player sets a secret word, and the other player has a limited number of attempts to guess it correctly. The program provides feedback after each guess to help narrow down the possibilities, making it an engaging and logic-based word challenge.  

##  How the Game Works  

1. **Dictionary Setup**  
   - The game loads a dictionary of valid English words from `project4_dictionary.txt`.  
   - Only words in this file are considered valid inputs for both the secret word and player guesses.  
   - Words are automatically converted to lowercase for consistency.  

2. **Player Roles**  
   - **Player 1** enters the secret word (must be a valid 5-letter word from the dictionary).  
   - **Player 2** chooses the number of attempts allowed, then tries to guess the word.  

3. **Guess Validation**  
   - Every guess must:  
     - Be the correct length (5 letters).  
     - Exist in the dictionary.  
   - Invalid guesses prompt the player to try again.  

4. **Feedback System**  
   After each guess, the program provides feedback:  
   - **Correct letters in the correct position** → Revealed in the guess output.  
   - **Correct letters in the wrong position** → Tracked separately for reference.  
   - **Letters not in the word** → Recorded and removed from the alphabet pool.  

5. **Tracking Progress**  
- Shows history of:  
  - Letters correctly placed in the secret word.  
  - Letters found but in the wrong spot.  
  - Letters not in the word.  
- Displays the **remaining alphabet** for easier deduction.  

6. **Win/Loss Conditions**  
- **Win** → Player 2 guesses the secret word within the allowed attempts.  
- **Loss** → Player 2 runs out of attempts without finding the word.  
