import pyodbc
import pandas as pd

def error_messeage():
    print("""
          ***********************************
          *****Please enter valid input!*****
          ***********************************
          """)

def getGene():
    while True:
            gene = input("\nHello! To get started enter gene name(s)\nOr press ENTER to input txt file.\n")
            if  gene.isdigit():
                error_messeage()
                continue
            else:
                break
    if gene == "":
        filepath = input("input your file path: ")
        file = open(filepath, 'r')
        gene_name_list = file.read()
        gene = gene_name_list.split(",")
        print ("input genes: ")
        print (gene)
        file.close()     
    return(gene)    

def getPValue():
    cutoff = input("""
Press just 'ENTER' to use the default value of 0.05.
Otherwise, specify the cutoff for p-value:\n""")
    if cutoff == '':
        return(0.05)
    while True:
        try:
            cutoff = float(cutoff)
            while (cutoff < 0) or (cutoff > 1):
                print('Enter a valid input.\n')
                cutoff = float(input("""
Press just 'ENTER' to use the default value of 0.05.\n
Otherwise, specify the cutoff for p-value:\n"""))

        except ValueError:
            print('Enter a valid input.\n')
            cutoff = input("""
Press just 'ENTER' to use the default value of 0.05.\n
Otherwise, specify the cutoff for p-value:\n""")

        return(cutoff)

def getMargin():
    while True:
        try:
            margin_input = input("""
Press just 'ENTER' to use default value of 200,000.
Otherwise, specify your margin:""")

            if margin_input == '':
                return(200000)
            else:
                margin = int(margin_input)
                break
        except ValueError:
            print('Enter a valid input.\n')
    return(margin)

def exitMethod():
    exitInput = input("If you would like to exit program press 1:\nRun a new query by pressing 0\n")
    if exitInput == 1:
        quit()
    elif exitInput == 0:
        main()

def main():
     # Connect to SQL Server
    sql_conn =  pyodbc.connect("""
                               DRIVER={ODBC Driver 11 for SQL Server};
                               SERVER=PARKSLAB;
                               DATABASE=Human_GWAS;
                               Trusted_Connection=Yes;
                               """)
    while True:
        getGene()
        getMargin()
        getPValue()
        exitMethod()

   
if __name__ == "__main__":
    main()