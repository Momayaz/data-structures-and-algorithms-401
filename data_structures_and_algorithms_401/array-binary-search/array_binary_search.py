
def binary_search(lst, value):
      left_index = 0
      right_index = (len(lst)-1)

      while left_index <= right_index:
          middle = left_index + (right_index) + 1 // 2
      
          if value == lst[middle]:
              return middle
          elif value < lst[middle]:
              right_index = middle - 1
          else:
              left_index = middle + 1
      
      return -1