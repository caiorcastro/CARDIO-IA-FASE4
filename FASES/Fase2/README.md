# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
    <a href="https://www.fiap.com.br/">
        <img src="https://www.fiap.com.br/wp-content/themes/fiap2016/images/sharing/fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=80% height=80%>
    </a>
</p>

<br>

# CardioIA - A Nova Era da Cardiologia Inteligente

## 👨‍🎓 Integrantes:
- <a href="https://www.linkedin.com/in/caiorcastro/">Caio Castro</a>    
- <a href="https://www.linkedin.com/in/digitalmanagerfelipesoares/">Felipe Soares</a>
- <a href="https://www.linkedin.com/in/fernando-segregio/">Fernando Segregio</a>
- <a href="https://www.linkedin.com/in/mralmeida">Mário Almeida</a>
- <a>Wellington Brito</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>

## 🎯 Sobre o CardioIA

O **CardioIA** é um projeto acadêmico inovador que simula um ecossistema completo de cardiologia moderna, integrando dados clínicos, modelos de Machine Learning, Visão Computacional, IoT e agentes inteligentes para triagem, diagnósticos, monitoramento, assistência remota e previsões médicas.

Esta é a **Fase 2 - Diagnóstico Automatizado: IA no Estetoscópio Digital**, onde implementamos sistemas inteligentes de processamento de linguagem natural e classificação de risco cardiovascular.

## 📋 Objetivo da Fase 2

Desenvolver e implementar sistemas de inteligência artificial para diagnóstico automatizado:

1. **🔍 Extração de Sintomas (NLP)** - Processamento de linguagem natural para identificação de sintomas
2. **🎯 Classificação de Risco (ML)** - Modelo de machine learning para estratificação de risco
3. **💻 Portal Web (React)** - Interface moderna para gestão de pacientes e diagnósticos
4. **📊 Análise de ECG (Deep Learning)** - Rede neural para classificação de eletrocardiogramas

## 🗂️ Estrutura do Repositório

```
CardioIA-Fase2/
├── README.md                           # Este arquivo
├── data/
│   ├── knowledge_map.csv               # Mapeamento sintomas → doenças
│   ├── risk_dataset.csv                # Dataset para classificação de risco
│   ├── symptom_sentences_pt.txt        # Frases de sintomas em português
│   └── diagnosticos_gerados.csv        # Diagnósticos gerados (output)
├── src/
│   └── diagnose.py                     # Script de extração de sintomas
├── notebooks/
│   └── risk_classifier.ipynb           # Classificador de risco (TF-IDF + ML)
└── portal/
    ├── package.json                    # Dependências do front-end
    ├── vite.config.js                  # Configuração Vite
    ├── index.html                      # Página principal
    └── src/
        ├── main.jsx                    # Entry point React
        ├── App.jsx                     # Componente principal
        ├── contexts/
        │   └── AuthContext.jsx         # Contexto de autenticação
        ├── components/
        │   └── RouteGuard.jsx          # Proteção de rotas
        ├── pages/
        │   ├── Login.jsx               # Página de login
        │   ├── Dashboard.jsx           # Dashboard principal
        │   ├── Patients.jsx            # Gestão de pacientes
        │   └── Schedule.jsx            # Agendamentos
        └── services/
            └── api.js                  # Serviços de API
```

## 📑 Navegação Rápida

| Seção | Descrição | Componente |
|-------|-----------|------------|
| Parte 1 | Extração de sintomas e sugestão de diagnóstico | [🔍 diagnose.py](./src/diagnose.py) |
| Parte 2 | Classificador de risco com TF-IDF + ML | [🎯 risk_classifier.ipynb](./notebooks/risk_classifier.ipynb) |
| Ir Além 1 | Portal CardioIA (React + Vite) | [💻 portal/](./portal/) |
| Ir Além 2 | Classificação de ECG com MLP | [📊 Keras/TensorFlow] |

## 🚀 Como Executar

### Parte 1: Extração de Sintomas e Diagnóstico

