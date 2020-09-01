import pyautogui, time, random
import PIL.ImageGrab as ImageGrab
import gc
#from ctypes import windll
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_pixel_color(pic, x, y):
    return pic.load()[x,y]
##def horizontials(x1, y1):
##    y = y1
##    rows_color = []
##    rows_pos = []
##    for i in range(6):
##        x = x1
##        row_color = []
##        row_pos = []
##        if i <= 2:
##            for _ in range(6):
##                row_color.append(pyautogui.pixel(int(x), int(y)))
##                row_pos.append((int(x), int(y)))
##                x += 64 
##        elif i >= 3:
##            for _ in range(2):
##                for z in range(3):
##                    row_color.append(pyautogui.pixel(int(x), int(y)))
##                    row_pos.append((int(x), int(y)))
##                    x += 64
##        y += 64
##        rows_color.append(row_color)
##        rows_pos.append(row_pos)
####    print(rows_pos[len(rows_pos)-1])
####    for i,_ in enumerate(rows_color):
####        print(i, _)
##    windll.user32.ReleaseDC(0, 999999)
##    return rows_color, rows_pos
def horizontials(x1, y1):
    pic = pyautogui.screenshot()
    y = y1
    rows_color = []
    rows_pos = []
    for i in range(6):
        x = x1
        row_color = []
        row_pos = []
        if i is 0:
            for _ in range(6):
                row_color.append(get_pixel_color(pic, int(x), int(y)))
                row_pos.append((int(x), int(y)))
                x += 64
        elif i is 1:
            for _ in range(6):
               row_color.append(get_pixel_color(pic, int(x), int(y)))
               row_pos.append((int(x), int(y)))
               x += 64
        elif i is 2:
            for _ in range(6):
                row_color.append(get_pixel_color(pic, int(x), int(y)))
                row_pos.append((int(x), int(y)))
                x += 64
        elif i is 3:
            for _ in range(6):
                row_color.append(get_pixel_color(pic, int(x), int(y)))
                row_pos.append((int(x), int(y)))
                x += 64
        elif i is 4:
            for _ in range(6):
                row_color.append(get_pixel_color(pic, int(x), int(y)))
                row_pos.append((int(x), int(y)))
                x += 64
        elif i is 5:
            for _ in range(6):
               row_color.append(get_pixel_color(pic, int(x), int(y)))
               row_pos.append((int(x), int(y)))
               x += 64
        y += 64
        rows_color.append(row_color)
        rows_pos.append(row_pos)
##    for i,_ in enumerate(rows_color):
##        print(i, _)
    return rows_color, rows_pos
def sleep():
    time.sleep(random.uniform(0.25, 1))
##def compare_rbgs(rbg1, rbg2):
##    if rbg1[0] is rbg2[0] and rbg1[1] is rbg2[1] and rbg1[2] is rbg2[2]:
##        return True
def compare_rbgs_tolerance(rbg1, rbg2, tolerance = 20):
    if rbg1[0]-tolerance <= rbg2[0] and rbg1[0]+tolerance >= rbg2[0] and rbg1[1]-tolerance <= rbg2[1] and rbg1[1]+tolerance >= rbg2[1] and rbg1[2]-tolerance <= rbg2[2] and rbg1[2]+tolerance >= rbg2[2]:
        return True
def find_same_colors(change_in_colors, change_in_pos, colors, _, i):
    if _ + change_in_colors >= 0 and i + change_in_pos >= 0 and _ + change_in_colors < 6 and i + change_in_pos < 6:
        if compare_rbgs_tolerance(colors[_ + change_in_colors][i + change_in_pos], colors[_][i]):
            return True
def drag(current_pos, wanted_pos):
    pyautogui.moveTo(current_pos, duration = 0.1)
    pyautogui.dragTo(wanted_pos, duration = 0.25)
