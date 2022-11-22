# Given two strings X and Y. The task is to find the length of the longest common substring.
 # Create a function that takes two strings of any length. 
 # X = ABCDGH and Y = ACDGH

def solution(s1, s2):

    # how we keep track of the length of longest prefix
    count = 0
    temp_count = 0

    # where we will store the prefixes
    prefixes = {}
    
    # using a "sliding frame" method to check for 
    # matches
    pointer = 0 # beginning of the "frame"
    end = 0 # end of the "frame"

    while pointer < len(s1):

        # boundary conditions:
        # 1) the end of the frame cannot be longer than the string we are examining
        # 2) if we're starting from the longer string, limit the "frame width" to 
        # the length of the smaller string
        if end > len(s1) or end - pointer > len(s1):
            pointer += 1 
            end = pointer 
            temp_count = 0 

        end += 1
        frame = s1[pointer:end]
        if frame in s2:
            temp_count += 1
            if temp_count > count:
                count = temp_count

                # returns the last match, can append if we want to 
                # get all matches if there are multiples 
                prefixes[count] = frame
        else:
            pointer += 1
            temp_count = 0

    # no matches were found
    if count == 0:
        return ""

    return prefixes[max(prefixes.keys())]

if __name__ == '__main__':
    print(solution("ABCDGH", "ACDGH"))