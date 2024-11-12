# Commutative-_Algebra
That repository is deployed during a Research in Commutative Algebra Research granted by National Center of Science in Poland
![D5]([https://link_do_obrazka.com/obrazek.jpg](https://imgur.com/a/RNFUfej))

\
**grafy** contains programms used to manipulating weights of graph. After initializing **nadawanie_wag** which is a bijection between set of nodes and list of weights you can ommit nodes with positive/negative weights. It is so after applying odbicie function (means reflection) and using function **omijanie_dodatnich / omijanie_ujemnych**. You can also use **zmiana_na_dodatnie/ zmiana_na_ujemne** to run odbicie function (reflection) until there will be any negative/possitive weights.
\
\
**kombi_najnowsze** contains all functions above adapted to manipueting tuple containing lists of weights. Function **rownolegle_mod** manipulates tuple of weights until one of conditions is fulfilled: after applaing multiple iteration of odbicie weight is the same as before odbicies either weight contains all non-negative digits.  rownolegle_mod returns not only non-negative weights but also numbers of iterations necessary to achive each weight. It devide weights with even and odd iterations.  **rownolegle** returns weight which numbers of odd iterations is not equal to numbers of even iterations.
