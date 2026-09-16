import random

def generate_maze(m, n, room=0, wall=1, cheese='.'):

    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs_iterativo(x, y):
        """Gera os caminhos do labirinto usando DFS (Depth-First Search).

        Argumentos:
            x (int): Coordenada x do ponto inicial.
            y (int): Coordenada y do ponto inicial.

        Retorna:
            maze (list): Lista de tuplas representando todas as posições do labirinto."""
        pilha = [(x, y)]
        maze[2 * x + 1][2 * y + 1] = room  

        while pilha:
            cx, cy = pilha[-1]
            adj = []

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                    adj.append((nx, ny))

            if adj:
                nx, ny = random.choice(adj)
                maze[cx + nx + 1][cy + ny + 1] = room  
                maze[2 * nx + 1][2 * ny + 1] = room  
                pilha.append((nx, ny))
            else:
                pilha.pop()

    dfs_iterativo(0, 0)

    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze


def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))
        
def dfs_solver(maze):
    """Soluciona o labirinto usando DFS (Depth-First Search).

    Argumentos:
        maze (list): Lista de tuplas representando todas as posições do labirinto.

    Retorna:
        caminho (list): Lista de tuplas representando o caminho do início até o queijo.
    """
    wall = maze[0][0]
    caminho = maze[1][1]  
    start = (1, 1)     
    pilha = [start]
    visited = set()
    parent = {start: None}
    end = None

    while pilha:
        current = pilha.pop()
        x, y = current

        if maze[x][y] not in (wall,caminho):
            end = current
            break

        visited.add(current)

       
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(maze) and 0 <= ny < len(maze[0]) 
                    and maze[nx][ny] != wall 
                    and (nx, ny) not in visited):
                if (nx, ny) not in parent:
                    parent[(nx, ny)] = current
                pilha.append((nx, ny))

    caminho = []
    while end is not None:
        caminho.append(end)
        end = parent[end]
    caminho.reverse()

    return caminho

def print_maze_caminho():
    
    for passo in range(len(caminho) - 1):
        r1, c1 = caminho[passo]
        r2, c2 = caminho[passo + 1]

        if r2 < r1:  
            maze[r1][c1] = '⬆️'
        elif r2 > r1:  
            maze[r1][c1] = '⬇️'
        elif c2 < c1:  
            maze[r1][c1] = '⬅️'
        elif c2 > c1:  
            maze[r1][c1] = '➡️'
            
    print_maze(maze)
    
def print_tamanho_caminho_dfs():
    print('\nTamanho caminho DFS:', len(caminho))

if __name__ == '__main__':
    
    m, n = 10, 14 
    room = ' '
    wall = '𒄆'
    cheese = '🪤'
       
    maze = generate_maze(m, n, room, wall, cheese)
    caminho = dfs_solver(maze)
    
    print('\nMaze')
    print_maze(maze)
    
    print('\nMaze com caminho DFS:')
    print_maze_caminho()
    print_tamanho_caminho_dfs()