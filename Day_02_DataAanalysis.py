# Day-02: Basic Data Analysis - Sales Revenue Calculation {Calculatetotal revenue from sales data}
# Author: Tanish Saxena
# Date: 15/12/2024

def main():
    # List of sales data containing tuples of item as each sale is fixed and oredered
    sales_data = [("Laptop",4,45000), 
                  ("Mouse",5,700),
                  ("Mobile",6,24000),
                  ("Monitor",2,15000),
                  ("Keyboard",1,300)]
    Total_Revenue = 0 # accumulator for total revenue
    for item,quantity,price in sales_data: # to unpack each sale tuple
        sale_total = quantity * price # calculate the total sale for each item
        Total_Revenue += sale_total # accumulate to total revenue
        print(f"{item} Sale Total: {sale_total}") # print each item's sale total

    print(f"\nTotal_Revenue = {Total_Revenue}") # print total revenue in the end

if __name__ == "__main__":
    main()