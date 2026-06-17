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

### Comparar dois Pokémon
```bash
python main.py comparar pikachu charizard
```

### Exportar para CSV
```bash
python main.py exportar pikachu charizard mewtwo
```
Gera `pokemon.csv` com nome, tipos, peso, altura e experiência base.

## Tecnologias
- Python 3.14
- Requests
- Pandas

## Autor
Eduardo Cruz Junior — [LinkedIn](https://linkedin.com/in/educruzjr) · [GitHub](https://github.com/edu76666)
