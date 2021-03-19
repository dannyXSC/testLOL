from selenium import webdriver
from bs4 import BeautifulSoup

try:
    driver = webdriver.Chrome()
    driver.get("https://lol.qq.com/tft/#/championDetail/1")

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    HeroName = soup.find(class_="page-title").text.splitlines()[1].split()
    SkillName = soup.find(class_="skill-name").text.strip()
    Cost = int(soup.find(class_="detail-price").text.strip()[0])
    Skill_Desc = soup.find(class_="skill-desc").text.strip()
    Detail_Info_Desc = soup.find(
        class_="detail-info-desc").text.strip().replace(" ", "").splitlines()
    Races = soup.find(class_="detail-info-3").find_all(class_="detail-box")
    HeroRace = {}
    for race in Races:
        thisName = race.find(class_="detail-info-title").text.strip()
        thisDesc = race.find(class_="desc-txt").text.strip()

        thisLevel = {}
        thisLevels = race.find_all("desc-txt-level")
        print(thisLevels)
        print()
        for item in thisLevels:
            print(item)

finally:
    driver.close()
