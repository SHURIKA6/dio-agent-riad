# 🤖 DIO Agent

> Seu mentor com Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar, praticar e planejar a sua carreira.

Você não precisa saber programar nem instalar nada complicado. Em **3 passos**, o seu mentor está pronto para usar.

---

## ✨ Três palavras para começar

- 🧠 **Agente de IA:** um chatbot responde perguntas. Um *agente* vai além: lê, planeja e executa passos para ajudar você a alcançar um objetivo. É a diferença entre alguém que explica o caminho e alguém que caminha junto com você.
- 🖥️ **Harness:** é o programa onde o agente roda. O agente é o mentor, e o harness é a sala onde vocês se encontram. O mesmo mentor atende em salas diferentes, por isso o DIO Agent funciona em vários harnesses.
- 🧩 **Skill:** é uma habilidade do agente, descrita em um guia passo a passo. Você não precisa chamar a skill: o agente percebe o que você precisa e usa a certa sozinho.

Esses e outros termos estão no [Glossário](docs/glossary.md).

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um harness

Recomendamos o **Google Antigravity**, que tem limites de uso generosos para quem está começando. Mas qualquer harness da lista funciona: escolha um e siga a instalação da documentação oficial dele.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://code.claude.com/docs |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

### 2️⃣ Baixe o DIO Agent e abra no harness

Baixe este repositório do jeito mais simples para você:

- **Com Git:** no terminal, rode `git clone https://github.com/digitalinnovationone/dio-agent.git`
- **Sem Git:** no topo desta página, clique no botão verde **Code**, depois em **Download ZIP**, e extraia a pasta.

Depois, abra no harness a pasta do projeto, a que tem o arquivo `AGENTS.md` (pelo Git, ela se chama `dio-agent`; pelo .zip, `dio-agent-main`). O harness lê esse arquivo sozinho, e o agente já sabe quem é: o seu mentor de estudos da DIO.

### 3️⃣ Converse

Fale naturalmente, com as suas palavras. Nas primeiras vezes, vale usar um dos [modelos de prompt](#-modelos-de-prompt) abaixo: quanto mais contexto você dá, melhor o agente ajuda.

---

## 🧩 As skills do agente

| Skill | Para que serve | Experimente pedir |
|-------|----------------|-------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Quero concluir este Bootcamp em 2 meses, me ajuda?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta | "Travei nesse desafio, me ajuda?" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma simples, com analogias e exemplos | "Não entendi o que é uma API." |
| [Pesquisa na web](skills/web-search/SKILL.md) | Responde dúvidas atuais (versões, lançamentos, mercado) com fontes citadas | "Qual a versão estável do Node hoje?" |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Dá feedback sobre o seu portfólio e GitHub antes de buscar vagas | "O que falta no meu GitHub para uma vaga júnior?" |
| [Caminho AI Builder](skills/ai-builder-path/SKILL.md) | Ajuda você a escolher o próximo passo na Carreira AI Builder | "Qual Formação AI Builder combina comigo?" |
| [Análise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md) | Entende o contexto, avalia impacto/probabilidade/severidade e orienta a correção | "Achei um possível SQL Injection no meu projeto, me ajuda?" |

A pesquisa na web usa a busca do seu harness. Se ele não tiver busca própria, veja [como conectar o You.com](docs/youcom-mcp.md), que tem uma opção gratuita.

### 🛡️ Especialização AppSec

O agente também atua como mentor de segurança de aplicações: antes de sugerir qualquer passo, ele pergunta o contexto (linguagem, onde o app roda, se é seu ambiente de laboratório) e só orienta testes em ambiente próprio.

Toda análise usa um formato fixo — **Impacto / Probabilidade / Severidade** — para você aprender a priorizar correções como um profissional de segurança.

---

## 📝 Modelos de prompt

Copie, preencha o que está entre colchetes e envie. Não precisa de formato perfeito: o agente pede mais detalhes se precisar.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos.
- Meu objetivo: [ex: ser dev back-end, concluir um Bootcamp]
- O que quero fazer na DIO: [link ou nome do Bootcamp, Formação, Aceleração ou Carreira]
- O que já tenho: [um plano de ação ou de estudos, se tiver]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou, no Desafio de Projeto, o link do repositório do desafio]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código ou repositório: [cole o código ou o link, se tiver]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
```

**🧭 Caminho AI Builder**

```
Quero escolher meu próximo passo na Carreira AI Builder.
- O que quero construir com IA: [ex: um produto para o meu negócio, um software, agentes que automatizam processos, ainda não sei]
- Minha experiência com programação: [nenhuma, o básico, trabalho com desenvolvimento]
- Meu objetivo: [ex: mudar de carreira, tirar uma ideia do papel]
```

---

## 🔄 Mantenha o DIO Agent atualizado

O DIO Agent evolui com o tempo. Se você usou Git, rode `git pull` no terminal, dentro da pasta (ou peça para o próprio agente rodar). Se baixou o .zip, baixe de novo.

---

## 🗂️ Estrutura do repositório

```
dio-agent-riad/
├── README.md                Este guia + entrega AppSec
├── AGENTS.md                Definição do agente (lida pelo harness)
├── CLAUDE.md                Atalho para o Claude Code
├── app.py                   Lab vulnerável (SQL Injection de propósito)
├── app_fixed.py             Lab corrigido (query parametrizada)
├── agent/
│   ├── persona.md           Personalidade + Modo AppSec
│   └── knowledge/           O que o agente sabe
│       ├── dio-platform.md
│       ├── learning-experiences.md
│       └── security-basics.md  Fundamentos: vuln/ameaça/risco, CIA, boas práticas
├── skills/                  Uma pasta por skill, cada uma com o seu SKILL.md
│   └── vulnerability-analysis/
│       ├── SKILL.md         Roteiro defensivo do agente
│       └── README.md        Explicação da skill para humanos
└── docs/
    ├── glossary.md          Glossário de termos
    └── youcom-mcp.md        Como conectar a busca do You.com
