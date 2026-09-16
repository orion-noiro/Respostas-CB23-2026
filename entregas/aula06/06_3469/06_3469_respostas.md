# Análise de Complexidade — Aula 06

**Aluno (Matrícula):** 3469  
**Disciplina:** CB23 — 2026

---

## 1. Por que desenfileirar() pode custar O(N) em uma chamada isolada?

Em uma chamada específica ao método desenfileirar(), o pior caso acontece quando:
1. A pilha_saida está completamente vazia; e
2. A pilha_entrada contém todos os N elementos enfileirados até o momento.

Nessa situação, para conseguir remover o elemento mais antigo (respeitando a regra FIFO da fila), a estrutura precisa transferir todos os N elementos da pilha_entrada para a pilha_saida.

Essa transferência envolve:
* N chamadas de pop() na pilha_entrada; e
* N chamadas de push() na pilha_saida.

Como cada push e pop custa O(1), a estrutura realiza 2N operações no total. Por isso, o custo temporal dessa chamada específica é proporcional a N, ou seja, O(N).

---

## 2. Por que a complexidade é O(1) amortizada?

Apesar de uma chamada isolada poder custar O(N), esse custo elevado acontece muito raramente. A complexidade média (amortizada) ao longo do tempo é O(1). 

Podemos provar isso analisando o ciclo de vida de cada elemento: do momento em que ele entra até o momento em que sai da fila, cada elemento passa exatamente por 4 passos:

1. inserção na pilha_entrada ao enfileirar (custo O(1))
2. remoção da pilha_entrada durante a transferência (custo O(1))
3. inserção na pilha_saida durante a transferência (custo O(1))
4. remoção definitiva da pilha_saida ao desenfileirar (custo O(1))

Nenhum elemento é transferido mais de uma vez entre as pilhas e nenhum elemento volta para a entrada. Logo, cada item que entra na fila gera no máximo 4 operações elementares de pilha ao longo de toda a sua existência.

Para qualquer sequência de X operações na fila (misturando enfileirar e desenfileirar):
* O número total de operações de pilha nunca ultrapassa 4 * X;
* O custo total acumulado é limitado por O(X).

Portanto, a chamada demorada de O(N) na transferência já foi "paga antecipadamente" pelas inserções anteriores, garantindo que o custo amortizado por operação seja O(1).