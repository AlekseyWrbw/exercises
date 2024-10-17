'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
strs = ["abbra", "abb"]
#strs = []
print(len(strs))
#print(strs[0])


class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort(key=len)
        common_prefix = []
        if  len(strs) <=1:
            return('""')

        for i in strs[0]:
            for k in range(1, len(strs)):
                if i in strs[k][len(strs[0]):]:

                    common_prefix.append(i)
                    print(common_prefix)
                    return common_prefix
                else:
                # strs[0][:i] != strs[k][i]:
                    return "nothing"

                # elif strs[0][:i] not in strs[k] and strs[0][:i] not in common_prefix:
                #     return ""
                # elif strs[0][:i] not in strs[k] and strs[0][:i] in common_prefix:
                #     common_prefix.remove(strs[0][:i])
                #     return common_prefix[-1]

solution = Solution()

print(solution.longestCommonPrefix(strs))


###еще один вариант
def longest_common_prefix(strs):

    if not strs:
        return ""

    min_len = min(len(s) for s in strs)
    prefix = ""
    for i in range(min_len):
        char = strs[0][i]
        for s in strs[1:]:
            if s[i] != char:
                return prefix  # No common prefix
        prefix += char
    return prefix
strings = ["flower", "flow", "flight"]

result = longest_common_prefix(strings)