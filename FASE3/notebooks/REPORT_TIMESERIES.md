# Relatório Comparativo: Detecção de Anomalias em Séries Temporais

## 1. Objetivo

Este relatório, parte do entregável "IR ALÉM 2", descreve a implementação e comparação de dois métodos estatísticos para detecção de anomalias em dados de séries temporais simulando sinais vitais (BPM e temperatura).

O objetivo é identificar picos ou quedas abruptas que possam representar eventos de risco à saúde, como febre ou taquicardia, em um fluxo contínuo de dados.

O código para esta análise está no notebook `phase3_time_series.ipynb`.

## 2. Geração de Dados

Para a análise, foi gerada uma série temporal sintética com 600 pontos de dados, contendo:

-   **Padrão Normal:** Variações senoidais e ruído gaussiano para simular o comportamento normal dos sinais vitais ao longo do tempo.
-   **Anomalias Injetadas:** Oito eventos de "taquicardia" (BPM = 125) e quatro eventos de "febre" (Temperatura = 38.6°C) foram inseridos em pontos aleatórios da série para servirem como ground truth em nossa avaliação.

## 3. Métodos de Detecção de Anomalias

Foram implementados e comparados dois métodos clássicos e computacionalmente eficientes.

### Método 1: Z-score

O Z-score mede quantos desvios padrão um ponto de dados está da média da série. Pontos com um valor absoluto de Z-score acima de um limiar (neste caso, 3.0) são classificados como anomalias.

-   **Fórmula:** `z = (x - média) / desvio_padrão`
-   **Vantagens:** Simples de calcular e interpretar.
-   **Desvantagens:** É sensível a outliers, pois a média e o desvio padrão são influenciados por valores extremos. Uma anomalia pode "puxar" a média, mascarando a si mesma e outras anomalias.

### Método 2: Desvio Absoluto Mediano (MAD)

O MAD é uma alternativa mais robusta ao Z-score. Ele utiliza a mediana em vez da média e o desvio absoluto mediano em vez do desvio padrão. A mediana é menos sensível a outliers.

-   **Fórmula (simplificada):** `score = (x - mediana) / desvio_absoluto_mediano`
-   **Vantagens:** Robusto e resistente a outliers. Geralmente mais eficaz em detectar anomalias sem ser influenciado por elas.
-   **Desvantagens:** Ligeiramente mais complexo de calcular.

## 4. Resultados e Comparação

Ambos os métodos foram aplicados às séries de BPM e temperatura.

-   **Z-score:** Conseguiu detectar alguns dos picos, mas sua eficácia foi limitada. O limiar de 3.0 é um padrão comum, mas pode não ser ideal para todos os conjuntos de dados.

-   **MAD:** Mostrou-se **superior** na detecção dos eventos injetados. Ele identificou corretamente os picos de BPM e temperatura com maior precisão, pois a mediana da série não foi afetada pelos valores extremos das anomalias.

-   **Visualização:** Os gráficos no notebook mostram claramente que os pontos marcados como anômalos pelo método MAD (`'rx'`) correspondem aos picos que inserimos artificialmente, validando sua eficácia para este caso de uso.

## 5. Conclusão

Para a detecção de picos e eventos súbitos em séries temporais de sinais vitais, o método **MAD é mais recomendado** que o Z-score devido à sua robustez a outliers. 

Em um cenário de produção, onde a estabilidade e a confiabilidade do sistema de alertas são críticas, o uso de uma métrica resistente a anomalias como o MAD é fundamental. Para análises mais avançadas, poderíamos explorar modelos como ARIMA, Isolation Forest ou LSTMs, que podem capturar padrões sazonais e mais complexos nos dados.
