# yearn

Say I hear or read about something... and for whatever reason it stays with me... won't go away... for to put the compulsion to rest... I code.

If you're finding yourself curious you may consider picking an item from the list below, glancing over the brief and maybe even clicking on the header to see the code itself.

<!-- vim-markdown-toc GFM -->
* [hash_me_poorly](#hash_me_poorly)
* [is_there_a_pair](#is_there_a_pair)
* [reverse_text_not_tags](#reverse_text_not_tags)

<!-- vim-markdown-toc -->

## [hash_me_poorly](code/hash_me_poorly.py)

Show me that hash, will ya?..

```
$ code/hash_me_poorly.py | grep -v len=0
No of items: 1024
Item 0 is 0
Item 1 is 1
Item 1022 is 1022
Item 1023 is 1023
```

## [is_there_a_pair](code/is_there_a_pair.py)

Given a list of numbers and a value... establish whether the list contains a pair of numbers whose sum equals given value.

Now... how many of those pairs is there, exactly?

```
$ code/is_there_a_pair.py
Array of 1024 elements (values 0..1023), sum to search for: 0
Found: 0 pairs
Array of 1024 elements (values 0..1023), sum to search for: 1
Found: 1 pairs
Array of 1024 elements (values 0..1023), sum to search for: 1022
Found: 511 pairs
Array of 1024 elements (values 0..1023), sum to search for: 1023
Found: 512 pairs
Array of 1024 elements (values 0..1023), sum to search for: 1024
Found: 511 pairs
Array of 1024 elements (values 0..1023), sum to search for: 2045
Found: 1 pairs
Array of 1024 elements (values 0..1023), sum to search for: 2046
Found: 0 pairs
```

## [reverse_text_not_tags](code/reverse_text_not_tags.py)

Lets reverse some text, shall we?

Now... what if portions of the text, lets call them tags, need to be left intact?

```
$ code/reverse_text_not_tags.py
Text: Reverse me!
Text reversed: !em esreveR
Text reversed not tags: !em esreveR
Text: <html><head></head><body><h1>Reverse me!</h1></body></html>
Text reversed: >lmth/<>ydob/<>1h/<!em esreveR>1h<>ydob<>daeh/<>daeh<>lmth<
Text reversed not tags: <html><head></head><body><h1>!em esreveR</h1></body></html>
```
