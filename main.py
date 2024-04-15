letters={}
count=0
with open(r"C:\Users\Александр\Downloads\sample.txt") as f:
    for line in f:
        if not line.startswith('>'):
            for symbol in line:
                if(symbol != '\n'):       
                    count = count +1         
                    if (symbol in letters):
                        letters[symbol] = letters[symbol] + 1
                    else:
                        letters[symbol] = 1
    for key in letters:
        print("{} - {}%".format(key,format(letters[key]/ count * 100,'.2f')))              