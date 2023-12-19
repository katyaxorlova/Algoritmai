answer = float('inf')
min_path = []


def tsp(graph, v, currPos, n, count, cost, path):

    global answer, min_path
    if count == n and graph[currPos][0]:
        if cost + graph[currPos][0] < answer:
            answer = cost + graph[currPos][0]
            min_path = path.copy()

    for i in range(n):
        if not v[i] and graph[currPos][i]:
            
            # pažymim kaio aplankyta
            v[i] = True
            tsp(graph, v, i, n, count + 1, cost + graph[currPos][i], path + [i])
            
            # pažymim kaip neaplankyta
            v[i] = False

# skaitom duomenis iš file
def read_graph_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        n = len(lines)
        graph = [[int(val) for val in line.split()] for line in lines]
        return graph, n


if __name__ == '__main__':
    file_name = "grafas.txt"
    graph, n = read_graph_from_file(file_name)

    #patikra ar miestas buvo aplankytas
    v = [False for _ in range(n)]
    
    # primą miestą pažymim aplankytu
    v[0] = True

    # minimalios kainos paieška
    tsp(graph, v, 0, n, 1, 0, [0])

    # Cpatikra ar galime iš paskutinio miesto sugrįžti į pradinį
    if min_path and min_path[-1] != min_path[0]:
        min_path.append(min_path[0])  

    # spausdinimas
    print("Kaina:", answer)
    print("Kelias:", min_path)
