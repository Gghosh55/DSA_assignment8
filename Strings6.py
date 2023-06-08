from collections import Counter

def findAnagrams(s, p):
    p_freq = Counter(p)
    window_freq = Counter()
    left = 0
    result = []

    for right in range(len(s)):
        window_freq[s[right]] += 1

        if right - left + 1 > len(p):
            window_freq[s[left]] -= 1
            if window_freq[s[left]] == 0:
                del window_freq[s[left]]
            left += 1

        if window_freq == p_freq:
            result.append(left)

    return result
s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))
