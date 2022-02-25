import XMLHttpRequest from 'xhr2';
var url = "https://userapi.vdsina.ru/v1/account.balance";

export var xhrVdsinaIntercom = new XMLHttpRequest();
xhrVdsinaIntercom.open("GET", url);

xhrVdsinaIntercom.setRequestHeader("Authorization", "014970af9fa604b80732eeff115c33338825ea71f229538fe16a112b672822f5");

xhrVdsinaIntercom.onreadystatechange = function () {
	if (xhrVdsinaIntercom.readyState === 4) {
		var rawString = JSON.parse(xhrVdsinaIntercom.responseText);
		var dataString = rawString["data"];
		//.log(dataString["real"]);
		return dataString["real"];
	}
};

xhrVdsinaIntercom.send();
