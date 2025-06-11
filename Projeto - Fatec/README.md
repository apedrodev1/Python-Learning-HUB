# 📦 Sistema de Controle de Estoque - Elevah

Projeto final da disciplina **Laboratório de Engenharia de Software** da **FATEC Mococa**, orientado pela professora **Jaciara Silva Carosia**.

---

## 🧿 Sobre o Projeto

Este projeto tem como objetivo desenvolver um sistema simples e funcional para **controle de entrada e saída de produtos**, auxiliando a gestão de estoque da empresa **Elevah**, especializada em **produtos místicos e naturais**.

🔗 Instagram da Elevah: [@elevah.club](https://www.instagram.com/elevah.club/)

---

## 🧰 Tecnologias Utilizadas

- **Python 3.10+**
- Estrutura de arquivos em **JSON**
- Interface via terminal (CLI)
- Organização modular em pastas (`functions`, `data`, etc.)

---

## 📂 Estrutura do Projeto

```
.
├── data/                     # Armazena os arquivos JSON (produtos, registros, usuários)
│   ├── products.json
│   ├── input.json
│   ├── output.json
│   └── users.json
│
├── functions/                # Funções modulares
│   ├── entrada.py
│   ├── saida.py
│   └── loguin.py
│
├── products.py               # Módulo que gerencia o banco de produtos
├── index.py                  # Tela inicial com login (simulado)
├── main_page.py              # Página principal do sistema
├── README.md                 # Este arquivo
└── requirements.txt          # (Opcional) Dependências do projeto
```

---

## 🔄 Funcionalidades

- ✅ **Login ilustrativo**
- ✅ **Registro de entrada de produtos**
- ✅ **Registro de saída de produtos**
- ✅ **Atualização automática do estoque**
- ✅ **Validação de códigos RFID**
- ✅ **Persistência local com arquivos JSON**

---

## 📁 Banco de Dados

Os dados são armazenados localmente em arquivos `.json`:

- `products.json`: informações dos produtos (nome, preço, estoque, validade, etc.)
- `input.json`: registros de entrada
- `output.json`: registros de saída
- `users.json`: usuários cadastrados (simulação)

---

## 🛠 Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/seuprojeto.git
   cd seuprojeto
   ```
3. Execute o sistema:
   ```bash
   python index.py
   ```

---

## 👩‍🏫 Créditos

- **Disciplina:** Laboratório de Engenharia de Software  
- **Curso:** Tecnologia em Análise e Desenvolvimento de Sistemas  
- **Instituição:** FATEC Mococa  
- **Professora:** Jaciara Silva Carosia  
- **Empresa Parceira:** [Elevah Club](https://www.instagram.com/elevah.club/)

---

## 📌 Observações

Este projeto é acadêmico e visa aplicar os conceitos de modularização, persistência de dados e estruturação de software em Python.  
Não se trata de um sistema comercial finalizado.
