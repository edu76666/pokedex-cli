import requests
import argparse
import pandas as pd

BASE = "https://pokeapi.co/api/v2/"
cache = {}

def buscar_pokemon(session, nome):
    if nome in cache:
        return cache[nome]

    resposta = session.get(f"{BASE}pokemon/{nome}", timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()
    cache[nome] = dados
    return dados

def extrair_tipos(dados):
    return [t["type"]["name"] for t in dados["types"]]

def extrair_ability(dados):
    return [a["ability"]["name"] for a in dados["abilities"]]

def extrair_egggroup(dados_especies):
    return [g["name"] for g in dados_especies["egg_groups"]]

def comparar_pokemon(dados1, dados2):
    stats1 = {s["stat"]["name"]: s["base_stat"] for s in dados1["stats"]}
    stats2 = {s["stat"]["name"]: s["base_stat"] for s in dados2["stats"]}

    nome1 = dados1["name"].capitalize()
    nome2 = dados2["name"].capitalize()

    print(f"\n{'STAT':<20} {nome1:<15} {nome2:<15} {'VENCEDOR'}")
    print("-" * 60)

    for stat in stats1:
        v1 = stats1[stat]
        v2 = stats2[stat]

        if v1 > v2:
            vencedor = nome1
        elif v2 > v1:
            vencedor = nome2
        else:
            vencedor = "Empate"

        print(f"{stat:<20} {v1:<15} {v2:<15} {vencedor}")

def buscar_especies(session, dados):
    url = dados["species"]["url"]
    resposta = session.get(url, timeout=5)
    resposta.raise_for_status()
    return resposta.json()

def exibir_pokemon(dados, dados_especie):

    print()
    print(f"Nome:              {dados['name'].capitalize()}")
    print(f"Tipagem:           {', '.join(extrair_tipos(dados))}")
    print(f"Peso:              {dados['weight'] / 10} kg")
    print(f"Altura:            {dados['height'] / 10} m")
    print(f"Experiência base:  {dados['base_experience']}")
    print(f"Habilidade:        {', '.join(extrair_ability(dados))}")
    print(f"Egg Group:         {', '.join(extrair_egggroup(dados_especie))}")

def exportar_pokemon(session, nomes, arquivo="pokemon.csv"):
    registros = []

    for nome in nomes:
        try:
            dados = buscar_pokemon(session, nome)
            registros.append({
                "nome": dados["name"],
                "tipos": ", ".join(extrair_tipos(dados)),
                "peso_kg": dados["weight"] / 10,
                "altura_m": dados["height"] / 10,
                "experiencia_base": dados["base_experience"],
                "habilidades": ', '.join(extrair_ability(dados)),
                "egg_group": ', '.join(extrair_egggroup(dados))
            })
        except requests.exceptions.HTTPError:
            print(f"Pokémon '{nome}' não encontrado, pulando.")

    df = pd.DataFrame(registros)
    df.to_csv(arquivo, index=False)
    print(f"{len(registros)} Pokémon exportados para {arquivo}")

def main():

    parser = argparse.ArgumentParser(description="Pokédex CLI")
    subparsers = parser.add_subparsers(dest="comando")

    buscar_parser = subparsers.add_parser("buscar")
    buscar_parser.add_argument("nome", type=str)

    comparar_parser = subparsers.add_parser("comparar")
    comparar_parser.add_argument("pokemon1", type=str)
    comparar_parser.add_argument("pokemon2", type=str)

    exportar_parser = subparsers.add_parser("exportar")
    exportar_parser.add_argument("nomes", nargs="+", type=str)

    args = parser.parse_args()

    with requests.Session() as session:
        if args.comando == "buscar":
            try:
                dados = buscar_pokemon(session, args.nome)
                dados_especie = buscar_especies(session, dados)
                exibir_pokemon(dados, dados_especie)
            except requests.exceptions.HTTPError:
                print(f"Pokémon '{args.nome}' não encontrado.")
            except requests.exceptions.RequestException as e:
                print(f"Erro de conexão: {e}")

        elif args.comando == "comparar":
            dados1 = buscar_pokemon(session, args.pokemon1)
            dados2 = buscar_pokemon(session, args.pokemon2)
            comparar_pokemon(dados1, dados2)

        elif args.comando == "exportar":
            exportar_pokemon(session, args.nomes)

        else:
            parser.print_help()

if __name__ == "__main__":
    main()