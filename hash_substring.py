# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input()
    if input_type[0]=='I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type[0]=='F':
        filename = "tests/06"
        file = open(filename)
        pattern = file.readline().rstrip()
        text = file.readline().rstrip()  
    
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    patlen = len(pattern)
    txtlen = len(text)
    result = []
    for i in range(txtlen-patlen+1):
        if text[i:i+patlen] == pattern:
            result.append(i)

    return result
# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

