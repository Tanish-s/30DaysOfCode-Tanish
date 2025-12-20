# DAY 03
# Author: Tanish Saxena
# Date: 20/12/2025

def main():
    # Creating list with duplicate items
    my_list = ["hii", "hello", "hii", "welcome to python day", 3, "chapter"]
    my_set = set(my_list)  # Converting list to set to remove duplicates
    print("Original List:", my_list)
    print("Set after removing duplicates:", my_set)

    # Creating a Dictionary
    Employee_Ids = {
        "Tanish": 101,
        "Aarav": 102,
        "Mia": 103,
        "Sophia": 104,
        "Liam": 105
    }
    
    print ("\n Employee_Ids:", Employee_Ids)
    print ( "Name:", Name)
    print(Employee_Ids.get("Ta")) # Accessing value using key

if __name__ == "__main__":
    main()

# SQL Command to use Forign Key Constraint
'''-- Users table
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE
);

-- Orders table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    order_date DATE NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
-- The FOREIGN KEY constraint in the Orders table ensures that the user_id in Orders must match a valid user_id in the Users table. 
This maintains referential integrity between the two tables.'''