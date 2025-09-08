import numpy as np

def input_matrix(name, rows=None, cols=None):
    if rows is None or cols is None:
        rows = int(input(f"Enter the number of rows for Matrix {name}: "))
        cols = int(input(f"Enter the number of columns for Matrix {name}: "))
    print(f"Enter {cols} values for Matrix {name}, row by row (space separated):")

    matrix_data = []
    for i in range(rows):
        while True:
            try:
                row_values = list(map(float, input(f"Row {i+1}: ").split()))
                if len(row_values) != cols:
                    print(f"Please enter exactly {cols} values.")
                    continue
                matrix_data.append(row_values)
                break
            except ValueError:
                print("⚠️ Invalid input. Please enter numbers only.")
    return np.array(matrix_data)

def display_matrix(matrix, name="Result"):
    print(f"\n{name}:")
    print(matrix)


def main():
    print("█████████ Welcome to the Matrix Operations Tool █████████")

    # Input both matrices with same size at the beginning
    rows = int(input("Enter the number of rows for both matrices: "))
    cols = int(input("Enter the number of columns for both matrices: "))
    A = input_matrix("A", rows, cols)
    B = input_matrix("B", rows, cols)

    while True:
        print("\nChoose an operation:\n"
              "1. Addition\n"
              "2. Subtraction\n"
              "3. Multiplication\n"
              "4. Transpose (A or B)\n"
              "5. Determinant (A or B)\n"
              "7. Restart (Enter new Matrices)\n"
              "6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":  # Addition
            if A.shape == B.shape:
                result = A + B
                display_matrix(result, "Result of Addition")
            else:
                print("❌ Error: Matrices must have the same dimensions for Addition.")

        elif choice == "2":  # Subtraction
            if A.shape == B.shape:
                result = A - B
                display_matrix(result, "Result of Subtraction")
            else:
                print("❌ Error: Matrices must have the same dimensions for Subtraction.")

        elif choice == "3":  # Multiplication
            if A.shape[1] == B.shape[0]:
                result = np.dot(A, B)
                display_matrix(result, "Result of Multiplication (A × B)")
            else:
                print("❌ Error: Columns of A must equal rows of B for Multiplication.")

        elif choice == "4":  # Transpose
            matrix_choice = input("Transpose Matrix A or B? (A/B): ").strip().upper()
            if matrix_choice == "A":
                display_matrix(A.T, "Transpose of A")
            elif matrix_choice == "B":
                display_matrix(B.T, "Transpose of B")
            else:
                print("❌ Invalid choice.")

        elif choice == "5":  # Determinant
            matrix_choice = input("Determinant of Matrix A or B? (A/B): ").strip().upper()
            if matrix_choice == "A":
                if A.shape[0] == A.shape[1]:
                    print(f"Determinant of A: {np.linalg.det(A):.2f}")
                else:
                    print("❌ Error: Determinant can only be calculated for square matrices.")
            elif matrix_choice == "B":
                if B.shape[0] == B.shape[1]:
                    print(f"Determinant of B: {np.linalg.det(B):.2f}")
                else:
                    print("❌ Error: Determinant can only be calculated for square matrices.")
            else:
                print("❌ Invalid choice.")

        elif choice == "6":  # Exit
            print("---- Exiting Matrix Operations Tool. Goodbye! ----")
            break

        elif choice == "7":  # Restart with new matrices
            print("\n🔄 Restarting... Please enter new matrices.")
            rows = int(input("Enter the number of rows for both matrices: "))
            cols = int(input("Enter the number of columns for both matrices: "))
            A = input_matrix("A", rows, cols)
            B = input_matrix("B", rows, cols)

        else:
            print("❌ Invalid choice. Please select from (1-7).")


if __name__ == "__main__":
    main()
