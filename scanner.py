#!/usr/bin/env python3

# Aviso de Uso Responsável:
# Este script é destinado apenas para fins educacionais e para
# testar redes para as quais você tem permissão de acesso.
# O uso indevido deste script pode ser ilegal e resultará em
# consequências legais. O autor não se responsabiliza por qualquer
# dano ou uso indevido do código.

import socket
import ipaddress

def varrer_rede(rede):
    print(f"\nIniciando varredura na rede: {rede}")
    try:
        # Cria um objeto de rede para iterar sobre os IPs
        for ip in ipaddress.IPv4Network(rede, strict=False):
            try:
                # Tenta se conectar ao IP na porta 80 (padrão para HTTP)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)  # Timeout curto para rapidez
                resultado = sock.connect_ex((str(ip), 80))  # Porta 80
                if resultado == 0:
                    print(f"[ATIVO] Dispositivo encontrado: {ip}")
                sock.close()
            except Exception as e:
                pass
    except ValueError as ve:
        print(f"Erro: {ve}")

# Solicitar a rede do usuário
if __name__ == "__main__":
    rede = input("Digite a rede no formato CIDR (ex: 192.168.0.0/24): ")
    varrer_rede(rede)
