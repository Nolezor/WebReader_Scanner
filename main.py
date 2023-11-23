import numpy as np
import cv2
import pyautogui
import time
import img2pdf

from pynput.mouse import Button, Controller


start_page, end_page = 343, 424  # Edit based on the pages you need
left, top = 991, 392  # x, y coordinates of the page
width, height = 999 + left, 1408 + top  # x, y coordinates of the page
next_button_x, next_button_y = 1412, 540  # x, y coordinates of the next page button
timer = 3  # timer between screenshots -> add more if the pages need more time to lead


def click() -> None:
    pyautogui.moveTo(next_button_x, next_button_y)
    Controller().click(Button.left)


def get_image(file_name: str) -> None:
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)
    cv2.imwrite(file_name, image)


def get_all():
    time.sleep(5)

    for i in range(start_page, end_page+1):
        img_name = f"./temp/img_{i}.jpg"
        get_image(img_name)
        click()
        print(i)
        time.sleep(timer)


def crop_images():
    for i in range(start_page, end_page+1):
        img_name = f"./temp/img_{i}.jpg"
        new_name = f"./cropped/img_{i}.jpg"
        image = cv2.imread(img_name)
        cropped_image = image[top:height, left:width]
        cv2.imwrite(new_name, cropped_image)


def make_pdf():
    with open("Calcolo delle Probabilità.pdf", "wb") as f:
        f.write(img2pdf.convert([f'./cropped/img_{x}.jpg' for x in range(start_page, end_page+1)]))


if __name__ == '__main__':
    get_all()
    crop_images()
    make_pdf()
