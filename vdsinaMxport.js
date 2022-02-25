import XMLHttpRequest from 'xhr2';
var url = "https://userapi.vdsina.ru/v1/account.balance";

export var xhrVdsinaMxport = new XMLHttpRequest();
xhrVdsinaMxport.open("GET", url);

xhrVdsinaMxport.setRequestHeader("Authorization", "7ec0d1a7acc907bc20a0ea7f31916c9ac60e25fb49c531cd87522817a526f892");

xhrVdsinaMxport.onreadystatechange = function () {
	if (xhrVdsinaMxport.readyState === 4) {
		var rawString = JSON.parse(xhrVdsinaMxport.responseText);
		var dataString = rawString["data"];
		//console.log(dataString["real"]);
		return dataString["real"];
	}
};

xhrVdsinaMxport.send();
