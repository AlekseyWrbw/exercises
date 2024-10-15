'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
strs = ["",""]
print(len(strs))
print(strs[0])


class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort(key=len)
        common_prefix = []

        if len(strs) == 1:
            return strs[0]
        for i in range(1, len(strs[0])):
            for k in range(1, len(strs)):

                if strs[0][:i] in strs[k]:
                    common_prefix.append(strs[0][:i])

                elif strs[0][:i] not in strs[k] and strs[0][:i] not in common_prefix:
                    return ""
                elif strs[0][:i] not in strs[k] and strs[0][:i] in common_prefix:
                    common_prefix.remove(strs[0][:i])
                    return common_prefix[-1]

