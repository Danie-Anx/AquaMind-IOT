# AquaMind - Sistema de Irrigação Inteligente

O **AquaMind** é uma solução completa que integra IoT, machine learning e APIs RESTful para auxiliar pequenos e médios produtores rurais a otimizar o uso da água em períodos de seca. Sensores de umidade no solo (ESP32) coletam dados de umidade e temperatura, que são processados em notebooks de análise, modelagem e pré-processamento. Um modelo de regressão prevê o nível de umidade futuro, e um classificador binário indica a necessidade de irrigação. Uma API Flask expõe o endpoint de previsão, permitindo integração com dispositivos e dashboards.

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
   git clone <URL_DO_REPO>
   cd AquaMind-IOT
   ```

2. **Instalar dependências**

   ```bash
   pip install -r requirements.txt
   ```

---

## Geração de Dados

Se não houver um arquivo `data/sensor_data.csv` real com leituras de sensores, você pode simular dados executando o script de geração ou usando a célula de simulação em `notebooks/AquaMind_Model.ipynb`.

Exemplo de script opcional `gen_data.py`:

```python
import pandas as pd, numpy as np, os
os.makedirs('data', exist_ok=True)
timestamps = pd.date_range('2025-01-01', '2025-01-07', freq='15min')
# ... simulação de soil_moisture e temperature ...
df.to_csv('data/sensor_data.csv', index=False)
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

## Próximos Passos

* Ajuste de hiperparâmetros e outras arquiteturas de modelo.
* Análise de resíduos e métricas adicionais (precision, recall, F1).
* Teste em dados reais de sensores para validação final e ajustes de features.

---

Qualquer dúvida ou sugestão, fique à vontade para abrir uma issue ou pull request. Bons testes!
