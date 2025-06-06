from services.clima import get_weather, get_historical_temperatures

def analisar_alertas(clima):
    alertas = []

    if clima['temperatura'] >= 40 or clima['temperatura'] <= 5:
        alertas.append("Alerta de temperatura crítica!")

    if clima['umidade'] <= 20 or clima['umidade'] >= 95:
        alertas.append("Alerta de umidade crítica!")

    if clima['precipitacao'] >= 80:
        alertas.append("Alerta de risco de enchente!")

    if clima['vento'] >= 70:
        alertas.append("Alerta de ventos fortes!")

    if clima['pressao'] <= 980:
        alertas.append("Alerta de baixa pressão atmosférica!")

    return alertas


def buscar_clima_por_cidade(cidade):
    resultado = get_weather(cidade)

    if "erro" in resultado:
        return {"erro": "Cidade não encontrada."}

    alertas = analisar_alertas(resultado)
    total_alertas = len(alertas)

    alerta_msg = "\n\n".join(alertas) if alertas else "Nenhum alerta detectado."

    if total_alertas > 5:
        mensagem_final = "\n\nRisco Alto de Evento Climático Extremo"
    else:
        mensagem_final = "\n\nClima sob controle"

    matriz, estatisticas = get_historical_temperatures(cidade)
    semana1 = estatisticas[0]
    semana2 = estatisticas[1]

    historico_msg = (
        f"\n\n📅 Temperaturas últimas 2 semanas:\n"
        f"\nSemana 1:\n"
        f"  Máxima: {semana1['maior']}°C\n"
        f"  Mínima: {semana1['menor']}°C\n"
        f"Semana 2:\n"
        f"  Máxima: {semana2['maior']}°C\n"
        f"  Mínima: {semana2['menor']}°C"
    )

    mensagem = (
        f"Clima em {cidade.title()}:\n\n"
        f"Temperatura: {resultado['temperatura']}°C\n"
        f"Umidade: {resultado['umidade']}%\n"
        f"Descrição: {resultado['descricao']}\n"
        f"Vento: {resultado['vento']} km/h\n"
        f"Pressão: {resultado['pressao']} mb\n"
        f"Precipitação: {resultado['precipitacao']} mm\n\n"
        f"{alerta_msg}"
        f"{historico_msg}"
        f"{mensagem_final}"
    )

    return {"mensagem": mensagem}
