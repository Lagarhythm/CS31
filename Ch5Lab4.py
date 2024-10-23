# christopher Earl
# Chapter 5, Lab 4
import trig
import algebra


# Part 1 & 2
def main():
    val = float(input('Enter a value: '))
    which_one = int(input('Enter a number between 1 and 5 (inclusive): '))
    while which_one != 5:
        match which_one:
            case 1:
                sin_x, cos_x, tan_x = trig.trig(val)
                print(f'sin_x = {sin_x:.2f}, cos_x = {cos_x:.2f}, tan_x = {tan_x:.2f}')
                print()
            case 2:
                ceil_x, floor_x = algebra.ceilfloor(val)
                print(f'ceil_x = {ceil_x:d}, floor_x = {floor_x:d}')
                print()
            case 3:
                logx, log10x = algebra.logs(val)
                print(f'logx = {logx:.2f}, log10x = {log10x:.2f}')
                print()
            case 4:
                sqrt_x, exp_x = algebra.sqrtexp(val)
                print(f'sqrt_x = {sqrt_x:.2f}, exp_x = {exp_x:.2f}')
                print()
            case _:
                print('Invalid value entered. Try again.')
                print()
        which_one = int(input('Enter a number between 1 and 5 (inclusive): '))
    # End of while loop
    print('End of program. Thanks for coming')


main()
