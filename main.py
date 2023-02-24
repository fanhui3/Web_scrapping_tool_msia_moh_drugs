from web_scrapper import go_to_site, export_table
from download_manager import move_csv
from request_generator import get_ingredient_list

INGREDIENTS = get_ingredient_list()

brower_path = open("browser_location.txt", "r").readline()
go_to_site(brower_path)

for ingredient in INGREDIENTS:
    export_table(ingredient)
    move_csv(ingredient)
