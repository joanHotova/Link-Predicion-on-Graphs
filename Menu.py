import sys

class Menu:

    def filename(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~ WELCOME ~~~~~~~~~~~~~~~~~~~~~~")
        filename = input("Enter filename: ")+".txt"
        print()
        return(filename)


    def representation_menu(self):
        print("Select a number for each graph representation: ")
        print("1. Adjacency Matrix")
        print("2. Adjacency List")
        print("3. CSR")
        performance_choice = input("Your choice is: ")
        print()
        x = ["1", "2", "3"]

        while (performance_choice not in x ):
            print("Please, select a number for each graph representation from the menu below: ")
            print("1. Adjacency Matrix")
            print("2. Adjacency List")
            print("3. CSR")
            performance_choice = input("Your choice is: ")
            print()
        return performance_choice

    def metric_menu(self):
        print("Select a number for each metric: ")
        print("1. Common Neighbors")
        print("2. Jaccard Coefficient")
        print("3. Adamic/Adar")
        metric_choice = input("Your choice is: ")
        print()
        x = ["1", "2", "3"]

        x = ["1", "2", "3"]
        while (metric_choice not in x ):
            print("Please, select a number for each metric from the menu below: ")
            print("1. Common Neighbors")
            print("2. Jaccard Coefficient")
            print("3. Adamic/Adar")
            metric_choice = input("Your choice is: ")
            print()
        return metric_choice

    def k_menu(self):
        k = input("Enter the first k results you need: \n")
        try:
            return int(k)
        except ValueError:
            try:
                k = input("Please, enter a number of k results you need: \n")
                return int(k)
            except ValueError:
                print ("The program has ended. Please try again later.\nThank you!\n")
                sys.exit()

