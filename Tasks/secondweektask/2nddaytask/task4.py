# # Task 04: Magic Square Validator

# ## Objective
# Create a program that checks if a given 3x3 matrix forms a magic square.

# ## Requirements

# 1. A magic square is a square matrix where the sums of the numbers in each row, column, and both main diagonals are the same.
# 2. Ask the user to input a 3x3 matrix (nine integer values).
# 3. Check and print whether the given matrix forms a magic square.
# 4. Handle cases where the input matrix is not of size 3x3 or contains non-integer values.
def is_magic_square(matrix):
    try:
        if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
            raise ValueError("Please provide a 3x3 matrix.")

        target_sum = sum(matrix[0])

        if any(sum(row) != target_sum for row in matrix) or \
           any(sum(row[i] for row in matrix) != target_sum for i in range(3)) or \
           sum(matrix[i][i] for i in range(3)) != target_sum or \
           sum(matrix[i][2 - i] for i in range(3)) != target_sum:
            raise ValueError("This is not a magic square.")

        print("Congratulations! It's a magic square!")
        return True

    except (ValueError, IndexError):
        print("Oops! Something went wrong. Please make sure to enter a valid 3x3 matrix with whole numbers only.")
        return False


if __name__ == "__main__":
    print("Please enter the numbers for the 3x3 matrix:")
    matrix = []
    for _ in range(3):
        row = input().strip().split()
        try:
            matrix.append([int(value) for value in row])
        except ValueError:
            print("Oops! Please enter whole numbers only.")
            exit()

    is_magic_square(matrix)
