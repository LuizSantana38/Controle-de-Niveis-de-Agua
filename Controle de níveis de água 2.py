
from colorama import Fore, Style, init

init(autoreset=False)

niveis = [
    (1, "Muito baixo crítico"),
    (2, "Baixo"),
    (3, "Médio"),
    (4, "Alto"),
    (5, "Muito alto alerta")]


def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.CYAN
    elif nivel == 4:
        return Fore.GREEN
    elif nivel == 5:
        return Fore.MAGENTA
    else:
        return Fore.BLACK

print("=== CONTROLE DE NÍVEIS DE ÁGUA ===\n")

for nivel, mensagem in niveis:
    cor = definir_cor(nivel)
    print(cor + f"Nível {nivel}: {mensagem}")

print(Fore.BLACK + Style.NORMAL, end="")    


