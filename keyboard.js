import { Markup } from "telegraf"

export function getMainMenu() {
	return Markup.keyboard([
		['Проверить баланс']
	]).resize()
}

export function yesNoKeyboard() {
	return Markup.inlineKeyboard([
		Markup.button.callback('Да', 'yes'),
		Markup.button.callback('Нет', 'no')])
}