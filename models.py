def buscar_ficha_por_matricula(matricula):
    if matricula == "123":
        return {
            "objetivo": "Hipertrofia",
            "validade": "30/06/2025",
            "observacoes": "Evitar exercícios de impacto.",
            "treino": {
                "Segunda-feira": [
                    {"nome": "Supino reto", "carga": 40, "series": 3, "repeticoes": 10, "observacoes": ""},
                    {"nome": "Crucifixo", "carga": 12, "series": 3, "repeticoes": 12, "observacoes": "devagar"}
                ],
                "Quarta-feira": [
                    {"nome": "Agachamento livre", "carga": 60, "series": 4, "repeticoes": 8, "observacoes": "com pausa"},
                ]
            }
        }
    return None