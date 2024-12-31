#!/usr/bin/env python3

# Aviso de Uso Responsável:
# Este script é destinado apenas para fins educacionais e para
# testar redes para as quais você tem permissão de acesso.
# O uso indevido deste script pode ser ilegal e resultará em
# consequências legais. O autor não se responsabiliza por qualquer
# dano ou uso indevido do código.

import socket
import ipaddress
import concurrent.futures

# Função para verificar a porta de um IP
def verificar_ip(ip, porta=80):
    try:
        # Cria o socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Timeout curto
        resultado = sock.connect_ex((str(ip), porta))  # Verifica a porta
        sock.close()
        if resultado == 0:
            return f"[ATIVO] Dispositivo encontrado: {ip} na porta {porta}"
        else:
            return None
    except socket.error as e:
        return None

# Função para varrer a rede
def varrer_rede(rede, portas=[80]):
    print(f"\nIniciando varredura na rede: {rede}")
    try:
        # Cria um objeto de rede para iterar sobre os IPs
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            # Cria as tarefas para cada IP
            tarefas = []
            for ip in ipaddress.IPv4Network(rede, strict=False):
                for porta in portas:
                    tarefas.append(executor.submit(verificar_ip, ip, porta))
            
            # Processa os resultados
            for tarefa in concurrent.futures.as_completed(tarefas):
                resultado = tarefa.result()
                if resultado:
                    print(resultado)

    except ValueError as ve:
        print(f"Erro: {ve}")

# Solicitar a rede do usuário
if __name__ == "__main__":
    rede = input("Digite a rede no formato CIDR (ex: 192.168.0.0/24): ")
    portas_input = input("Digite as portas (separadas por vírgula, ex: 80,22): ")
    portas = [int(p.strip()) for p in portas_input.split(",")]
    varrer_rede(rede, portas)

