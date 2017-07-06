Harry Potter Kata

so a given set of books could be a string of 5 numbers (inc 0)
10 4 5 1 0

let A = [k1, k2, k3, k4, k5] be the number of books bought
let p = 8 be the price
let n = 5 be number of books
let d: (2,3,4,5) => (5,10,20,25) be the discount for buying k books.
let k \in [0...5] be the number of distinct books purchased
let C be total cost

||: strip zeros
partial_cost = len(A) x price x discount(len(A))
take one from each collection
C += partial_cost
:||


so [2,2,2,1,1]
no zeros to strip


TIME: 30 minutes done
