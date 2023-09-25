def kmp(text, subtext):
    positions = []
    if len(subtext) == 0:
        return positions

    prefix = compute_prefix(subtext)

    i = 0  # Индекс для текста
    j = 0  # Индекс для подстроки
    while i < len(text):
        if text[i] == subtext[j]:
            i += 1
            j += 1
            if j == len(subtext):
                positions.append(i - j)
                j = prefix[j - 1]
        else:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1
    return positions

def compute_prefix(pattern):
    prefix = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            prefix[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix[length - 1]
            else:
                prefix[i] = 0
                i += 1
    return prefix
