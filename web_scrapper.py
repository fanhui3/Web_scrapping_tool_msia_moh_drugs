import pyautogui as pg
import webbrowser
import time

# INGREDIENTS = ["paracetamol"]


def go_to_site(browser_location: str) -> None:
    """This function open up the stockrow financial page in annual format

    Args:
        stock (_str_): ticker symbol listed on thy nyse or nasdaq
        browser_location (_str_): location where you keep your brower exe
    """
    URL = f"https://quest3plus.bpfk.gov.my/pmo2/index.php"
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(browser_location))
    webbrowser.get("chrome").open(URL)


def click_on_object(location):
    if location:
        pg.moveTo(location, duration=0.5)
        pg.leftClick()
        time.sleep(1)
    else:
        pass


def export_table(ingredient: str):
    """this scripts will find the table on the site and proceed to click export

    Args:
        table (_str_): the button name in your screenshot folder without hte png extension
    """
    # click search by
    time.sleep(2)
    coordinates = pg.locateCenterOnScreen("./Screenshots/search_by.png", confidence=0.7)
    click_on_object(coordinates)

    # click active active ingredients
    coordinates = pg.locateCenterOnScreen(
        "./Screenshots/active_ingredients.png", confidence=0.7
    )
    click_on_object(coordinates)

    # click on search bar
    coordinates = pg.locateCenterOnScreen(
        "./Screenshots/search_bar.png", confidence=0.7
    )
    click_on_object(coordinates)

    # type in ingredient
    pg.write(ingredient)

    # click on search button
    coordinates = pg.locateCenterOnScreen(
        "./Screenshots/search_button.png", confidence=0.7
    )
    click_on_object(coordinates)

    # scrool down and wait for page to load
    time.sleep(7)
    pg.scroll(-200)
    time.sleep(1)

    # click on csv_button
    coordinates = pg.locateCenterOnScreen(
        "./Screenshots/csv_button.png", confidence=0.7
    )
    click_on_object(coordinates)

    # hit refresh for next search
    pg.press("f5")

    # scroll back up
    time.sleep(1)
    pg.scroll(200)


def get_csv(ingredient):
    brower_path = open("browser_location.txt", "r").readline()
    go_to_site(brower_path)
    export_table(ingredient)


# if __name__ == "__main__":
#     for ingredient in INGREDIENTS:
#         get_csv(ingredient)
