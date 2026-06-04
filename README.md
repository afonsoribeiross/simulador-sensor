# Simulador de Sensor Industrial

Script Python que simula um sensor industrial enviando leituras de temperatura automaticamente para o banco de dados do Sistema de Manutenção Industrial.

## Como funciona

A cada 10 segundos, o script gera uma nova leitura de temperatura com incremento aleatório entre 1°C e 3°C e salva na tabela `leituras` do Supabase. O status é definido automaticamente:

- Abaixo de 70°C → normal
- Entre 70°C e 85°C → alerta  
- Acima de 85°C → falha

## Tecnologias

- Python
- Supabase

## Integração

Este simulador alimenta o [Sistema de Manutenção Industrial](https://github.com/afonsoribeiross/sistema-manutencao), que exibe os dados em tempo real com gráficos de tendência e previsão de falha.

## Como rodar

```bash
pip install supabase==2.3.0
python simulador.py
```
