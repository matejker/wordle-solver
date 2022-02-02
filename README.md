# Wordle solver
A command line Python [Wordle](https://www.powerlanguage.co.uk/wordle/) solver based on most frequent letters.


## Usage
1. Install the package on Python +3.8
2. Run `wordle`
3. Follow the screen, e.g.
```bash
Try: 'arose' with rank 0.5769
Round 1: (a),r,o,[s],[e]
Try: 'trona' with rank 1.1154
Round 2: [t],r,o,[m],(a)
Try: 'droil' with rank 1.2692
Round 3: [d],r,o,[i],[l]
Try: 'groan' with rank 1.4615
Round 4: [g],r,o,a,[n]
Try: 'croak' with rank 1.6923
Round 5: c,r,o,a,k            
🎉 🎉 🎉  Solved in 5 steps!
```
### Syntax
 - if the letter isn't in the word, use `[l]`
 - if the letter is in the word but not that position, use `(o)`
 - if the letter is on correct place, use `r`

For example `(a),r,o,[s],[e]` means that `a` is there but not on the first position, `r` and `o` are correct
and `s` and `e` aren't the word at all.