def parse_long_direction(instruction):
    direction = str(instruction).zfill(5)
    direction_dict={}
    param_1_mode, param_2_mode, param_3_mode, opcode = int(direction[2]), int(direction[1]), int(direction[0]), int(direction[-2:])
    return [opcode, param_1_mode, param_2_mode, param_3_mode]

def diagnosis_code(program, input = 1):
    opcode_index = 0
    while True:
        opcode = program[opcode_index]
        if opcode > 99:
            direction = parse_long_direction(opcode)[0]
            for i in range(1,4):
                if parse_long_direction(direction)[i] == 0:
                    element_i = program[opcode_index + i]
                else:
                    element_i = opcode_index + 1
            if direction == 99:
                break   
            elif direction == 1:
                program[element_3] = program[element_1] + program[element_2]
            elif direction == 2:
                program[element_3] = program[element_1] * program[element_2]
                opcode_index +=4
            elif direction == 3:
                program[element_1] = input
                opcode_index +=2
            elif direction == 4:
                print(element_1 + "!")
                opcode_index +=2
        elif opcode == 99:
            break
        elif opcode == 1:
            program[program[opcode_index + 3]] = program[program[opcode_index + 2]] + program[program[opcode_index + 1]]
            opcode_index +=4    
        elif opcode == 2:
            program[program[opcode_index + 3]] = program[program[opcode_index + 2]] * program[program[opcode_index + 1]]
            opcode_index +=4 
        elif opcode == 3:
            print(opcode)
            program[opcode_index+1] = input
            opcode_index +=2
        elif opcode == 4:
            print(program[opcode_index + 1] + "!!") 
    intcode = list(map(int, open('input.txt', 'r').read().split(','))) #Resets intcode
    print("The program has terminated.")

intcode = list(map(int, open('input.txt', 'r').read().split(',')))

diagnosis_code(intcode)