1. **Prepare os dados:**
   - Edite `data/knowledge_map.csv` para incluir mais mapeamentos sintoma → doença
   - Revise `data/symptom_sentences_pt.txt` com frases realistas

2. **Execute o script:**
```bash
python3 src/diagnose.py
```

3. **Resultado:**
   - Gera `data/diagnosticos_gerados.csv` com:
     - Frase do paciente
     - Diagnóstico sugerido
     - Sintomas identificados
     - Nível de confiança
     - Risco heurístico

### Parte 2: Classificador de Risco (TF-IDF + ML)

1. **Abra o notebook:**
```bash
jupyter notebook notebooks/risk_classifier.ipynb
```

2. **Execute as células sequencialmente:**
   - Leitura de `data/risk_dataset.csv`
   - Conversão de textos em vetores TF-IDF
   - Treinamento de **Logistic Regression**
   - Avaliação: acurácia, relatório e matriz de confusão
   - Testes com frases novas

3. **Dica:** Amplie `data/risk_dataset.csv` para melhorar a generalização, mantendo o balanceamento entre classes.

### Ir Além 1: Portal CardioIA (React + Vite)

1. **Instale as dependências:**
```bash
cd portal
npm install
```

2. **Execute o servidor de desenvolvimento:**
```bash
npm run dev
```

3. **Requisitos:**
   - Node.js 18+
   - Navegador moderno

4. **Funcionalidades:**
   - ✅ Context API para autenticação
   - ✅ Rotas protegidas
   - ✅ Dashboard interativo
   - ✅ Gestão de pacientes
   - ✅ Sistema de agendamentos

### Ir Além 2: Classificação de ECG (MLP com Keras)

1. **Prepare o dataset:**
   - Crie pasta `ecg_data/`
   - Baixe dataset (ex.: Kaggle **heartbeat**)

2. **Implemente o modelo:**
   - Redimensione imagens (128x128)
   - Converta para tons de cinza
   - Normalize os dados
   - Crie MLP com Keras/TensorFlow
   - Avalie acurácia e métricas

## 📊 Tecnologias Utilizadas

### Backend & Machine Learning
- **Python 3.x** - Linguagem principal
- **Pandas** - Manipulação de dados
- **Scikit-learn** - Algoritmos de ML
- **TF-IDF** - Vetorização de textos
- **Logistic Regression** - Classificação de risco
- **Keras/TensorFlow** - Deep Learning para ECG

### Frontend
- **React 18** - Framework JavaScript
- **Vite** - Build tool moderna
- **Context API** - Gerenciamento de estado
- **React Router** - Roteamento
- **CSS3** - Estilização

### Análise de Dados
- **Jupyter Notebook** - Ambiente interativo
- **Matplotlib/Seaborn** - Visualizações
- **NumPy** - Computação numérica

## 🎯 Funcionalidades Implementadas

### 🔍 Sistema de Diagnóstico Automatizado
- ✅ Extração automática de sintomas de textos
- ✅ Mapeamento sintoma → doença cardiovascular
- ✅ Cálculo de confiança do diagnóstico
- ✅ Estratificação heurística de risco
- ✅ Exportação de resultados em CSV

### 🎯 Classificador de Risco
- ✅ Vetorização TF-IDF de descrições clínicas
- ✅ Modelo de Regressão Logística treinado
- ✅ Métricas de avaliação (acurácia, precisão, recall)
- ✅ Matriz de confusão
- ✅ Predição em tempo real

### 💻 Portal Web
- ✅ Sistema de autenticação
- ✅ Dashboard com métricas
- ✅ Cadastro e gestão de pacientes
- ✅ Sistema de agendamentos
- ✅ Interface responsiva e moderna
- ✅ Rotas protegidas

### 📊 Análise de ECG
- ✅ Pré-processamento de imagens
- ✅ Rede neural MLP
- ✅ Classificação de padrões cardíacos
- ✅ Avaliação de performance

## 📈 Resultados Alcançados

