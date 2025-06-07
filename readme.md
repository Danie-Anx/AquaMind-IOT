# AquaMind - Sistema de Irrigação Inteligente

O **AquaMind** é uma solução completa que integra IoT, machine learning e APIs RESTful para auxiliar pequenos e médios produtores rurais a otimizar o uso da água em períodos de seca. Sensores de umidade no solo (ESP32) coletam dados de umidade e temperatura, que são processados em notebooks de análise, modelagem e pré-processamento. Um modelo de regressão prevê o nível de umidade futuro, e um classificador binário indica a necessidade de irrigação. Uma API Flask expõe o endpoint de previsão, permitindo integração com dispositivos e dashboards.

---

## Descrição do Problema
Neste documento, apresentamos o desafio de escassez hídrica enfrentado por pequenos e médios produtores rurais, explicando como a variabilidade climática e a falta de um sistema de irrigação automatizado resultam em desperdício de água, baixa produtividade e prejuízos econômicos.

## Metodologia (EDA, Pré-processamento, Modelos, Validação)

1. **Análise Exploratória de Dados (EDA)**  
   - Visualização de séries temporais de umidade e temperatura.  
   - Identificação de outliers e tratamento de valores faltantes. 

2. **Pré-processamento**  
   - Remoção de outliers com z-score.  
   - Criação de features temporais (hora, dia do ano, média móvel).  
   - Escalonamento com StandardScaler. 

3. **Modelagem**  
   - Teste de três algoritmos de regressão (Linear Regression, Decision Tree, MLP) e três classificadores (Logistic Regression, Decision Tree, Random Forest).  
   
4. **Validação**  
   - Validação cruzada k-fold (5 splits).  
   - Comparação de métricas (RMSE para regressão; acurácia para classificação).

---

## Estrutura do Projeto

```
AquaMind-IOT/
├─ api/
│  └─ model_api.py           # Servidor Flask com endpoint /predict
├─ data/
│  └─ sensor_data.csv        # CSV com leituras de umidade e temperatura
├─ models/
│  ├─ aquamind_scaler.joblib # StandardScaler serializado
│  └─ aquamind_model.joblib  # Modelo final serializado
├─ notebooks/
│  ├─ AquaMind_EDA.ipynb     # Exploração de dados e visualizações
│  ├─ AquaMind_Model.ipynb   # Pré-processamento, treinamento e avaliação
│  └─ visualizando_arquivos.ipynb # Inspeção de scaler e modelo
├─ requirements.txt          # Dependências Python
├─ test_api.py               # Script para testar endpoint Flask
└─ test_predict.py           # Script para prever localmente com o modelo
```

---

## Pré-requisitos

* Python 3.8+ instalado
* `pip` para gerenciar pacotes

---

## Instalação

1. **Clonar repositório**

   ```bash
   git clone <https://github.com/Danie-Anx/AquaMind-IOT.git>
   cd AquaMind-IOT
   ```

2. **Instalar dependências**

   ```bash
   pip install -r requirements.txt
   ```

---

## Executando os Notebooks

1. Abra **VS Code** (com extensão Jupyter) ou **JupyterLab**.
2. Execute em ordem:

   * `notebooks/AquaMind_EDA.ipynb` → Exploração, estatísticas e gráficos.
   * `notebooks/AquaMind_Model.ipynb` → Pré-processamento, treino, validação e comparações.
3. Ao final, serão gerados em `models/`:

   * `aquamind_scaler.joblib`
   * `aquamind_model.joblib`

---

## Rodando a API

1. Entre na pasta `api/`:

   ```bash
   cd api
   ```
2. Inicie o servidor Flask:

   ```bash
   python model_api.py
   ```
3. Você verá algo como:

   ```
   ```

# Running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

````

### Endpoint disponível

- **POST** `/predict`
  - Recebe JSON com chaves: `temperature`, `hour`, `dayofyear`, `roll_moist`.
  - Retorna JSON: `{ "predicted_moisture": valor }`.

---

## Testando a API

No terminal (na raiz do projeto), execute:
```bash
python test_api.py
````

Saída esperada:

```
Status code: 200
Resposta JSON: {'predicted_moisture': 39.44}
```

Ou via `curl`:

```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"temperature":28.4,"hour":15,"dayofyear":145,"roll_moist":32.1}'
```

---

## Testando Previsões Localmente

Para rodar sem a API, use o script `test_predict.py`:

```bash
python test_predict.py
```

Exemplo de saída:

```
Predicted soil moisture: 39.44%
```

---

## Resultados (RMSE, R², Acurácia, Métricas de Classificação)

- **Regressão**  
  - RMSE médio em validação cruzada: 2.246  
  - RMSE no conjunto de teste: 2.456  
  - R² no conjunto de teste: 0.880  
  
- **Classificação**  
  - Acurácia média em validação cruzada: 95.72%  
  - Acurácia no conjunto de teste: 95.6%  



## Justificativa da Escolha do Modelo
Baseamos a seleção do melhor modelo nos seguintes critérios:

- **Performance**: menor RMSE e maior R² (para regressão) ou maior acurácia (para classificação).  

- **Estabilidade**: baixo desvio-padrão nas métricas de validação cruzada.  

- **Interpretabilidade**: facilidade de explicar decisões (por exemplo, importâncias de feature na Decision Tree).  

- **Custo de erro**: priorização de minimizar falsos negativos na classificação (“solo seco não irrigado”), garantindo segurança para o produtor.
