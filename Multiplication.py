with open('Random.txt', 'r') as inp, open('Mul.txt', 'w') as outp:
    total = 1
    for line in inp:
        if line.strip().isdigit():
            total += int(line)
    outp.write(str(total))

inp.close()
outp.close()