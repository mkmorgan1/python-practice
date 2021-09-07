class Solution:
    def romanToInt(self, s: str) -> int:
        def recurse(string, total):
            if string[-1] == 'M':
                total += 1000
            elif string[-1] == 'D':
                total += 500
            elif string[-1] == 'C':
                if total >= 500:
                    total -= 100
                else:
                    total += 100
            elif string[-1] == 'L':
                total += 50
            elif string[-1] == 'X':
                if total >= 50:
                    total -= 10
                else:
                    total += 10
            elif string[-1] == 'V':
                total += 5
            elif string[-1] == 'I':
                if total >= 5:
                    total -= 1
                else:
                    total += 1

            string = string[:-1]
            if len(string) > 0:
                return recurse(string, total)
            else:
                return total
        return recurse(s, 0)
