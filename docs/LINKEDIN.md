# Post LinkedIn — skill vulnerability-analysis

🛡️ Transformei o DIO Agent num mentor de AppSec!

Em vez de responder direto, ele agora:
1️⃣ pergunta o contexto antes de agir (uma pergunta por vez)
2️⃣ classifica vulnerabilidade x ameaça x risco
3️⃣ avalia Impacto / Probabilidade / Severidade + CIA
4️⃣ explica exploração em alto nível com MITRE ATT&CK (sem payload)
5️⃣ orienta a correção até query parametrizada

Testei com lab próprio:
- `app.py` com SQL Injection (`f-string`) → detectou CWE-89, T1190
- `app_fixed.py` com `?` parametrizado → mitigado, bypass=False
- `Ubuntu de laboratório exposto` → perguntou serviços antes de sugerir comando

Skill em Markdown puro: `skills/vulnerability-analysis/SKILL.md` + `agent/knowledge/security-basics.md`

Repo: https://github.com/SHURIKA6/dio-agent-riad

#Cybersecurity #AppSec #AIagents #DIO
