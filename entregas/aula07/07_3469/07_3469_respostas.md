Questão 1: Usando o código CodigosExcercicios/maze_builder.py, implemente uma versão do código da busca em profundidade (dfs) que seja iterativo.

Construi a função **dfs_iterativo** que utiliza de pilha definida de acordo com as posições adjacentes que ainda não foram exploradas, assim ao chegar no final de um caminho e não ter mais nenhuma posição adjacente válida, o proximo item na pilhas é a escolha feita aleatoriamente prévia.

Reutilizei de partes do código fonte de geração de labirinto deixado, principalmente na parte de definir como as direções são escolhidas e suas representações.


Questão 2: Implemente um código que, dado um labirinto gerado pelo código do item anterior, encontre um caminho partindo da posição (1,1) até o queijo.
- Implemente uma função que exibe o labirinto e o caminho achado.
- Discuta a solução que você implementou para achar o caminho, indicando  se usou uma busca em profundidade ou largura e explicando o porquê.

Construi a função **dfs_solver** que utiliza da mesma lógica de pilhas usadas para gerar o labirinto, para resolver-lo. 
No inicio defino **wall** e **maze**, que servem para posteriormente tornar a visualização mais facil e mútavel.
Se diferencia de **dfs_iterativo** ao utilizar de **parent**, dicionário que guarda a posição anterior a posição explorada, utilizado na reconstrução do caminho encontrado.

Foi reutilizado a função **print_maze**, e implementado a função **print_maze_caminho** que utiliza da lista **caminho** do retorno da função **dfs_solver**, substituindoas por setas apontando na direção da solução até o queijo. A função **print_tamanho_caminho_dfs** printa o tammanho do caminho.

A solução implementada no **dfs_solver** foi a busca em profundidade com o auxílio de uma pilha explícita e um dicionário de predecessores **parent** para a reconstrução da rota. A escolha da DFS se justifica pelas propriedades topológicas do labirinto gerado, o algoritmo utilizado na questão 1 cria um labirinto perfeito, o que matematicamente equivale a
um grafo conexo e acíclico (forma de spanning tree). Como existe apenas um caminho simples entre quaisquer dois vértices, a principal vantagem da BFS, que é garantir o menor caminho em grafos gerais, torna-se irrelevante aqui, pois o caminho encontrado pelo DFS é obrigatoriamente o único caminho possível e, por consequência, o ótimo. Além disso, a DFS apresenta menor consumo de memória em média em árvores com caminhos profundos em comparação à BFS (que precisa manter toda a fronteira de largura na fila) e permite reaproveitar a mesma estrutura de dados baseada em pilha já desenvolvida na questão 1.