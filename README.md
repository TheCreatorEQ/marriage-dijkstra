# marriage-dijkstra
The young explorer came to a tribe. There he fell in love with the chief’s daughter, so he went to the chief to ask for marriage. The chief asked him to use 10,000 gold coins as a dowry before agreeing to marry his daughter to him. The explorer couldn’t come up with so many gold coins, so he asked the chief to lower his requirements. The chief said, “Well, if you can get me the high priest’s coat, I can get 8,000 gold coins. If you can get his crystal ball, then it will only cost 5,000 gold coins.”

The explorer ran to the high priest. There, ask him for a leather jacket or a crystal ball, and the high priest asks him for gold coins, or get him something else to lower the price. The explorers then went elsewhere, and others made similar requests, either directly exchanging with gold coins, or finding other things to reduce the price. But explorers don’t need to trade multiple things for the same thing, because they won’t get a lower price. The explorer needs your help now, let him marry his sweetheart with the least amount of gold coins. In addition, what he wants to tell you is that in this tribe, the concept of hierarchy is very strict. There will be no direct contact of any kind, including transactions, between two persons whose status gap exceeds a certain limit. He’s an outsider, so he’s exempt from these restrictions. But if he trades with someone of lower status, the higher-status person won’t trade with him again, they see it as indirect contact, and vice versa. Therefore, you need to provide him with the best solution after considering all the circumstances.

For convenience, we number all items starting from 1, the chief’s promise is also regarded as an item, and the number is always 1. Each item has a corresponding price P, the owner’s status level L, and a series of substitutes Ti and the “offer” Vi corresponding to the substitute. If the difference between the two’s status level exceeds M, they cannot “indirect transaction”. You have to use this data to figure out the minimum amount of gold an explorer needs to marry the chief’s daughter.

Input

The first line of input is two integers M, N (1 <= N <= 100), which in turn represent the status level gap limit and the total number of items. Next, the descriptions of the N items are given in order from small to large. The description of each item begins with three non-negative integers P, L, X (X < N), which in turn represent the price of the item, the status level of the owner, and the total number of substitutes. Each of the next X lines includes two integers T and V, representing the replacement number and “preferential price”, respectively.

Output

Output the minimum required gold coins.

Sample Input
1 4
10000 3 2
2 8000
3 5000
1000 2 1
4 200
3000 2 1
4 200
50 2 0

Sample Output
5250
