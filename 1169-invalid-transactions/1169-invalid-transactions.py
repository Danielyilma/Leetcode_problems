class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transaction_map = []
        res = []

        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")
            transaction_map.append([name, int(time), int(amount), city, i])
        print(transaction_map)
        for i in range(len(transaction_map)):
            if transaction_map[i][2] > 1000:
                res.append(transactions[transaction_map[i][4]])
                continue
    
            for j in range(len(transaction_map)):
                if i == j:
                    continue
                
                if transaction_map[i][0] == transaction_map[j][0] and transaction_map[i][3] != transaction_map[j][3] and abs(transaction_map[i][1] - transaction_map[j][1]) <= 60:
                    res.append(transactions[transaction_map[i][4]])
                    break

            
        
        return res
