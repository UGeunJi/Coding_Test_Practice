import sys

def main():
    first_input = sys.stdin.readline().strip()
    
    while first_input:
        memory = [int(first_input, 2)] + [int(sys.stdin.readline().strip(), 2) for _ in range(31)]
        pc = 0
        adder = 0
        
        while True:
            operator = memory[pc] // 32
            operand = memory[pc] % 32
            pc += 1
            pc %= 32
            
            if operator == 0:
                memory[operand] = adder
            elif operator == 1:
                adder = memory[operand]
            elif operator == 2:
                if adder == 0:
                    pc = operand
            elif operator == 3:
                continue
            elif operator == 4:
                adder = (adder + 255) % 256
            elif operator == 5:
                adder = (adder + 1) % 256
            elif operator == 6:
                pc = operand
            elif operator == 7:
                break
                
        sys.stdout.write(f"{format(adder, '08b')}\n")
        first_input = sys.stdin.readline().strip()

if __name__ == "__main__":
    main()
