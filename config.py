bot_token = "7267991462:AAFfirxSE_zeijvYHYOH-mF9Xq3GOdUhNNQ"
y_token = ""
card = ""
support = "7123901080"
support_id = ID # id support

# ~~CLIENT TEXT~~

main_menu_text = "👋🏻 Добро пожаловать, {name}!\n🧨 ты есть ты🥰!"
# NAME - для замены

profile_text = """👤 Профиль

🔮 Имя: {first_name}
⚙️ ID: {user_id}
🔱 Username: @{username}
📌 Дата регистрации: {reg_date}
💳 Количество покупок: {count}
"""

order_capt = """⛓ Ожидаю платеж... (кнопка действительна 15 минут)

💸 Сумма: {price}
🛍 Товар(ы): {items}
⚙️ Айди заказа: <code>{payment_id}</code>"""

buy_menu_text = "🛍 Введите ID товаров через пробел, например: 1 5 (товар товар)\n(для отмены введите 0)\n\n\n🔒 Покупая товар, вы автоматически соглашаетесь с правилами магазина (ознакомиться с ними можно в главном меню)."
calc_menu_text = "Для рассчета отправьте ID товаров через пробел с командой !calc, например: !calc 1 5"
address_menu_text = "🌠 Введите адрес для доставки"
order_capt_1 = "⛔️Заказы можно делать раз в 2 минуты!"
order_capt_2 = "📵Неверный формат ввода или товара нет в наличии!\n(за 1 раз можно купить не более 5 товаров)"
paid_text = "✅оплачено, с вами свяжется администратор (@{support}) в течении дня."
rules = """🔒 Правила
...
❗️ Напоминаем, что незнание правил не освобождает вас от ответственности.
❗️ Покупая товар, вы автоматически соглашаетесь с правилами магазина.
"""

# ~~ADMIN TEXT~~
adm_menu_text = "⚡️ADMIN PANEL"
canceled_action = "❌ Действие отменено"
success_ban = "🔱 Вы успешно забанили {user}"
success_pardon = "🔱 Вы успешно разбанили {user}!"
error_text = "❌ Ошибка"
sender_started = "✅ Рассылка началась!"
sender_ended = "🔱 Рассылка завершена!\n📤 Отправлено {success_sent} сообщений!"
notification = "Новый пользователь -> @{username}"
new_order_capt = """ℹ️ Новый заказ!

👤 Покупатель: @{username}
💸 Сумма: {price}
🛍 Товары: {items}
-> {processed_items}
🏠 Адрес: {address}
⚙️ Айди заказа: {payment_id}
🕰 Время заказа: {purchase_date}"""
