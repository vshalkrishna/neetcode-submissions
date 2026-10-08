class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        small = float('inf')
        second_small = float('inf')
        
        for price in prices:
            if price < small:
                second_small = small
                small = price
            elif price < second_small:
                second_small = price
                
        total_cost = small + second_small
        
        return money - total_cost if total_cost <= money else money