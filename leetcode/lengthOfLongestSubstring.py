class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        length_max = 1
        if s == "":
            return 0
        else:
            while i<(len(s)):
                length_temp = 1
                for n in range(i + 1,len(s)):
                    temp = 1
                    for j in range(i,n):
                        if s[j] == s[n]:
                            temp = 0
                            length_max = max(length_temp, length_max)
                            break
                    if temp == 0:
                        break
                    elif temp == 1:
                        length_temp = length_temp + 1
                    # if s[i] != s[n]:
                    #     length_temp = length_temp + 1
                    if n==(len(s) - 1):
                        length_max = max(length_temp,length_max)
                        break
                if length_max >= (len(s)):
                    break
                i = i + 1
        return length_max

def main():
    a = Solution()
    print(len("pwwkew"))
    print(a.lengthOfLongestSubstring("pwwkew"))


if __name__ == '__main__':
    main()
