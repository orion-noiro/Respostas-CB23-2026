import time
import random
import AulasPraticas.AP_03_ordenacao as ap3
import sys

sys.setrecursionlimit(100000) 


def avg_case(tamanhos_testados):
    listas = {}
    for n in tamanhos_testados:
        listas[n] = random.choices(range(n + 1), k=n)
    return listas


def worst_case(tamanhos_testados):
    listas = {}
    for n in tamanhos_testados:
        listas[n] = list(range(n, 0, -1))
    return listas

### Geração de tabela por IA
def criar_tabela_ranking_resultados_media_tempos(times, tamanhos_testados):
    qtd_tamanhos = len(tamanhos_testados)
    num_testes = len(times["SelectionSort_avg"]) // qtd_tamanhos

    print("\n" + "═" * 78)
    print(
        f" RESULTADOS: MÉDIA DE TEMPOS E RANKING ({num_testes} teste(s) por tamanho) ".center(
            78, "═"
        )
    )
    print("═" * 78)

    # 1. TABELA RESUMO GERAL (Visão lado a lado por tamanho)
    print("\n📊 VISÃO GERAL DOS TEMPOS MÉDIOS:\n")
    headers = [
        "N",
        "Selection (Avg)",
        "Selection (Pior)",
        "Merge (Avg)",
        "Merge (Pior)",
        "Quick (Avg)",
        "Quick (Pior)",
    ]
    larguras = [8, 16, 16, 14, 14, 14, 14]

    # Linha de cabeçalho
    sep_topo = (
        "┌" + "┬".join("─" * (w + 2) for w in larguras) + "┐"
    )
    sep_meio = (
        "├" + "┼".join("─" * (w + 2) for w in larguras) + "┤"
    )
    sep_base = (
        "└" + "┴".join("─" * (w + 2) for w in larguras) + "┘"
    )

    print(sep_topo)
    header_str = "│" + "│".join(
        f" {h.center(w)} " for h, w in zip(headers, larguras)
    ) + "│"
    print(header_str)
    print(sep_meio)


    medias_por_tamanho = {n: {} for n in tamanhos_testados}

    for idx, n in enumerate(tamanhos_testados):
        for algoritmo in times:

            valores = [
                times[algoritmo][rodada * qtd_tamanhos + idx]
                for rodada in range(num_testes)
            ]
            medias_por_tamanho[n][algoritmo] = sum(valores) / len(valores)

        linha = [
            str(n),
            formatar_tempo(medias_por_tamanho[n]["SelectionSort_avg"]),
            formatar_tempo(medias_por_tamanho[n]["SelectionSort_worst"]),
            formatar_tempo(medias_por_tamanho[n]["MergeSort_avg"]),
            formatar_tempo(medias_por_tamanho[n]["MergeSort_worst"]),
            formatar_tempo(medias_por_tamanho[n]["QuickSort_avg"]),
            formatar_tempo(medias_por_tamanho[n]["QuickSort_worst"]),
        ]
        linha_str = "│" + "│".join(
            f" {col.center(w)} " for col, w in zip(linha, larguras)
        ) + "│"
        print(linha_str)

    print(sep_base)

    print("\n🏆 RANKING DE VELOCIDADE POR TAMANHO:\n")

    for n in tamanhos_testados:

        ranking = sorted(
            medias_por_tamanho[n].items(), key=lambda item: item[1]
        )

        print(f"🔹 Tamanho N = {n}")
        print("┌─────────┬──────────────────────────┬────────────────┐")
        print("│ Posição │ Algoritmo / Caso         │ Tempo Médio    │")
        print("├─────────┼──────────────────────────┼────────────────┤")

        medalhas = {0: "🥇 1º", 1: "🥈 2º", 2: "🥉 3º"}
        for pos, (alg, media_ns) in enumerate(ranking):
            pos_str = medalhas.get(pos, f"   {pos + 1}º")
            alg_formatado = alg.replace("_", " (") + ")"
            tempo_formatado = formatar_tempo(media_ns)
            print(
                f"│ {pos_str:<7} │ {alg_formatado:<24} │ {tempo_formatado:>14} │"
            )

        print("└─────────┴──────────────────────────┴────────────────┘\n")

def formatar_tempo(ns):

    if ns < 1_000:
        return f"{ns:.1f} ns"
    elif ns < 1_000_000:
        return f"{ns / 1_000:.2f} µs"
    elif ns < 1_000_000_000:
        return f"{ns / 1_000_000:.3f} ms"
    else:
        return f"{ns / 1_000_000_000:.3f} s"
### 
tamanhos_testados = list(map(int, input("Digite os tamanhos das listas a serem testadas (separados por espaço): ").split()))
numero_de_testes = int(input("Digite o número de testes: "))

times = {
    "SelectionSort_avg": [],
    "SelectionSort_worst": [],
    "MergeSort_avg": [],
    "MergeSort_worst": [],
    "QuickSort_avg": [],
    "QuickSort_worst": [],
}

for _ in range(numero_de_testes):
    listas_avg = avg_case(tamanhos_testados)
    listas_worst = worst_case(tamanhos_testados)

    for n in tamanhos_testados:

        start_time = time.perf_counter_ns()
        ap3.selection_sort(listas_avg[n].copy())
        times["SelectionSort_avg"].append(time.perf_counter_ns() - start_time)

        start_time = time.perf_counter_ns()
        ap3.selection_sort(listas_worst[n].copy())
        times["SelectionSort_worst"].append(time.perf_counter_ns() - start_time)

        start_time = time.perf_counter_ns()
        ap3.divide_and_conquer_sort(listas_avg[n].copy())
        times["MergeSort_avg"].append(time.perf_counter_ns() - start_time)

        start_time = time.perf_counter_ns()
        ap3.divide_and_conquer_sort(listas_worst[n].copy())
        times["MergeSort_worst"].append(time.perf_counter_ns() - start_time)

        start_time = time.perf_counter_ns()
        ap3.quick_sort(listas_avg[n].copy())
        times["QuickSort_avg"].append(time.perf_counter_ns() - start_time)

        start_time = time.perf_counter_ns()
        ap3.quick_sort(listas_worst[n].copy())
        times["QuickSort_worst"].append(time.perf_counter_ns() - start_time)


criar_tabela_ranking_resultados_media_tempos(times, tamanhos_testados)