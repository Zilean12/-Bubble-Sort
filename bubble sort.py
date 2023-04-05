choice=1
while(choice==1 or choice==2 or choice==3 or choice==4):
    choice=int(input('''
      1. MATRIX MULTIPLICATION
      2. MATRIX Addition
      3. MATRIX Subtraction
      4. EXIT THE PROGRAM
                         '''))
                         
    if(choice ==1):
        A_rows = int(input("Enter the number of rows in matrix A: "))
        A_cols = int(input("Enter the number of columns in matrix A: "))
        B_rows = int(input("Enter the number of rows in matrix B: "))
        B_cols = int(input("Enter the number of columns in matrix B: "))
        if A_cols != B_rows:
            print("Matrix multiplication is not possible")
            exit() 
        print("Enter elements of matrix A:")
        A = []
        for i in range(A_rows):
            row = []
            for j in range(A_cols):
                row.append(int(input(f"Enter element {j + 1} of row {i + 1}: ")))
                A.append(row)
                
        print("Enter elements of matrix B:")
        B = []
        for i in range(B_rows):
            row = []
        for j in range(B_cols):
            row.append(int(input(f"Enter element {j + 1} of row {i + 1}: ")))
            B.append(row)
            
        C = [[0 for j in range(B_cols)] for i in range(A_rows)]
        for i in range(A_rows):
            for j in range(B_cols):
                for k in range(A_cols):
                    C[i][j] += A[i][k] * B[k][j]
                    
        print("Resultant matrix:")
        for row in C:
            print(*row)

            
            
    elif(choice ==2):
            matrix1 = []
            matrix2 = []
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            print("Enter the first matrix:")
            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(int(input("Enter an element: ")))
                matrix1.append(row)
                
            print("Enter the second matrix:")
            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(int(input("Enter an element: ")))
                matrix2.append(row)
                
            result = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(matrix1[i][j] + matrix2[i][j])
                result.append(row)
            
            print("Result:")
            print(result)
            
    elif(choice ==3):
            matrix1 = []
            matrix2 = []
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            print("Enter the first matrix:")
            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(int(input("Enter an element: ")))
                matrix1.append(row)
                
            print("Enter the second matrix:")
            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(int(input("Enter an element: ")))
                matrix2.append(row)
                
            result = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    row.append(matrix1[i][j] - matrix2[i][j])
                result.append(row)
            
            print("Result:")
            print(result)
        

    elif (choice ==4):
         break

