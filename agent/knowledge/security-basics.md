# Fundamentos de segurança (AppSec)

Base rápida para o agente orientar análise de vulnerabilidades de forma educativa e segura.

## Vulnerabilidade vs ameaça vs risco

**Vulnerabilidade:** é uma fraqueza no código, na configuração ou no processo que pode ser explorada. Exemplo: um login que concatena o input do usuário direto na query SQL (`SELECT * FROM users WHERE name = '` + input + `'`) — isso é uma vulnerabilidade de SQL Injection.

**Ameaça:** é quem ou o que pode explorar a fraqueza (atacante, malware, script automatizado). Exemplo: um atacante que envia `' OR '1'='1` no campo de login para tentar burlar a autenticação.

**Risco:** é a combinação do impacto que a exploração causaria com a probabilidade de ela acontecer. Exemplo: esse SQL Injection tem risco alto se o banco contém senhas e dados pessoais e a página de login é pública.

## Tríade CIA

- **Confidencialidade:** só quem tem permissão acessa a informação. Exemplo: senhas armazenadas com hash (bcrypt/argon2) em vez de texto puro.
- **Integridade:** a informação não é alterada sem autorização. Exemplo: validar no servidor o preço de um pedido em vez de confiar no valor enviado pelo navegador.
- **Disponibilidade:** o sistema continua acessível para quem precisa. Exemplo: limitar tentativas de login (rate limit) para evitar que um ataque derrube o serviço.

## Boas práticas

- **Validação de input:** valide tipo, tamanho e formato no servidor; nunca confie só no front-end.
- **Query parametrizada:** use prepared statements/ORM com parâmetros, nunca concatene input em SQL.
- **Least privilege:** dê a cada usuário, serviço e conexão de banco só o acesso mínimo necessário.
- **Updates:** mantenha linguagem, frameworks e dependências atualizados; remova o que não usa.
- **Logs:** registre eventos de segurança (login, erro, acesso negado) sem gravar senhas ou dados sensíveis.
- **Lab-only:** estude e teste vulnerabilidades apenas em ambiente próprio de laboratório, nunca em sistemas de terceiros sem autorização explícita.

## Impacto x Probabilidade -> Severidade

| Impacto \ Probabilidade | Baixa | Média | Alta |
|-------------------------|-------|-------|------|
| Baixo | Baixa | Baixa | Média |
| Médio | Baixa | Média | Alta |
| Alto | Média | Alta | Crítica |

Use sempre esse formato ao avaliar uma vulnerabilidade: **Impacto / Probabilidade / Severidade**.
