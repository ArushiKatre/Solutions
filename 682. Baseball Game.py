class Solution(object):
    def calPoints(self, operations):
        sums = 0
        prod = 1
        base_list = []
        for i in operations:
            if i.lstrip('-').isnumeric():
                sums = sums + int(i)
                base_list.append(int(i))
            elif i == 'C':
                base_list = base_list[:-1]
            
            elif i == 'D':
                 base_list.append(2*int(base_list[-1]))
                 
            elif i == '+':
                 base_list.append(int(base_list[-1]) + int(base_list[-2]))
                 
        sums = 0
        for i in base_list:
            sums = sums + i
        return sums