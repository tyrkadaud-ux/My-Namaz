import flet as ft
import requests

city = "Raduzhny"
url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country=Russia&method=16"
data = requests.get(url).json()
timings = data['data']['timings']

fajr = timings['Fajr'][:5]
dhuhr = timings['Dhuhr'][:5]
asr = timings['Asr'][:5]
maghrib = timings['Maghrib'][:5]
isha = timings['Isha'][:5]

def main(page: ft.Page):
    page.title = "МойНамаз"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    times = ft.Column([
        ft.Text(f"Фаджр    {fajr}", size=18),
        ft.Text(f"Зухр     {dhuhr}", size=18),
        ft.Text(f"Аср      {asr}", size=18),
        ft.Text(f"Магриб   {maghrib}", size=18),
        ft.Text(f"Иша      {isha}", size=18),
    ])

    benefits = ft.Column([
        ft.Text("📿 Дополнительные намазы:", weight=ft.FontWeight.BOLD),
        ft.Text("• Тахаджуд: лучший ночной намаз"),
        ft.Text("• Духа: заменяет 360 милостынь"),
        ft.Text("• 12 суннат: дом в Раю"),
    ])

    page.add(
        ft.Container(
            content=ft.Column([times, ft.Divider(), benefits]),
            padding=20
        )
    )

ft.app(target=main)
