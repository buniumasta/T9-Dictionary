## T9-Dictionary

***A long, long time ago, before the touchscreen keyboards of modern phones, primitive beings called humans typed words on their flip phones using numeric keypads. "How does this work?" you wonder. "Numbers aren't letters!" Indeed, they are not; however, each numeric key was marked with a collection of letters it could represent.***

![Alt text](/img/nokia.png?raw=true "Nokia")


The Python program simulates T-9 dictionary behavior on old mobiles and helps users to write fast SMS on mobile phones :).

As presented in the picture above to numeric keys letters are assigned:

```
keymap = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}
```

## Sequence without T9:
when the user edited SMS without T-9 and inserted the sequence: '226' it resulted in 'bm'. Hitting more than one the same key gave the option to go via a sequence of letters assigned to the key. So twice hit key '2' gave "a->b", so letter b was inserted into SMS, one hit '6' gave 'm' so the final word 'bm'm.


* Recursive dictionary data structure is used for fast search
* Recursive search functions are implemented for data search

### File Sources
The data set originally comes from Google's [NGram](https://storage.googleapis.com/books/ngrams/books/datasetsv3.html) project, released under CC BY 3.0.