def do_next_rows(rows_color, rows_pos):
    #rows_color, rows_pos = horizontials()
    for _ in range(len(rows_color)):
        for i in range(len(rows_color[_])-1):
            #print(compare_rbgs(rows_color[_][i], rows_color[_][i + 1]))
            if compare_rbgs_tolerance(rows_color[_][i], rows_color[_][i + 1]):
                #print(rows_pos[_][i], rows_pos[_][i+1])
                #left-left
                if find_same_colors(0, -2, rows_color, _, i):
                    drag(rows_pos[_][i-2], rows_pos[_][i-1])
                    if pyautogui.pixelMatchesColor(int(rows_pos[_][i][0]), int(rows_pos[_][i][1]), rows_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
                #left-up
                elif find_same_colors(-1, -1, rows_color, _, i):
                    drag(rows_pos[_-1][i-1], rows_pos[_][i-1])
                    if pyautogui.pixelMatchesColor(int(rows_pos[_][i][0]), int(rows_pos[_][i][1]), rows_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
                #left-down
                elif find_same_colors(+1, -1, rows_color, _, i):
                    drag(rows_pos[_+1][i-1], rows_pos[_][i-1])
                    if pyautogui.pixelMatchesColor(int(rows_pos[_][i][0]), int(rows_pos[_][i][1]), rows_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
                #right-right-right
                elif find_same_colors(0, +3, rows_color, _, i):
                    drag(rows_pos[_][i+3], rows_pos[_][i+2])
                    if pyautogui.pixelMatchesColor(int(rows_pos[_][i][0]), int(rows_pos[_][i][1]), rows_color[_][i], tolerance = 15) is False:
                        sleep()
                    return True
                #right_right_up
                elif find_same_colors(-1, +2, rows_color, _, i):
                    drag(rows_pos[_-1][i+2], rows_pos[_][i+2])
                    if pyautogui.pixelMatchesColor(int(rows_pos[_][i][0]), int(rows_pos[_][i][1]), rows_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
                #right_right_down
                elif find_same_colors(+1, +2, rows_color, _, i):
                    drag(rows_pos[_+1][i+2], rows_pos[_][i+2])
                    if pyautogui.pixelMatchesColor(int(rows_pos[_][i][0]), int(rows_pos[_][i][1]), rows_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
    return False
def do_next_verticals(verticals_color, verticals_pos):
    #verticals_color, verticals_pos = verticals()
    #print("vertical")
    for _ in range(len(verticals_color)-1):
        for i in range(len(verticals_color[_])):
            #print(compare_rbgs(verticals_color[_][i], verticals_color[_][i + 1]))
            if compare_rbgs_tolerance(verticals_color[_][i], verticals_color[_ + 1][i]):
                #print(verticals_pos[_][i], verticals_pos[_][i+1])
                #up-up
                if find_same_colors(-2, 0, verticals_color, _, i):
                    drag(verticals_pos[_-2][i], verticals_pos[_-1][i])
                    if pyautogui.pixelMatchesColor(int(verticals_pos[_][i][0]), int(verticals_pos[_][i][1]), verticals_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
                #up-left
                elif find_same_colors(-1, -1, verticals_color, _, i):
                    drag(verticals_pos[_-1][i-1], verticals_pos[_-1][i])
                    if pyautogui.pixelMatchesColor(int(verticals_pos[_][i][0]), int(verticals_pos[_][i][1]), verticals_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
                #up-right
                elif find_same_colors(-1, +1, verticals_color, _, i):
                    drag(verticals_pos[_-1][i+1], verticals_pos[_-1][i])
                    if pyautogui.pixelMatchesColor(int(verticals_pos[_][i][0]), int(verticals_pos[_][i][1]), verticals_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
                #down-down-down
                elif find_same_colors(+3, 0, verticals_color, _, i):
                    drag(verticals_pos[_+3][i], verticals_pos[_+2][i])
                    if pyautogui.pixelMatchesColor(int(verticals_pos[_][i][0]), int(verticals_pos[_][i][1]), verticals_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
                #down-down-left
                elif find_same_colors(+2, -1, verticals_color, _, i):
                    drag(verticals_pos[_+2][i-1], verticals_pos[_+2][i])
                    if pyautogui.pixelMatchesColor(int(verticals_pos[_][i][0]), int(verticals_pos[_][i][1]), verticals_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
                #down-down-right
                elif find_same_colors(+2, +1, verticals_color, _, i):
                    drag(verticals_pos[_+2][i+1], verticals_pos[_+2][i])
                    if pyautogui.pixelMatchesColor(int(verticals_pos[_][i][0]), int(verticals_pos[_][i][1]), verticals_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
    return False
def do_skipped_rows(rows_color, rows_pos):
    for _ in range(len(rows_color)):
        for i in range(len(rows_color[_])-2):
            #print(compare_rbgs(rows_color[_][i], rows_color[_][i + 2]))
            if compare_rbgs_tolerance(rows_color[_][i], rows_color[_][i + 2]):
                #up-right
                if find_same_colors(-1, +1, rows_color, _, i):
                    drag(rows_pos[_-1][i+1], rows_pos[_][i+1])
                    if pyautogui.pixelMatchesColor(int(rows_pos[_][i][0]), int(rows_pos[_][i][1]), rows_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
                #down-right
                elif find_same_colors(+1, +1, rows_color, _, i):
                    drag(rows_pos[_+1][i+1], rows_pos[_][i+1])
                    if pyautogui.pixelMatchesColor(int(rows_pos[_][i][0]), int(rows_pos[_][i][1]), rows_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
    return False
def do_skipped_verticals(verticals_color, verticals_pos):
    for _ in range(len(verticals_color)-2):
        for i in range(len(verticals_color[_])):
            if compare_rbgs_tolerance(verticals_color[_][i], verticals_color[_ + 2][i]):
                if find_same_colors(+1, +1, verticals_color, _, i):
                    drag(verticals_pos[_+1][i+1], verticals_pos[_+1][i])
                    time.sleep(0.15)
                    if pyautogui.pixelMatchesColor(int(verticals_pos[_][i][0]), int(verticals_pos[_][i][1]), verticals_color[_][i], tolerance = 15) is False:
                        sleep()
                    return True
                elif find_same_colors(+1, -1, verticals_color, _, i):
                    drag(verticals_pos[_+1][i-1], verticals_pos[_+1][i])
                    time.sleep(0.15)
                    if pyautogui.pixelMatchesColor(int(verticals_pos[_][i][0]), int(verticals_pos[_][i][1]), verticals_color[_][i], tolerance = 15) is False:
                        sleep()
                        return True
    return False
def compare_rbg_to_bomb(rbg1, tolerance = 15):
    if rbg1[0]-tolerance <= 93 and rbg1[0]+tolerance >= 93 and rbg1[1]-tolerance <= 57 and rbg1[1]+tolerance >= 57 and rbg1[2]-tolerance <= 114 and rbg1[2]+tolerance >= 114:
        return True
    elif rbg1[0]-tolerance <= 205 and rbg1[0]+tolerance >= 205 and rbg1[1]-tolerance <= 200 and rbg1[1]+tolerance >= 200 and rbg1[2]-tolerance <= 220 and rbg1[2]+tolerance >= 220:
        return True
    elif rbg1[0]-tolerance <= 171 and rbg1[0]+tolerance >= 171 and rbg1[1]-tolerance <= 115 and rbg1[1]+tolerance >= 115 and rbg1[2]-tolerance <= 191 and rbg1[2]+tolerance >= 191:
        return True
    elif rbg1[0]-tolerance <= 148 and rbg1[0]+tolerance >= 148 and rbg1[1]-tolerance <= 81 and rbg1[1]+tolerance >= 81 and rbg1[2]-tolerance <= 172 and rbg1[2]+tolerance >= 172:
        return True
def bomb(rows_color, rows_pos):
    for _ in range(len(rows_color)):
        for i in range(len(rows_color[_])):
            if compare_rbg_to_bomb(rows_color[_][i], tolerance = 30):
                pyautogui.click(rows_pos[_][i], duration = 0.25)
                if pyautogui.pixelMatchesColor(int(rows_pos[_][i][0]), int(rows_pos[_][i][1]), rows_color[_][i], tolerance = 30) is False:
                    sleep()
                return True
    return False
def Log_in(driver):
    WebDriverWait(driver, 7.5).until(EC.element_to_be_clickable((By.CLASS_NAME, "headerNewLogin"))).click()
    WebDriverWait(driver, 7.5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, """//*[@id="ibox2_content"]/div/iframe""")))
    WebDriverWait(driver, 7.5).until(EC.visibility_of_element_located((By.ID, "loginname"))).send_keys("Username")
    WebDriverWait(driver, 7.5).until(EC.visibility_of_element_located((By.ID, "pwd"))).send_keys("Password")
    WebDriverWait(driver, 7.5).until(EC.element_to_be_clickable((By.ID, "submit"))).click()
    WebDriverWait(driver, 7.5).until_not(EC.frame_to_be_available_and_switch_to_it((By.XPATH, """//*[@id="ibox2_content"]/div/iframe""")))
    driver.switch_to_default_content()

def center_game(driver):
    driver.execute_script("window.scrollTo(25, 430)")

def go_candy_jam(driver):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "games_li_link_div"))).click()
    WebDriverWait(driver, 7.5).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="mainContentDiv"]/div/div/div[4]/div[1]/div[3]/a"""))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "secondaryCurrencyProgressWrapper"))).click()
    center_game(driver)
    WebDriverWait(driver, 7.5).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "game-window")))
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "game")))
    driver.switch_to_default_content()

def go_to_game(driver):
    driver.implicitly_wait(2)
    driver.get("Website")
    driver.set_window_size(673, 728)
    driver.set_window_position(0, 0)
    Log_in(driver)
    go_candy_jam(driver)

def scratch_all_tier_2(driver):
    for _ in range(1,7):
        name = "SC-scratchOffWrapper-" + str(_)
        a = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, name)))
        ActionChains(driver).click(a).perform()

def main(driver):
    gc.enable()
    gc.set_threshold(50, 10, 10)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "secondaryCurrencyProgressWrapper"))).click()
    time.sleep(1.5)
    while True:
        if len(WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "secondaryCurrencyScratchOffWrapper"))).get_attribute("style")) is 14:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "secondaryCurrencyProgressWrapper"))).click()
        center_game(driver)
        if pyautogui.locateCenterOnScreen("top left.png", grayscale = True) != None:
            x1, y1 = pyautogui.locateCenterOnScreen("top left.png", grayscale = True)
            if pyautogui.pixelMatchesColor(int(x1+61), int(y1+63), (43, 234, 246), tolerance = 25):
                pyautogui.click(x1+234, y1+303, duration = 0.15)
            break
        else:
            if pyautogui.locateOnScreen("play button.png") != None:
                pyautogui.click(pyautogui.locateCenterOnScreen("play button.png"), duration = 0.15)
    print((x1, y1))
    side_length = 385
    counter = 0
    counter1 = 0
    counter2 = 0
    timer = time.time()
    timer_stop = timer + random.randint(3600, 4200)
    past_time = time.time()
    while True:
        if time.time() > timer_stop:
            print("Stopped at " + str((timer_stop/60)/60) + " hours")
            return
        center_game(driver)
        try:
            WebDriverWait(driver, 0).until(EC.visibility_of_element_located((By.ID, "error-window")))
            go_candy_jam(driver)
            print("reset")
        except:
            pass
        rows_color, rows_pos = horizontials(x1 + 27, y1 + 29)
        #Use selenium for scratch and win
        if len(WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.ID, "scratchOffWrapperTier-1"))).get_attribute("class")) is 8 and counter1 is 0:
            print(str(int((time.time() - past_time)/60)) + " min" + " - Tier 1")
            center_game(driver)
            counter1 += 1
        if len(WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.ID, "scratchOffWrapperTier-2"))).get_attribute("class")) is 8 and counter2 is 0:
            print(str(int((time.time() - past_time)/60)) + " min" +" - Tier 2")
            center_game(driver)
            #counter2 += 1
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "scratchNowButtonTier-2"))).click()
            scratch_all_tier_2(driver)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "scYouWinEarnMoreButton"))).click()
            counter1 = 0
            past_time = time.time()
        if len(WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.ID, "secondaryCurrencyScratchOffWrapper"))).get_attribute("style")) is 14:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "secondaryCurrencyProgressWrapper"))).click()
        if pyautogui.pixelMatchesColor(int(x1+61), int(y1+63), (43, 234, 246), tolerance = 25):
            pyautogui.click(x1+234, y1+303, duration = 0.15)
        if pyautogui.pixelMatchesColor(int(x1+195), int(y1+189), (255, 151, 7), tolerance = 10):
            pyautogui.click(int(x1+195), int(y1+189), duration = 0.15)
        #print("next_rows")
        if do_next_rows(rows_color, rows_pos) is False:
            #print("next verticals")
            if do_next_verticals(rows_color, rows_pos) is False:
                #print("skipped rows")
                if do_skipped_rows(rows_color, rows_pos) is False:
                    #print("skipped verticals")
                    if do_skipped_verticals(rows_color, rows_pos) is False:
                        if bomb(rows_color, rows_pos) is False:
                            if counter >= 10:
                                print("no solutions")
                                pyautogui.screenshot("ending picture.png")
                                counter = 0
                            else:
                                counter += 1
        else:
            counter = 0
driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path)
go_to_game(driver)
main(driver)
