"""
File: webcrawler.py
Name: Stephanie
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def main():

    for year in ['2010s', '2000s', '1990s']:

        print('---------------------------')
        print(year)

        driver = webdriver.Chrome()
        driver.get('https://www.ssa.gov/oact/babynames/decades/names' + year + '.html')
        # driver.get('https://www.ssa.gov/oact/babynames/decades/' + year + '.html') # 更新網址
        # try:
        #     element_present = EC.presence_of_element_located((By.ID, 'specific-element-id'))
        #     WebDriverWait(driver, 5).until(element_present)
        # except TimeoutException:
        #     print("Timed out waiting for page to load")

        # Get the entire HTML content of the page
        html = driver.page_source
        soup = BeautifulSoup(html)

        tags = soup.find_all('table', {'class': 't-stripe'})
        # print(type(tags))
        men_total, women_total = 0, 0
        count = 0
        l_men = []
        l_women = []
        for tag in tags:
            # print(type(tag))
            # print(tag.text)
            tokens = tag.text.split()
            # print(tokens)

            # 去除數字中的逗號, 不用index處理較好; 因為數字串中有',', 所以可以用token中有','
        for token in tokens:
            if ',' in token:
                num_ppl = token
                # print(num_ppl)
                ans = ''
                for ch in token:
                    if ch != ',':
                        ans += ch
                # print(ans)
                count += 1

                if count % 2 == 0:
                    l_women.append(ans)
                    women_total += int(ans)
                else:
                    l_men.append(ans)
                    men_total += int(ans)

        # print('Men List: '+str(l_men))
        # print('Women List: '+str(l_women))
        print('Men Total:', men_total)
        print('Women Total: ', women_total)
        print('Count:', count)
        # ----- Write your code below this line ----- #
        pass

        driver.quit()


if __name__ == '__main__':
    main()
