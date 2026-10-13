class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #[25,10,23,4]
        #[4,10,23,25]
        max_bananas = 0
        for num in piles:
            max_bananas = max(max_bananas, num)
        min_bananas = 1
        #now for the search
        #find the smallest k where k/h or bannanas/hr will result in the all of the piles being eaten in time
        #k = number of bannanas
        #h = max time
        k = 0
        while max_bananas >= min_bananas:
            curr_per_hour = (max_bananas + min_bananas)//2
            #is that mid bannanas the most optimal(smallest k) that allows me to eat all of the piles in h hours?
            #now that we have the mid: i want to check if the mid is the smallest k or bananas per hour we can eat within h hours
            total_hours = 0
            for bananas in piles:
                total_hours += math.ceil(bananas / curr_per_hour)
            if total_hours <= h:
                max_bananas = curr_per_hour - 1
                k = curr_per_hour
            else:
                min_bananas = curr_per_hour + 1
            
        return k
