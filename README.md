# Pokédex CLI

CLI em Python para buscar, comparar e exportar dados de Pokémon usando a PokéAPI.

## Como executar

```bash
git clone https://github.com/edu76666/pokedex-cli
cd pokedex-cli
pip install -r requirements.txt
python main.py --help
```

## Comandos

### Buscar um Pokémon

```bash
python main.py buscar pikachu
```

```Nome:              Pikachu
Tipagem:           electric
Peso:              6.0 kg
Altura:            0.4 m
Experiência base:  112
Habilidade:        static, lightning-rod
Egg Group:         ground, fairy
```

### Comparar dois Pokémon

```bash
python main.py comparar pikachu charizard
```

```
STAT                 Pikachu         Charizard       VENCEDOR
------------------------------------------------------------
hp                   35              78              Charizard
attack               55              84              Charizard
defense              40              78              Charizard
special-attack       50              109             Charizard
special-defense      50              85              Charizard
speed                90              100             Charizard
```

### Exportar para CSV

```bash
python main.py exportar pikachu charizard mewtwo
```

Gera pokemon.csv com nome, tipos, peso, altura, experiência base, habilidades e egg group.

```
3 Pokémon exportados para pokemon.csv
```

## Tecnologias
- Python 3.14
- Requests
- Pandas

## Autor
Eduardo Cruz Junior — [LinkedIn](https://linkedin.com/in/educruzjr) · [GitHub](https://github.com/edu76666)
