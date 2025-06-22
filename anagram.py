def isAnagram(str1, str2):

    if len(str1) != len(str2):
        return False
    
    count1,count2 = {}, {}

    for i in range(len(str1)):
        count1[str1[i]] = 1 + count1.get(str1[i], 0)
        count2[str2[i]] = 1 + count2.get(str2[i], 0)
    for key in count1:
        if count1[key] != count2.get(key, 0):
            return False
    return True

# Example usage:
if __name__ == "__main__":
    str1 = "listen"
    str2 = "silent"
    print(isAnagram(str1, str2))  # Output: True

    str1 = "hello"
    str2 = "world"
    print(isAnagram(str1, str2))  # Output: False