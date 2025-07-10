class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        # Iterate through all possible lengths of the repeating substring
        # The substring length 'l' must be a divisor of 'n'
        # and 'l' must be less than 'n' (i.e., 'l' can go up to n // 2)
        for l in range(1, n // 2 + 1):
            if n % l == 0:  # Check if 'l' is a divisor of 'n'
                substring = s[:l]  # Extract the potential repeating substring
                
                # Construct the full string by repeating the substring
                # num_repetitions = n // l
                # repeated_string = substring * num_repetitions
                
                # Check if the constructed string matches the original
                if substring * (n // l) == s:
                    return True
        
        # If no repeating pattern is found after checking all possibilities
        return False