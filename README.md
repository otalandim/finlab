
# FastAPI

### Criando o ambiente virtual

`python -m venv .venv`

`source /.venv/bin/activate`

### Iniciando servidor

`uv run uvicorn main:app --app-dir api --reload`

### Qualidade e Validação em Sistemas LLM

#### Problemas de vibe checking

Por que os testes manuais não funcionam em escala

- Não escala: Você não consegue testar manualmente 5-10 casos. Mas e se precisa testar 50-100 cenários?
- Não é repetível: Mesmo input pode ter avaliações diferentes dependendo do humor, cansaçõ, ou contexto
- É enviesado: Você testa naturalmente os casos óbvios e esquece dos casos extremos e edge cases
- Não gera dados: Baseado em 2-3 exemplos que você testou, você acha que melhorou. Mas melhorou mesmo?

#### Vibe checking aleatório

Testes sem estrutura e consistência

- Como está Apple?
- Microsoft é boa?
- Bitcoin?
- E a Tesla hoje?
- O que vocẽ acha de Y?
- Vale investir em X?

#### Problemas

- Testes diferentes a cada vez
- Não dá pra comparar resultados
- Esquece casos importantes
- Depende do que vem a cabeça

#### Manual estruturado

- Como está a Apple hoje?
- Analise a performance da IBM?
- O que você acha da Microsoft?
- Vale a pena investir em NVDA?

#### Benefícios

- Sempre testa os mesmos casos
- Pode comparar resultados ao longo do tempo
- Garante cobertura de casos importantes
- Identifica padrões e problemas recorrentes

#### Critérios de avaliação

- Ticker correto?
O sistema extraiu e identificou corretamente o ticker da ação?
Exemplo: "Apple" -> deveria retornar "AAPL"

- Menciona dados relevantes?
A analise inclui informações importantes (preço, volume, notícias)?
Exemplo: Menciona o preço atual, variação, contexto de mercado

- Tom apropriado?
O tom da resposta é profissional e adequado para análise financeira?
Exemplo: Evita linguagem muito casual ou promessas irrealistas

- Sem erros factuais?
As informações apresentadas são factualmente corretas?
Exemplo: Preços, datas, nomes das empresas estão corretos