//nodemon app

import express from 'express'
import { TOKEN, tokenAll, urlAll } from './config.js'
import { Telegraf } from 'telegraf'
import { getMainMenu } from './keyboard.js'
import XMLHttpRequest from 'xhr2';
//import { rawString, requestCurl } from './vdsinaMxport';
import { xhrMacloudMxport } from './macloudMxport.js';
import { xhrVdsinaIntercom } from './vdsinaIntercom.js';
import { xhrVdsinaMxport } from './vdsinaMxport.js';
import { balanceOneCloudInrecom } from './oneCloudIntercom.js';
import { balanceOneCloudMxport } from './oneCloudMxport.js';

const app = express()
const bot = new Telegraf(TOKEN)



/*bot.start(ctx => {
	ctx.reply(
		getMainMenu())
})

*/
var balanceMacloudMxport
var balanceVdsinaInercom
var balanceVdsinaMxport



setTimeout(function () {
	balanceMacloudMxport = xhrMacloudMxport.onreadystatechange()
	balanceVdsinaInercom = xhrVdsinaIntercom.onreadystatechange()
	balanceVdsinaMxport = xhrVdsinaMxport.onreadystatechange()
	console.log('vdsina inter ' + balanceVdsinaInercom)
	console.log('vdsina mx ' + balanceVdsinaMxport)
	console.log('macloud mx ' + balanceMacloudMxport)
	console.log('1cloud inter ' + balanceOneCloudInrecom)
	console.log('1cloud mx ' + balanceOneCloudMxport)
}, 6000)
bot.start(ctx => {
	ctx.reply('Welcome, bro', getMainMenu())
})
var balanceTest = xhrMacloudMxport.onreadystatechange();
bot.hears('Проверить баланс', ctx => {

	ctx.reply(
		//balanceTest
		42
	)
})

bot.launch()