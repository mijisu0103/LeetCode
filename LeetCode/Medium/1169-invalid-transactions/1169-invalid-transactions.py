from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        person_transactions = defaultdict(list)
        invalid_transactions = []

        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time, amount = int(time), int(amount)
            person_transactions[name].append((time, amount, city, transaction))

        for name, trans_list in person_transactions.items():
            trans_list.sort()

            for i in range(len(trans_list)):
                time_i, amount_i, city_i, trans_i = trans_list[i]
                
                # Check if the transaction amount exceeds $1000
                if amount_i > 1000:
                    invalid_transactions.append(trans_i)

                # Check for transactions within 60 minutes in different cities
                for j in range(i + 1, len(trans_list)):
                    time_j, _, city_j, trans_j = trans_list[j]
                    
                    if time_j - time_i > 60:
                        break

                    if city_i != city_j:
                        invalid_transactions.append(trans_i)
                        invalid_transactions.append(trans_j)

        return invalid_transactions