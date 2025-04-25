
import flet as ft
from models import buscar_ficha_por_matricula
import os

def main(page: ft.Page):
    page.title = "Minha Ficha de Treino"
    page.scroll = "AUTO"
    page.window_width = 400
    page.window_height = 800
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    matricula_input = ft.TextField(label="Digite sua matrícula", width=300)
    resultado = ft.Column()

    def buscar(e):
        resultado.controls.clear()
        ficha = buscar_ficha_por_matricula(matricula_input.value.strip())

        if not ficha:
            resultado.controls.append(ft.Text("Nenhuma ficha encontrada.", color="red"))
        else:
            resultado.controls.append(
                ft.Text(f"🎯 Objetivo: {ficha['objetivo']}", size=18, weight="bold")
            )
            resultado.controls.append(ft.Text(f"📅 Início: {ficha['data_inicio']}"))
            resultado.controls.append(ft.Text(f"⏳ Validade: {ficha['validade']}"))
            resultado.controls.append(ft.Text(f"📝 Obs: {ficha['observacoes']}"))

            for dia in ficha["dias"]:
                resultado.controls.append(ft.Text(f"\n📆 Dia: {dia['nome_dia']}", size=16, weight="bold"))
                resultado.controls.append(ft.Text(f"Descrição: {dia['descricao']}"))

                for ex in dia["exercicios"]:
                    resultado.controls.append(
                        ft.Text(
                            f"🏋️ {ex['nome']} - {ex['series']}x{ex['repeticoes']} - {ex['carga']}kg"
                        )
                    )
                    if ex["observacoes"]:
                        resultado.controls.append(ft.Text(f"   🔸 {ex['observacoes']}", italic=True))

        page.update()

    page.add(
        ft.Column([
            ft.Text("Acesse sua ficha de treino 💪", size=20, weight="bold"),
            matricula_input,
            ft.ElevatedButton("Ver Ficha", on_click=buscar),
            resultado
        ], horizontal_alignment="center", spacing=20)
    )

# Porta para Render usar
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8550))
    ft.app(target=main, view=ft.WEB_BROWSER, port=port)
