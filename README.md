# yearn

Say I hear or read about something... and for whatever reason it stays with me... won't go away... for to put the compulsion to rest... I code.

If you're finding yourself curious you may consider picking an item from the list below, glancing over the brief and maybe even clicking on the header to see the code itself.

<!-- vim-markdown-toc GFM -->

* [anagram_or_not](#anagram_or_not)
* [double_squares](#double_squares)
* [hash_me_poorly](#hash_me_poorly)
* [compare_versions](#compare_versions)
* [fizzbuzz](#fizzbuzz)
* [is_there_a_pair](#is_there_a_pair)
* [show_me_these_primes](#show_me_these_primes)
* [reverse_text_not_tags](#reverse_text_not_tags)
* [segmentise_that_sentence](#segmentise_that_sentence)
* [textify_that_list](#textify_that_list)
* [serve_and_track](#serve_and_track)
* [whos_there](#whos_there)

<!-- vim-markdown-toc -->

## [anagram_or_not](code/anagram_or_not.py)

Anagram or not?.. that's the question!

```
$ code/anagram_or_not.py
Is '' anagram of 'abc'? No!
Is 'abcde' anagram of ''? No!
Is 'abcde' anagram of 'vwxyz'? No!
Is 'abcde' anagram of 'abcde'? Yes!
Is 'abcde' anagram of 'edcba'? Yes!
Is 'edcba' anagram of 'abcde'? Yes!
```

## [double_squares](code/double_squares)

Given X, determine the number of ways in which it can be written as the sum of two squares.


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


## [compare_versions](code/compare_versions.py)

Compare two version numbers version1 and version2:

* If version1 > version2 return 1
* If version1 < version2 return -1
* Otherwise return 0.

Here is an example of version numbers ordering: *0.1 < 1.1 < 1.2 < 1.13 < 1.13.4*.

Allow to use custom comparison operators such as 'eq', 'lt', 'gt':
* If version1 *operator* version2 exit with 0
* Othewise exit with 1

```
$ ./compare_versions.py 1.0 1.1
-1

$ ./compare_versions.py 1.0 1.0
0

$ ./compare_versions.py 1.1 1.0
1

$ ./compare_versions.py --verbose 1.0 1.0
Comparing version numbers 1.0 and 1.0, comparison result: 0

$ ./compare_versions.py --verbose --operator eq 1.0 1.0
1.0 eq 1.0 True

$ ./compare_versions.py --operator ge 1.0 1.0 && echo "no update needed" || echo "update recommended"
no update needed

$ ./compare_versions.py --operator ge 1.0 1.1 && echo "no update needed" || echo "update recommended"
update recommended

$ ./compare_versions.py --operator eq 1.0 1.0 && echo "exact version installed" || echo "different version installed"
exact version installed

$ ./compare_versions.py --operator eq 1.0 1.0 && echo "exact version installed" || echo "different version installed"
exact version installed
```

## [fizzbuzz](code/fizzbuzz.py)

Oh boy. This. Really?.. Couldn't help, sorry!..

```
$ ./fizzbuzz.py 16
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizz buzz
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

## [show_me_these_primes](code/show_me_these_primes.py)

Some useful priming. (*useful* as in contrast to say the kind described by Daniel Kahneman in his talk [on Studies on Priming People to The Idea of Money](https://www.youtube.com/watch?v=Oj66YRuSe8Y))

```
$ code/show_me_these_primes.py
is n a prime?
-1: False
0: False
1: False
2: True
3: True
4: False
5: True
6: False
7: True
8: False
9: False
10: False
11: True
12: False
13: True
14: False
15: False
number of prime numbers smaller or equal n:
-1: 0
0: 0
1: 0
2: 1
3: 2
4: 2
5: 3
6: 3
7: 4
8: 4
9: 4
10: 4
11: 5
12: 5
13: 6
14: 6
15: 6
next prime:
1: 2
2: 3
3: 5
4: 5
5: 7
6: 7
7: 11
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

## [segmentise_that_sentence](code/segmentise_that_sentence.py)

Stomped upon this [little great essay](http://thenoisychannel.com/2011/08/08/retiring-a-great-interview-problem).

Thought for a moment and came up with a hackety quick and dirty piece of code. As a bonus comes translation table allowing to tune the translation process to one's taste.

```
$ sentence="Given an input string and a dictionary of words, segment the input string into a space-separated sequence of dictionary words if possible. For example, if the input string is 'applepie' and dictionary contains a standard set of English words, then we would return the string 'apple pie' as output."
$ code/segmentise_that_sentence.py "${sentence// /}" "${sentence}"
Given an input string and a dictionary of words, segment the input string into a space-separated sequence of dictionary words if possible. For example, if the input string is 'applepie' and dictionary contains a standard set of English words, then we would return the string 'apple pie' as output.
```

## [textify_that_list](code/textify_that_list.py)

How about we present list of positive integers as a string specifying continuous
ranges?

```
$ code/textify_that_list.py
1
1
1-2
1-2
1,4-5,8
1-2,4,8
1-2,4,8
1-3,5,8,13-17
```

## [serve_and_track](code/serve_and_track.sh)

A barebones of a webserver, for some weird reason written BASH.

Barely functional but capable enough to handle the following:

  * /image  - will serve image /tmp/service_image
  * /status - will respond with HTTP 200 if /tmp/service_status exists and with HTTP 503 otherwise
  * (other) - will respond with 501 not implemented

* server

```
$ ./serve_and_track.sh
127.0.0.1 - - [10/Aug/2017:22:38:16 +0000] "GET /ping HTTP/1.1" 200
```

* client

```
$ curl 127.0.0.1:8080/ping
OK
```

## [whos_there](code/whos_there.py)

Given service log file display user identifiers.

```
$ ./whos_there.py
User id(s): ['8', '123', '456', '789', 'abc', 'def']
```
