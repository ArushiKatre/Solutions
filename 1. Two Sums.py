def twoSum(self, nums, target):
        output = []

        for idx_first_digit in range(len(nums)):
            temp_list = nums[:idx_first_digit] + nums[idx_first_digit+1:]

            for idx_second_digit in range(len(temp_list)):
                if target - nums[idx_first_digit] == temp_list[idx_second_digit]:
                    output.append(idx_first_digit)

                    # Original list mein second number ka index
                    if idx_second_digit >= idx_first_digit:
                        output.append(idx_second_digit + 1)
                    else:
                        output.append(idx_second_digit)

                    return output

        return output