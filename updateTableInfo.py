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

    cmdTable.updateTableInfo('Vdsina Intercom', balanceVdsinaIntercom)
    cmdTable.updateTableInfo('Vdsina Mxport', balanceVdsinaMxport)
    cmdTable.updateTableInfo('Macloud Intercom', balanceMacloudIntercom)
    cmdTable.updateTableInfo('Macloud Mxport', balanceMacloudMxport)
    cmdTable.updateTableInfo('Macloud Help', balanceMacloudHelp)

    textMacloudHelp = 'Macloud Help: ' + str(balanceMacloudHelp)
    textMacloudIntercom = 'Macloud Intercom: ' + str(balanceMacloudIntercom)
    textMacloudMxport = 'Macloud Mxport: ' + str(balanceMacloudMxport)
    textVdsinaMxport = 'Vdsina Mxport: ' + str(balanceVdsinaMxport)
    textVdsinaIntercom = 'Vdsina Intercom: ' + str(balanceVdsinaIntercom)
    balanceNow = f'''
{textVdsinaIntercom}
{textVdsinaMxport}
{textMacloudIntercom}
{textMacloudMxport}
{textMacloudHelp}
		'''
    return balanceNow
