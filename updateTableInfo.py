import cmdTable
import cmdCurl
import config

def updateTableInfo():
	 
	balanceMacloudHelp = cmdCurl.getBalance(
    config.urlMacloud, config.tokenMacloudHelp)
	balanceMacloudIntercom = cmdCurl.getBalance(
    config.urlMacloud, config.tokenMacloudIntercom)
	balanceMacloudMxport = cmdCurl.getBalance(
    config.urlMacloud, config.tokenMacloudMxport)
	balanceVdsinaMxport = cmdCurl.getBalance(
    config.urlVdsina, config.tokenVdsinaMxport)
	balanceVdsinaIntercom = cmdCurl.getBalance(
    config.urlVdsina, config.tokenVdsinaIntercom)
	balance1cloudInrecom = cmdCurl.getBalance(
    config.url1cloud, config.token1cloudInrecom, 1)
	balance1cloudMxport = cmdCurl.getBalance(
    config.url1cloud, config.token1cloudMxport, 1)

	cmdTable.updateTableInfo('Vdsina Intercom', balanceVdsinaIntercom)
	cmdTable.updateTableInfo('Vdsina Mxport', balanceVdsinaMxport)
	cmdTable.updateTableInfo('Macloud Intercom', balanceMacloudIntercom)
	cmdTable.updateTableInfo('Macloud Mxport', balanceMacloudMxport)
	cmdTable.updateTableInfo('Macloud Help', balanceMacloudHelp)
	cmdTable.updateTableInfo('1cloud Inrecom', balance1cloudInrecom)
	cmdTable.updateTableInfo('1cloud Mxport', balance1cloudMxport)

	textMacloudHelp = 'Macloud Help: ' + str(balanceMacloudHelp)
	textMacloudIntercom = 'Macloud Intercom: ' + str(balanceMacloudIntercom)
	textMacloudMxport = 'Macloud Mxport: ' + str(balanceMacloudMxport)
	textVdsinaMxport = 'Vdsina Mxport: ' + str(balanceVdsinaMxport)
	textVdsinaIntercom = 'Vdsina Intercom: ' + str(balanceVdsinaIntercom)
	text1cloudInrecom = '1cloud Inrecom: ' + str(balance1cloudInrecom)
	text1cloudMxport = '1cloud Mxport: ' + str(balance1cloudMxport)

	balanceNow = f'''{textVdsinaIntercom}
		{textVdsinaMxport}
		{textMacloudIntercom}
		{textMacloudMxport}
		{textMacloudHelp}
		{text1cloudInrecom}
		{text1cloudMxport}
		'''
	return balanceNow