import flet as ft
import os
from models import buscar_ficha_por_matricula

def main(page: ft.Page):
    page.title = "Ficha de Treino"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    matricula_input = ft.TextField(label="Digite sua matrícula", width=300)
    resultado = ft.Column()

    def buscar_ficha(e):
        resultado.controls.clear()
        ficha = buscar_ficha_por_matricula(matricula_input.value.strip())
        if ficha:
            resultado.controls.append(ft.Text(f"Objetivo: {ficha['objetivo']}", size=18, weight="bold"))
            resultado.controls.append(ft.Text(f"Validade: {ficha['validade']}"))
            resultado.controls.append(ft.Text(f"Observações: {ficha['observacoes']}"))
            for dia, exercicios in ficha["treino"].items():
                resultado.controls.append(ft.Text(f"\n📅 {dia}", size=16, weight="w600"))
                for ex in exercicios:
                    resultado.controls.append(ft.Text(f"- {ex['nome']} | {ex['series']}x{ex['repeticoes']} | {ex['carga']}kg ({ex['observacoes']})"))
        else:
            resultado.controls.append(ft.Text("Matrícula não encontrada.", color="red"))

        page.update()

    page.add(
        ft.Column([
            matricula_input,
            ft.ElevatedButton("Buscar Ficha", on_click=buscar_ficha),
            resultado
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8550))
    ft.app(target=main, view=ft.WEB_BROWSER, port=port)