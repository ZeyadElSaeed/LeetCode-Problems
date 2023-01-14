class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        neighbors = collections.defaultdict(set)
        for a, b in zip(s1, s2):
            neighbors[a].add(b)
            neighbors[b].add(a)

        memo = {}

        def bfs(ch):
            if ch in memo: return memo[ch]
            res = ch
            seen = set()
            queue = {ch}

            while queue:
                c = queue.pop()
                if c in seen: continue
                seen.add(c)
                res = min(res, c)
                queue |= neighbors[c]

            for v in seen:
                memo[v] = res

            return res
        return ''.join(bfs(c) for c  in baseStr)