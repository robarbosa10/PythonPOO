# 🐍 Python: Programação Orientada a Objetos

Meus estudos de POO em Python. Aqui ficam as aulas, os exercícios e os desafios que fui fazendo, na ordem em que apareceram: classes e objetos primeiro, depois atributos e métodos, encapsulamento, herança, modularização e abstração.

Cada conceito virou um exercício pequeno e executável. Guardo o repositório para revisar depois, então o código está como foi escrito durante o estudo.

## 📌 O que está aqui

* Classes, objetos, `self` e `__init__`
* Métodos e atributos especiais (dunder)
* Encapsulamento e regras de negócio
* Herança, superclasse, subclasse e `super()`
* Modularização e `__main__`
* Abstração, interface pública e classes abstratas (`ABC`, `@abstractmethod`)
* Princípio DRY (*Don't Repeat Yourself*)

A ideia que liga tudo: um objeto junta dados e comportamento. Saí de variáveis soltas, listas e dicionários e fui para estruturas que carregam as duas coisas.

---

## 📂 Estrutura do projeto

```text
📦 pythonProject
│
├── 📚 Aula04_ex001/
│
├── 📚 Aula05_ex001/
│
├── 🧬 Aula07_Heranca/
│   ├── 👥 ex001_Clientes/
│   ├── 👨‍💻 ex002_Funcionario/
│   ├── 📦 ex003_Produtos/
│   └── ⚽ exFutebol/
│
├── 🧩 Aula08_Abstracao/
│
├── 🚀 Desafios/
│   ├── 📝 ex016_a_022/
│   ├── 🔷 ex023_Poligono/
│   ├── ☕ ex024_Cafeteira/
│   ├── 🚚 ex025_CalcularFrete/
│   ├── 💰 ex026_CalcularSalario/
│   └── 🎮 ex027_RPG/
│
├── 🏎️ exerciciosExtras/
│
├── 📄 .gitignore
└── 📖 README.md
```

`__pycache__`, arquivos `.pyc` e o `.venv` ficam de fora porque não são conteúdo de estudo.

---

## 📚 Aulas

### Aula 04: Classes e objetos

A classe é o molde e o objeto é uma instância criada a partir dele.

```python
class Pessoa:
    pass

pessoa = Pessoa()
```

Exercício: [`Aula04_ex001/ex001.py`](./Aula04_ex001/ex001.py)

### Aula 05: Atributos e métodos

Aqui os objetos passam a guardar informação e a executar ações. O `__init__` roda na criação do objeto e normalmente inicializa os atributos.

* [`ex001.py`](./Aula05_ex001/ex001.py)
* [`ex002_banco.py`](./Aula05_ex001/ex002_banco.py): depositar e sacar, com validações no próprio objeto.

### Aula 06: Métodos especiais

Estudei `__init__`, `__str__`, `__doc__`, `__dict__`, `__getstate__` e `__class__`. São os "dunder", por causa dos dois sublinhados.

Também vi como concentrar as regras de negócio dentro do objeto, em vez de deixar qualquer código de fora mexer nos atributos.

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome
```

Essa aula não tem pasta própria no repositório.

### Aula 07: Herança e modularização

A herança é uma relação "é um": `Aluno` é uma `Pessoa`. A subclasse reaproveita o que a superclasse já tem, e `super()` chama o construtor da classe mãe.

```python
class Aluno(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self.curso = curso
```

Nesta aula também separei as classes em arquivos diferentes, com um `__main__.py` para executar o programa.

* Clientes: [`ex001_Clientes`](./Aula07_Heranca/ex001_Clientes/)
* Funcionários: [`ex002_Funcionario`](./Aula07_Heranca/ex002_Funcionario/)
* Produtos: [`ex003_Produtos`](./Aula07_Heranca/ex003_Produtos/)
* Futebol: [`exFutebol`](./Aula07_Heranca/exFutebol/)

### Aula 08: Abstração

Abstrair é esconder o que não precisa aparecer. Quem usa o objeto precisa saber o que ele faz, não como.

Um controle remoto é o exemplo clássico: você aperta "ligar" sem saber nada do circuito.

Arquivos: [`Aula08_Abstracao`](./Aula08_Abstracao/)

### Aula 09: Classes abstratas

Continuação da abstração, agora com o módulo `abc`.

Uma classe abstrata serve de modelo para as subclasses e não pode ser instanciada. Um método abstrato é uma obrigação: toda subclasse concreta tem que implementar.

Um método concreto pode ter implementação compartilhada, o que evita repetição (DRY).

```python
from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def estudar(self):
        pass
```

Também não tem pasta própria. Os exemplos estão nos desafios 23 e 24.

---

## 🚀 Desafios

Exercícios para aplicar o que foi visto.

Pasta: [`Desafios`](./Desafios/)

### 16 a 20

| Desafio | Arquivo                                                               | Foco                               |
| ------- | --------------------------------------------------------------------- | ---------------------------------- |
| 16      | [`ex016_Funcionario.py`](./Desafios/ex016_a_022/ex016_Funcionario.py) | Atributos de instância e de classe |
| 17      | [`ex017_Produtos.py`](./Desafios/ex016_a_022/ex017_Produtos.py)       | Formatação e métodos               |
| 18      | [`ex018_Churrasco.py`](./Desafios/ex016_a_022/ex018_Churrasco.py)     | Cálculos em métodos                |
| 19      | [`ex019_Livros.py`](./Desafios/ex016_a_022/ex019_Livros.py)           | Controle de estado                 |
| 20      | [`ex020_Gamer.py`](./Desafios/ex016_a_022/ex020_Gamer.py)             | Atributos com listas               |

### 23: Polígonos

[`ex023_Poligono`](./Desafios/ex023_Poligono/): uma superclasse abstrata `Poligono`, com subclasses que implementam o cálculo de perímetro e de área.

### 24: Cafeteira

[`ex024_Cafeteira`](./Desafios/ex024_Cafeteira/): `BebidaQuente` define o comportamento geral e cada bebida implementa o seu preparo.

### 25: Cálculo de frete

[`ex025_CalcularFrete`](./Desafios/ex025_CalcularFrete/): tipos de transporte diferentes, cada um com suas regras e validações.

### 26: Cálculo de salário

[`ex026_CalcularSalario`](./Desafios/ex026_CalcularSalario/): formas diferentes de calcular o salário de funcionários, usando herança.

### 27: Batalha de RPG

[`ex027_RPG`](./Desafios/ex027_RPG/): objetos que interagem. O método `atacar(alvo)` recebe outro objeto e reduz os pontos de vida dele.

---

## 🏎️ Exercícios extras (Fórmula 1)

Pasta: [`exerciciosExtras`](./exerciciosExtras/)

| Arquivo                                                                             | Tema                        |
| ----------------------------------------------------------------------------------- | --------------------------- |
| [`ex001CadastroPiloto.py`](./exerciciosExtras/ex001CadastroPiloto.py)               | Cadastro de piloto          |
| [`ex002velocidadeMedia.py`](./exerciciosExtras/ex002velocidadeMedia.py)             | Velocidade média            |
| [`ex003conversorDeTempoVolta.py`](./exerciciosExtras/ex003conversorDeTempoVolta.py) | Conversão de tempo de volta |
| [`ex004mediaPitStop.py`](./exerciciosExtras/ex004mediaPitStop.py)                   | Média de pit stops          |
| [`exercicios.docx`](./exerciciosExtras/exercicios.docx)                             | Enunciados                  |

---

## ▶️ Como executar

Precisa de Python instalado.

Para um arquivo solto:

```bash
python Aula04_ex001/ex001.py
```

Nas pastas com vários arquivos, o ponto de entrada é o `__main__.py`:

```bash
python Aula07_Heranca/ex001_Clientes/__main__.py
```

Se der erro de import ao rodar assim, tente como módulo, a partir da pasta pai:

```bash
python -m Aula07_Heranca.ex001_Clientes
```

---

## 👤 Autor

**Rogerio Barbosa**

Estudando Python, POO e desenvolvimento de software.
