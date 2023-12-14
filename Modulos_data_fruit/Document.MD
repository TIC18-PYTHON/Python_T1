O código **Python** define classes e métodos para lidar com diferentes conjuntos de dados, incluindo nomes, datas, salários e idades. Ele oferece funcionalidades como inserção de dados, cálculos estatísticos simples (como média, mínimo e máximo), ordenação e iteração sobre esses conjuntos de dados.

**Classes Principais:**

Data (Classe para manipulação de datas)

**Métodos:**

__init__(self, dia=1, mes=1, ano=2000): Inicializa uma data com valores padrão ou os fornecidos pelo usuário, validando-os.
__str__(self): Retorna a representação da data no formato dia/mês/ano.

Métodos de comparação (__eq__, __lt__, __gt__): Compara datas para igualdade, menor que e maior que respectivamente.
AnaliseDados (Classe abstrata para análise de dados)
Métodos Abstratos: Define as operações básicas que devem ser implementadas pelas classes que herdam dela.
ListaNomes, ListaDatas, ListaSalarios, ListaIdades (Classes que implementam AnaliseDados)

**Métodos:**

entrada_de_dados(self): Solicita e armazena dados do usuário, validando-os conforme necessário.

mostra_mediana(self): Calcula a mediana dos dados.

mostra_menor(self): Retorna o valor mínimo dos dados.

mostra_maior(self): Retorna o valor máximo dos dados.

listar_em_ordem(self): Retorna os dados ordenados.

__iter__(self): Permite a iteração sobre os dados.

**Funcionalidades Adicionais:**

**Funções Adicionais:**

percorrer_listas_com_zip(lista_nomes, lista_salarios): Combina duas listas e exibe elementos em pares.

calcular_folha_com_reajuste(lista_salarios): Calcula salários com reajuste de 10% e os exibe.

modificar_datas_anteriores_a_2019(lista_datas): Modifica datas anteriores a 2019 para terem o dia como 1.

**Iteradores:**

iterador_zip(lista_nomes, lista_salarios): Itera sobre duas listas combinadas.

iterador_map(lista_salarios): Realiza um mapeamento sobre uma lista de salários.

iterador_filter(lista_datas): Filtra datas específicas.

**Menu:**

menu(): Um menu interativo que permite ao usuário escolher entre várias operações para cada tipo de dado.

**Como Utilizar:**

Execute menu() para acessar as opções do programa.

Escolha uma das opções numeradas para realizar a operação desejada.

Insira os dados conforme solicitado e acompanhe os resultados.

**Observações Importantes:**

Cada classe que herda de AnaliseDados implementa métodos específicos para manipular diferentes tipos de dados.

As classes ListaNomes, ListaDatas, ListaSalarios e ListaIdades são especializadas para cada tipo de dado.

As funções adicionais e iteradores são usados para executar operações específicas em diferentes conjuntos de dados.
