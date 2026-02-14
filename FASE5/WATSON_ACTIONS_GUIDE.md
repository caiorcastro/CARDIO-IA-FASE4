# Guia de Criação Manual - IBM Watson Actions (Fase 5)

Como as novas instâncias do IBM Watson utilizam o modelo **Actions**, siga este passo a passo:

## 1. Acessando
1. Abra seu Assistant no IBM Cloud.
2. Clique em **Actions**.
3. Clique em **New action**.

---

## 2. Action: "Saudação"
1. **When customer says:** `Oi`, `Olá`, `Bom dia`.
2. **Assistant says:** "Olá! Sou o **Assistente CardioIA**. 🫀\n\nEstou aqui para monitorar sua saúde cardíaca. Como posso ajudar?"
3. **Define customer response:** *Options*.
    *   `Agendar Consulta`
    *   `Emergência / Dor no Peito`

---

## 3. Action: "Emergência" (CRÍTICA)
1. **When customer says:** `Dor no peito`, `Infarto`, `Socorro`.
2. **Step 1:**
    *   **Assistant says:** "🔴 **ALERTA DE EMERGÊNCIA** 🔴\nA dor irradia para o braço esquerdo ou mandíbula? Você sente náusea?"
    *   **Define customer response:** *Options*.
    *   `Sim`
    *   `Não`
3. **Step 2 (Condicional - SE Sim):**
    *   **Condition:** `If Step 1 is Sim`
    *   **Assistant says:** "🚨 **AÇÃO IMEDIATA**\n\n1. Pare tudo e sente-se.\n2. Mastigue uma aspirina.\n3. **LIGUE 192 (SAMU).**"
4. **Step 3 (Condicional - SE Não):**
    *   **Condition:** `If Step 1 is Não`
    *   **Assistant says:** "Mesmo sendo leve, dores no peito devem ser investigadas. Gostaria de agendar uma consulta?"
    *   **Define customer response:** *Confirmation* (Yes/No).

---

## 4. Action: "Agendamento"
1. **When customer says:** `Agendar`, `Marcar consulta`.
2. **Step 1:**
    *   **Assistant says:** "Para qual data você gostaria de agendar?"
    *   **Define customer response:** *Date*.
3. **Step 2:**
    *   **Assistant says:** "Perfeito. Pré-agendei para **${step_1_result}**. Você receberá a confirmação por e-mail."

---

## 5. Publicar e Conectar
1. Vá em **Publish** -> **Publish**.
2. Vá em **Environment Settings** (engrenagem) -> **API Details**.
3. Copie: `Service URL` e `Environment ID` (este será seu `ASSISTANT_ID` no `.env`).
