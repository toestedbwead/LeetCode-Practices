#  Richest Customer Wealth
# Topics: Array, Prefix Sum, Weekly Contest 193
# used nested loops and comparisons

def maximumWealth():
    accounts = [[2,8,7],[7,1,3],[1,9,5]]
    # output : 6

    max_wealth = 0

    for customer_accounts in accounts:
        customer_total_wealth = sum(customer_accounts)

        if customer_total_wealth > max_wealth:
            max_wealth = customer_total_wealth

    return max_wealth
    
print(maximumWealth())


''' LEET CODE own ver
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for customer_accounts in accounts:
            customer_total_wealth = sum(customer_accounts)

            if customer_total_wealth > max_wealth:
                max_wealth = customer_total_wealth
        return max_wealth
'''