# Checking for Properly Nested Brackets
Today's exercise is drawn from the [ACM's](https://en.wikipedia.org/wiki/Association_for_Computing_Machinery) Intercollegiate Programming Contest (the ICPC), an annual tournament in which teams of three students from colleges and universities across the world compete to see how quickly they can write programs to solve specific tasks.

During the actual contest, teams submit their code to an automated judge, which runs their code against several (secret) test cases to verify whether it produces the correct output. The real contest has both time pressure and penalties for incorrect / incomplete submissions, but you don't have to worry about that while practicing.

Your submission will be a single-file python program that runs correctly on all the test inputs for the following task. It should take in input on stdin.

## Nesting a bunch of Brackets
In this problem we consider expressions containing brackets that are properly nested. These expressions are obtained by juxtaposition of properly nested expressions in a pair of matching brackets, the left one an opening and the right one a closing bracket.
```
( a + $ ( b = ) ( a ) )    # this is properly nested

( a + $ ) b = ) ( a ( )    # this is not
```

In this problem we have several pairs of brackets, so we have to impose a second condition on the expression: the matching brackets should be of the same kind. Consequently `(())` is OK, but `([))` is not. The pairs of brackets are:
```
(  )
[  ]
{  }
<  >
(*  *)
```
The two characters `(*` should be interpreted as one symbol, not as an opening bracket `(` followed immediately by an asterisk, and similarly for `*)`. The combination `(*)` should be interpreted as `(*` followed by `)`.

Write a program that checks whether expressions are properly nested. If the expression is not properly nested your program should determine the position of the offending bracket, that is the length of the shortest prefix of the expression that can not be extended to a properly nested expression. Don’t forget `(*` counts as one, as does `*)`. The characters that are not brackets also count as one.

**Input**

The input is a text-file. Each line contains an expression to be checked followed by and end-of-line marker. No line contains more than 3000 characters. The input ends with a standard end-of-file marker.

**Output**

The output is a textfile. Each line contains the result of the check of the corresponding inputline, that is ‘YES’ (in upper case), if the expression is OK, and (if it is not OK) ‘NO’ followed by a space and the position of the error.

Sample Input
```
(*a++(*) 
(*a{+}*)
```
Sample Output
```
NO 6
YES
```
 

Sample Input 2
```
(*a++(*)
(*a{+}*)
    <************)>
    ()(***)(**)
   ()(***)(*)
({{}{}}[{(){}[]}
   ([))
 ()(**)
    ()*
 aaaaaaa
    aaa(aaaa
 *******
 ```
Sample Output 2
```
NO 6
YES
NO 17
YES
NO 10
NO 17
NO 6
YES
YES
YES
NO 13
YES
```