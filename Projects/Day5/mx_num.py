# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# #sum of all studens scores
# sum_of_scores = 0
# for score in student_scores:
#     sum_of_scores += score
# # print(sum_of_scores)

# # Highest score
# max_score = 0

# for score in student_scores:
#     if max_score < score:
#         max_score = score
# print(max_score)

# #summing numbers with range
# sum_of_nums = 0
# for num in range(1, 101):
#     sum_of_nums += num
# print(sum_of_nums)
        
        
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        num = "FizzBuzz"
    elif num % 3 == 0:
        num = "Fizz"
    elif num % 5 == 0:
        num = "Buzz"
    print(num)
