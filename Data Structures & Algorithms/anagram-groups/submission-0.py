class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            #sorted returns a list, so we need to create a string
            key = "".join(sorted(s))

            if key in groups:
                groups[key].append(s)

            else:
                groups[key] = [s]
            
        return list(groups.values())
        