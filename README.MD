# Torneio do Dilema do Prisioneiro

![Preview](screenshot/example.png)

Bem-vindo ao **Torneio do Dilema do Prisioneiro**! Este projeto é uma simulação divertida e interativa que implementa diversas estratégias clássicas do dilema do prisioneiro, permitindo observar como cada uma se comporta em rodadas de confronto direto.

## Contexto e Objetivos

O dilema do prisioneiro é um conceito fundamental na teoria dos jogos, ilustrando a tensão entre cooperação e competição em situações onde as decisões individuais afetam o resultado coletivo. Este projeto foi desenvolvido com os seguintes propósitos:

- **Educar**: Servir como uma ferramenta didática para explicar conceitos de teoria dos jogos, mostrando na prática como diferentes estratégias podem resultar em vantagens ou desvantagens para os participantes.
- **Explorar Estratégias**: Permitir a análise comparativa de comportamentos em cenários de interação repetida, evidenciando os efeitos da cooperação, traição e retaliação.
- **Aplicar Conceitos Teóricos**: Demonstrar, através da simulação, como teorias econômicas, sociais e biológicas podem ser aplicadas para entender e prever comportamentos em sistemas complexos.

Além disso, o projeto se destaca como uma aplicação prática em áreas como economia, biologia evolutiva, sociologia e ciência da computação, onde os princípios do dilema do prisioneiro são utilizados para modelar e interpretar interações estratégicas.

### Público-Alvo

Este projeto é voltado para estudantes, pesquisadores e entusiastas de teoria dos jogos, inteligência artificial e ciências sociais. Também pode ser útil para professores que desejam demonstrar conceitos de estratégia e comportamento colaborativo de forma prática e interativa.

## Descrição

Nesta simulação, diferentes estratégias enfrentam-se em partidas com um número aleatório de rodadas (entre 50 e 200). Cada estratégia decide sua ação (cooperar ou trair) com base na última jogada do oponente. Ao fim do torneio, as pontuações são agregadas e um ranking final é exibido, tanto no terminal quanto em um gráfico de barras.

O conceito do dilema do prisioneiro foi formulado por Albert W. Tucker nos anos 1950, mas as simulações e torneios modernos de estratégias, como o realizado por Robert Axelrod em 1980, popularizaram essas ideias. Axelrod realizou um torneio com diferentes estratégias, com "Tit For Tat" sendo a vencedora devido à sua simplicidade e eficácia em contextos cooperativos.

### Estratégias Implementadas

- **Tit For Tat**: Inicia cooperando e replica o último movimento do oponente.  
- Exemplo histórico: Essa estratégia foi vencedora no famoso torneio de Robert Axelrod nos anos 80, demonstrando a eficácia da reciprocidade.
- **Always Cooperate**: Sempre coopera.
- Exemplo prático: Um grupo de indivíduos que sempre colabora pode se sair bem contra si mesmo, mas é vulnerável contra traidores.
- **Always Defect**: Sempre trai.
- Exemplo prático: Estratégias agressivas podem ser vistas em competições empresariais onde empresas sempre exploram seus concorrentes sem buscar cooperação.
- **Random**: Escolhe aleatoriamente entre trair ou cooperar.
- Exemplo prático: Em ambientes instáveis, algumas entidades podem agir de forma aleatória para confundir adversários.
- **Grudger**: Coopera até ser traído; após a traição, passa a trair para sempre.
- Exemplo histórico: Em sociedades tribais, a retaliação definitiva era uma forma de manter alianças e evitar traições.
- **Tit For Two Tats**: Coopera até que o oponente traia duas vezes seguidas, passando a trair somente após essa sequência.
- Exemplo prático: Estratégias mais tolerantes como essa podem ser vistas em negociações diplomáticas onde uma traição isolada pode ser ignorada, mas ações repetidas levam a retaliações.
- **Adaptive**: Analisa padrões de jogadas e ajusta sua estratégia ao longo do jogo.
- Exemplo prático: Inteligências artificiais que aprendem padrões de comportamento e se ajustam conforme o contexto.

As estratégias são categorizadas em dois grupos:
    - **Good Guys**: "Tit For Tat", "Always Cooperate" e "Tit For Two Tats".
    - **Bad Guys**: "Always Defect" e "Grudger".

### Regras de Pontuação

Os pontos são atribuídos a cada rodada conforme a seguinte tabela:

| Jogadas                        | Pontuação (Jogador 1, Jogador 2) |
| ------------------------------ | -------------------------------- |
| **Ambos cooperam**             | (3, 3)                           |
| **Um coopera e o outro trai**  | (0, 5) ou (5, 0)                 |
| **Ambos traem**                | (1, 1)                           |

#### Justificativa da Pontuação

Os valores da tabela seguem a estrutura clássica do dilema do prisioneiro, onde:

- **Cooperação mútua (3,3)**: Ambos se beneficiam, mas menos do que se um deles traísse.
- **Traição unilateral (0,5) ou (5,0)**: O traidor ganha mais pontos às custas do cooperador, incentivando a exploração.
- **Traição mútua (1,1)**: Ambos perdem, demonstrando que a falta de cooperação pode ser prejudicial para todos.

Essa configuração reflete o dilema fundamental: embora a melhor escolha coletiva seja a cooperação, o incentivo individual à traição pode levar a um resultado subótimo para todos.

## Como Funciona

Exemplo de Simulação

Para ilustrar melhor a dinâmica do torneio, considere a seguinte simulação:

- **Rodada 1**: "Tit For Tat" enfrenta "Always Defect".
  - "Tit For Tat" começa cooperando, mas "Always Defect" trai.
    - Pontuação: "Tit For Tat" (0), "Always Defect" (5).
- **Rodada 2**: "Tit For Tat" agora trai em resposta, e "Always Defect" continua traindo.
  - Pontuação: "Tit For Tat" (1), "Always Defect" (1).
    - O jogo continua até o final das rodadas, com as pontuações acumuladas e o ranking final exibido.

## Como Executar

 Execute o script principal:

```bash
python von.py
```

Isso iniciará a simulação e exibirá os resultados no terminal e no gráfico gerado automaticamente.

## Pré-requisitos

- **Python 3.x**
- **Bibliotecas**:
- `matplotlib`
- `numpy`

Você pode instalá-las utilizando o `pip`:

```bash
pip install matplotlib numpy
```

## Referências e Leitura Adicional

- Axelrod, R. (1984). *The Evolution of Cooperation*. Basic Books.
- Wikipedia: [Dilema do Prisioneiro](https://pt.wikipedia.org/wiki/Dilema_do_prisioneiro)
- Stanford Encyclopedia of Philosophy: [Game Theory](https://plato.stanford.edu/entries/game-theory/)
