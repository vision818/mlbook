def min_inequity(salaries, n):
  salaries.sort()
  salary_length = len(salaries)
  min_inequity = salaries[-1]
  for i in range(salary_length - n + 1):
    if salaries[i+n-1] - salaries[i] < min_inequity:
      min_inequity = salaries[i+n-1] - salaries[i]
      
  return min_inequity

# Test the function with a sample input
print(min_inequity([2,3,6,8,13], 4)) # Output: 20000

