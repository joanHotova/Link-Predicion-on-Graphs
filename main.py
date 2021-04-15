from AdjacencyMatrix import AdjacencyMatrix
from AdjacencyList import AdjacencyList
from Metrices import Metrices
from CSR import CSR
from Menu import Menu
import time

def print_k_results(top_k, string, k, dictionary):
    print("\nTop", k, "for", string, ":")
    print("(Vertex1, Vertex2, Score)")

    for t in top_k:
        print((dictionary[t[0]], dictionary[t[1]], t[2]))

def main():
    menu = Menu()
    filename=menu.filename()

    try:
        with open(filename) as f:

            performance_choice = menu.representation_menu()
            metric_choice = menu.metric_menu()
            k_choice = menu.k_menu()
            # apothhkeuoume to starting time
            begin = time.time()

            data = []
            data_temp=[]
            for line in f:
                if not (line.startswith('#')):
                    data_temp = line.split()
                for t in data_temp:
                    data.append(t)

        dataset = set(data)
        unique_list = (list(dataset))
        unique_list = list(map(int, unique_list))
        unique_list.sort()
        nums = range(len(unique_list))
        dictionary = dict(zip(nums, unique_list))
        rev_dictionary = {v: k for k, v in dictionary.items()}

        # topothetoume se ksexwristes listes ta keys kai ta values
        key_list = list(dictionary.keys())
        val_list = list(dictionary.values())

        V1 = []
        for v1 in range(0, len(data), 2):
            V1.append(data[v1])

        V2 = []
        for v2 in range(1, len(data), 2):
            V2.append(data[v2])



        if (performance_choice == "1"):
            adj = AdjacencyMatrix(key_list)

            for i in range(len(V1)):
                adj.fill_AdjMatrix(key_list[val_list.index(int(V1[i]))], key_list[val_list.index(int(V2[i]))])
            
        elif (performance_choice == "2"):
            edges = set()
            for i in range(len(V1)):
                edge = (key_list[val_list.index(int(V1[i]))], key_list[val_list.index(int(V2[i]))])
                edges.add(edge)

            edges = {tuple(sorted(item)) for item in edges}
            adj = AdjacencyList(key_list, val_list, edges)
        else:
            adj = CSR(key_list)
            for i in range(len(V1)):
                adj.fill_matrix(key_list[val_list.index(int(V1[i]))], key_list[val_list.index(int(V2[i]))])

            a1, a2, a3 = adj.csr_arrays()
           
            
        metric=Metrices()
        if (metric_choice == "1"):
            top_k=metric.common_neighbors(adj,k_choice)
            string = 'Common Neighbors'
            print_k_results(top_k, string, k_choice, dictionary)

        elif (metric_choice == "2"):
            top_k = metric.jaccard_coefficient(adj, k_choice)
            string = 'Jaccard Coefficient'
            print_k_results(top_k, string, k_choice, dictionary)
        else:
            top_k = metric.adamic(adj,k_choice)
            string = 'Adamic/Adar'
            print_k_results(top_k, string, k_choice, dictionary)

        time.sleep(1)
        end = time.time()
        total = end - begin
        total = time.gmtime(total)
        total = time.strftime("%H:%M:%S", total)
        print()
        print("Total runtime is " + total + "\n")
        print("~~~~~~~~~~~~~~~~~~~~~~ THANK YOU ~~~~~~~~~~~~~~~~~~~~~~\n")
    except FileNotFoundError as not_found:
        print("File", not_found.filename, "was not found.\n")
        print("The program has ended. Please try again later.\nThank you!\n")


if __name__ == "__main__":
    main()