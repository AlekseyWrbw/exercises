'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
strs = ["dog","skib","car"]

strs.sort(key=len)
common_prefix = []
for i in range(1,len(strs[0])):
            for k in range(1, len(strs)):
                if strs[0][:i] in strs[k]:
                    common_prefix.append(strs[0][:i])
                elif strs[0][:i] not in strs[k] and strs[0][:i] not in common_prefix:
                    print("")
                elif strs[0][:i] not in strs[k] and strs[0][:i] in common_prefix:
                    common_prefix.remove(strs[0][:i])
print(common_prefix[-1])


