# Write a software that verifies if a number is present in a pre-defined array.
# Output example:
# Insert number 3
# The number 3 is [not] present in the array.

def verify(value_list: list[int], value: int ):

  if ( int( value ) in value_list ):
    print(f"The number {value} is  present in the array.")
  else:
    print(f"The number {value} is not present in the array.")

if __name__ == '__main__':
  N = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]
  verify(N, 3)
  