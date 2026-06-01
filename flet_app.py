import flet as ft
import requests

API_URL = "http://127.0.0.1:5000/api/notes/"


def main(page: ft.Page):
    page.title = "Minecraft Notes"
    page.bgcolor = "#0b3d0b"
    notes_list = ft.ListView(expand=True, spacing=8)

    def load_notes(e=None):
        notes_list.controls.clear()
        try:
            r = requests.get(API_URL)
            r.raise_for_status()
            for n in r.json():
                notes_list.controls.append(ft.Card(ft.Container(ft.Column([
                    ft.Text(f"{n['id']}: {n['title']}", weight=ft.FontWeight.BOLD),
                    ft.Text(n['content'])
                ]), padding=10)))
        except Exception as ex:
            notes_list.controls.append(ft.Text("Erro ao carregar notas: " + str(ex)))
        page.update()

    title = ft.TextField(label="Título", width=360)
    content = ft.TextField(label="Conteúdo", multiline=True, width=360)
    feedback = ft.Text("", color="#d1fae5")

    def submit(e):
        payload = {"title": title.value, "content": content.value}
        try:
            r = requests.post(API_URL, json=payload)
            if r.status_code == 201:
                feedback.value = "Nota criada com sucesso."
                title.value = ""
                content.value = ""
                load_notes()
            else:
                feedback.value = f"Erro: {r.status_code} {r.text}"
        except Exception as ex:
            feedback.value = "Erro: " + str(ex)
        page.update()

    btn_submit = ft.Button("Criar Nota", bgcolor="#6b8e23", color="white", on_click=submit)
    btn_refresh = ft.Button("Recarregar", bgcolor="#4b8b3b", color="white", on_click=load_notes)
    header = ft.Row([ft.Text("Minecraft Notes", size=24, weight=ft.FontWeight.BOLD, color="#f8fde7")])
    page.add(ft.Column([header, ft.Row([title]), ft.Row([content]), ft.Row([btn_submit, btn_refresh]), feedback, notes_list], spacing=12, alignment=ft.MainAxisAlignment.START))
    load_notes()


if __name__ == "__main__":
    ft.run(main)
