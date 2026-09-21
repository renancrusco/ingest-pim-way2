API da WAY2 para dados de medição e consumo de energia.

Os dados passam de 2 milhões de linhas pois cada medição se refere a uma usina, e cada usina gera um valor de medição para geração e um para consumo para cada hora do dia.
A solução paliativa apresentada foi dividir o histórico contido no power bi para um Dataflow Gen1 que carrega o histórico até 2020 a 2024 e uma consulta que carrega os dados mais recentes no próprio modelo de dados do Power BI. A Api não tem paginação, oque vai ser necessário fazer adaptações no código python.