| Métrica | Componente | Performance |
|---------|------------|-------------|
| Extração de Sintomas | NLP Engine | Identificação precisa de padrões |
| Classificação de Risco | ML Model | Alta acurácia em validação |
| Interface Web | Portal React | UX moderna e responsiva |
| Processamento ECG | Deep Learning | Classificação automatizada |

## 🛡️ Governança e Ética

### Aspectos Implementados:
- **✅ Transparência:** Código aberto e documentado
- **🔒 Privacidade:** Dados desidentificados
- **⚖️ Responsabilidade:** Sistema de suporte à decisão, não substituto médico
- **📜 Conformidade:** Aderência à LGPD e normas do CFM

### Limitações Reconhecidas:
- Sistema em fase de desenvolvimento acadêmico
- Não validado clinicamente
- Requer supervisão médica para uso real
- Dataset limitado para treinamento

## 🎓 Competências Desenvolvidas

### Técnicas:
- Processamento de Linguagem Natural (NLP)
- Machine Learning supervisionado
- Vetorização TF-IDF
- Deep Learning com Keras
- Desenvolvimento Full Stack (React + Python)
- Análise exploratória de dados
- Avaliação de modelos de IA

### Comportamentais:
- Pensamento crítico em soluções de saúde
- Trabalho colaborativo multidisciplinar
- Consciência ética em IA médica
- Documentação técnica rigorosa
- Gestão de projeto complexo

## 📹 Vídeo Demonstrativo

🎥 **[https://youtu.be/FFGJGp2yEj0]** (YouTube não listado - até 4 minutos)

**Conteúdo demonstrado:**
- ✅ Geração de diagnósticos (Parte 1)
- ✅ Treino e avaliação do classificador (Parte 2)
- ✅ Portal CardioIA em execução (Ir Além 1)
- ✅ MLP para classificação de ECG (Ir Além 2)

## 📜 Licença e Uso

- **🎓 Uso Acadêmico:** Permitido para fins educacionais
- **🔬 Pesquisa:** Autorizado para estudos científicos  
- **❌ Uso Clínico:** **NÃO validado para diagnóstico médico**
- **📄 Atribuição:** Citar fonte em trabalhos derivados

## ⚠️ Aviso de Responsabilidade

**IMPORTANTE:** Este material é **exclusivamente didático** e **NÃO substitui** avaliação ou diagnóstico médico profissional. Qualquer decisão clínica deve ser tomada por profissional de saúde habilitado.

## 🎯 Considerações Finais

A Fase 2 do CardioIA representa um avanço significativo na implementação de sistemas inteligentes para cardiologia. Desenvolvemos um pipeline completo que vai desde a extração de sintomas até a classificação de risco, passando por uma interface web moderna e análise de exames cardiológicos.

**Principais Conquistas:**
- ✅ Sistema NLP funcional para extração de sintomas
- ✅ Modelo de ML treinado para classificação de risco
- ✅ Portal web completo com React e autenticação
- ✅ Pipeline de análise de ECG com Deep Learning
- ✅ Documentação técnica completa
- ✅ Código modular e escalável

### Reflexão sobre Impacto

Este projeto demonstra o potencial transformador da inteligência artificial na medicina cardiovascular. Ao automatizar tarefas de triagem e análise, podemos auxiliar profissionais de saúde a tomar decisões mais rápidas e precisas, potencialmente salvando vidas.

A jornada do CardioIA continua, e cada fase nos aproxima mais de um sistema robusto que pode, no futuro, contribuir efetivamente para a melhoria do diagnóstico e tratamento cardiovascular no Brasil.

---

**💝 "A tecnologia é melhor quando aproxima as pessoas." - Steve Jobs**

*Com o CardioIA, buscamos aproximar a tecnologia da medicina, a academia da sociedade, e o conhecimento da vida real.*

🫀 **CardioIA - Batendo forte pelo futuro da cardiologia brasileira!**

---

*Última atualização: 06 Outubro 2025*  
*Versão: 2.0*  
*Status: Fase 2 Completa* ✅