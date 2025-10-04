class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []

        for i in range(len(transactions)):
            name, time, amnt, city = transactions[i].split(",")

            if int(amnt) > 1000:
                res.append(transactions[i])
                continue
    
            for j in range(len(transactions)):
                if i == j:
                    continue

                name2, time2, amnt2, city2 = transactions[j].split(",")
                
                diff = abs(int(time2) - int(time))
                if name == name2 and city != city2 and diff < 60:
                    res.append(transactions[i])
                    break
        
        return res