```

---

## 🛡️ Entrega: especialização AppSec (dio-agent-riad)

### A especialização que dei ao agente, e por quê
Transformei o DIO Agent num mentor de AppSec que não responde direto: ele pergunta o contexto antes de agir, classifica vulnerabilidade x ameaça x risco, avalia Impacto / Probabilidade / Severidade + CIA, explica a exploração em alto nível com técnica MITRE ATT&CK (sem payload pronto) e orienta a correção de forma socrática. Escolhi AppSec porque é porta de entrada para segurança e treina o pensamento defensivo só com Markdown, sem treinar modelo.

### Quais arquivos criei ou alterei
- Criados: `skills/vulnerability-analysis/SKILL.md`, `skills/vulnerability-analysis/README.md`, `agent/knowledge/security-basics.md`, `app.py`, `app_fixed.py`
- Alterados: `agent/persona.md` (+ `## Modo AppSec`), `AGENTS.md` (+ linha na tabela Skills + bullet do knowledge), `README.md` (+ linha na tabela + esta seção)

### Como rodar o agente no harness, e a melhoria que escolhi
1. `git clone <seu-fork-dio-agent-riad> && cd dio-agent-riad`
2. Abra o terminal **nesta pasta** e rode `hermes` (se abrir em outro lugar ele não acha os arquivos).
3. Teste 1: `Tenho um login em app.py que monta SQL com f-string, é lab local. Como especialista AppSec, ache a falha, explique exploração, cite MITRE ATT&CK e oriente a correção.` → deve perguntar contexto, classificar, dar Severidade e guiar até query parametrizada.
4. Teste 2: troque por `app_fixed.py` e peça re-varredura → deve confirmar mitigação.
5. Teste 3: `Tenho um Ubuntu de laboratório exposto na internet` → deve perguntar versão/serviços/rede antes de sugerir qualquer comando.
- Melhoria escolhida: **formato fixo de saída** em toda análise (`Contexto / Classificação / Avaliação Impacto-Prob-Severidade + CIA / Exploração alto nível + MITRE / Correção guiada / Validação / Entendimento`) para comparar casos. Ideias futuras: skill de trilha de estudos, skill de testes de segurança, review DevSecOps por diff.

### Evidências (prints)
Salve os prints em `docs/prints/` com estes nomes:

- `docs/prints/print-analise-app.png` — análise do `app.py`: CWE-89, T1190, Impacto/Prob/Severidade + orientação para `app_fixed.py`
- `docs/prints/print-revarredura-fixed.png` — re-varredura do `app_fixed.py` confirmando mitigação (query fixa com `?`, testes SQLite memória)
- `docs/prints/print-contexto-ubuntu.png` — cenário `Ubuntu de laboratório exposto`: agente pergunta serviços/contexto antes de sugerir comando

> Todos os testes usam só código e servidores de laboratório próprios (`sqlite :memory:`, dados fictícios). Nada de sistemas reais.

---

## 🤝 Contribua

Tem uma ideia de skill? Veja [como criar uma skill](skills/README.md) e abra um pull request.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você nos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀
