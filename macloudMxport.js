import XMLHttpRequest from 'xhr2';
var url = "https://userapi.macloud.ru/v1/account.balance";

export var xhrMacloudMxport = new XMLHttpRequest();
xhrMacloudMxport.open("GET", url);

xhrMacloudMxport.setRequestHeader("Authorization", "d934b2561c1439c76c7e0e9704163d42eb35bb3420c709d5cff1bcbb15dd8321");

xhrMacloudMxport.onreadystatechange = function () {
	if (xhrMacloudMxport.readyState === 4) {
		var rawString = JSON.parse(xhrMacloudMxport.responseText);
		var dataString = rawString["data"];
		//console.log(dataString["real"]);
		return dataString["real"];
	}
};

xhrMacloudMxport.send();

//console.log(xhr)