try:
        def create_board(rows, columns):
 
                for row in range(rows):
                    if row % 2 == 0:
                        for col in range(1, columns):
                            if col % 2 == 1:
                                if col != columns - 1:
                                    print(" ", end="")
                                else:
                                    print(" ")
                            else:
                                print("|", end="")
                    else:
                        print("-" * columns)
        
                        return True
    

        create_board(20,20)

except:
        print("Error Character, Please check again your data")
finally:
        print("Acquired data")
