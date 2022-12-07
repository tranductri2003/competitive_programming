t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if s.count("0")%2==1 and s.count("0")>1:
        print("ALICE")
    else:
        print("BOB")
"""In each turn, the player can perform one of the following operations:

Choose any i (1≤i≤n), where s[i]= '0' and change s[i] to '1'. Pay 1 dollar.
Reverse the whole string, pay 0 dollars. This operation is only allowed if the string is currently not a palindrome, and the last operation was not reverse. 
That is, if Alice reverses the string,
then Bob can't reverse in the next move, and vice versa."""


"""In the first test case of the example,

in the 1-st move Alice has to perform the 1-st operation, since the string is currently a palindrome.
in the 2-nd move Bob reverses the string.
in the 3-rd move Alice again has to perform the 1-st operation. All characters of the string are '1', game over.
"""

    