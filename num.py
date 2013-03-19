#!/usr/bin/env python
# coding: utf-8


has_horline = lambda x: ' ' + '-'*x + ' '
no_horline = lambda x: ' ' * (x+2)
left_verline = lambda x: '|' + ' ' * (x+1)
right_verline = lambda x: ' ' * (x+1) + '|'
both_verline = lambda x: '|' + ' '*x + '|'
no_verline = lambda x: ' ' * (x+2)

NO_TOP_LINE = ('1', '4')
NO_MID_LINE = ('0', '1', '7')
NO_BOTTOM_LINE = ('1', '4', '7')

ABOVE_MAPPING = {
        '0': both_verline,
        '1': right_verline,
        '2': right_verline,
        '3': right_verline,
        '4': both_verline,
        '5': left_verline,
        '6': left_verline,
        '7': right_verline,
        '8': both_verline,
        '9': both_verline,
    }

BELOW_MAPPING = {
        '0': both_verline,
        '1': right_verline,
        '2': left_verline,
        '3': right_verline,
        '4': right_verline,
        '5': right_verline,
        '6': both_verline,
        '7': right_verline,
        '8': both_verline,
        '9': right_verline,
    }

def get_top_line(num, size):
    return (num in NO_TOP_LINE) and no_horline(size) or has_horline(size)

def get_mid_line(num, size):
    return (num in NO_MID_LINE) and no_horline(size) or has_horline(size)

def get_bottom_line(num, size):
    return (num in NO_BOTTOM_LINE) and no_horline(size) or has_horline(size)

def get_above_line(num, size):
    return ABOVE_MAPPING[num](size)

def get_below_line(num, size):
    return BELOW_MAPPING[num](size)

def get1num(num, size):
    num_lines = []
    num_lines.append(get_top_line(num, size))
    for i in range(size):
        num_lines.append(get_above_line(num, size))
    num_lines.append(get_mid_line(num, size))
    for i in range(size):
        num_lines.append(get_below_line(num, size))
    num_lines.append(get_bottom_line(num, size))
    return num_lines

def get_all_nums(nums, size):
    all_nums = []
    for num in nums:
        all_nums.append(get1num(num, size))
    return zip(*all_nums)

def get_output(nums, size):
    nums_lines = get_all_nums(nums, size)
    output_lines = [''.join(i) for i in nums_lines]
    return '\n'.join(output_lines)

if __name__ == '__main__':
    import sys
    size = int(sys.argv[1])
    nums = sys.argv[2]
    print get_output(nums, size)
     
