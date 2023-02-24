def common_chars(input1, input2):
    # Find common characters between the two input strings
    common = set(input1) & set(input2)
    
    # Count the frequency of each common character in both input strings
    freq = {}
    for c in common:
        freq[c] = input1.count(c) + input2.count(c)
    
    # Convert the frequency dictionary to a list of (char, freq) tuples and sort it by frequency desc
    freq_list = sorted(freq.items(), key=lambda x: x[1], reverse=True) #key=lambda x: x[1] ascending
    
    output = ''
    for c, freq in freq_list:
        output += f"{c}{freq}"
        
    return output

# Example
input1 = "teste"
input2 = "teae"
output = common_chars(input1, input2)
print(output) 