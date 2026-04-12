from selenium.webdriver.common.action_chains import ActionChains# # читаем диапазон

# min_v = float(volume_slider.get_attribute("min") or 0)
# max_v = float(volume_slider.get_attribute("max") or 100)
# target = 100.0   # нужное значение
#
# # ширина слайдера в пикселях
# width = volume_slider.size['width']
#
# # смещение от левого края в пикселях для target
# pos_px = width * (target - min_v) / (max_v - min_v)
#
# # ActionChains обычно кликает в центр элемента, поэтому корректируем:
# center = width / 2.0
# # хотим перейти в абсолютную позицию pos_px относительно левого края,
# # при клике в центре нужно смещение = pos_px - center
# offset = int(pos_px - center)
#
# ActionChains(driver).click_and_hold(volume_slider).move_by_offset(offset, 0).release().perform()