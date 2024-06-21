function printExchangeRates(){
	// var Json = '{"success":true,"timestamp":1669218303,"base":"EUR","date":"2022-11-23","rates":{"EUR":1,"USD":1.037716,"GBP":0.860173,"JPY":145.172309,"CNY":7.438137,"AUD":1.545881,"HKD":8.112929,"IDR":16194.38492,"MXN":20.088001,"SGD":1.431098,"KRW":1393.693444,"THB":37.420139,"TWD":32.294543}}';
	// var Json = '{"success":true,"timestamp":1706389983,"base":"EUR","date":"2024-01-27","rates":{"EUR":1,"USD":1.086361,"GBP":0.854797,"JPY":160.982486,"CNY":7.709476,"AUD":1.652512,"HKD":8.49301,"IDR":17137.620472,"MXN":18.641254,"SGD":1.459205,"KRW":1452.883297,"THB":38.707453,"TWD":33.990184}}'
	// var Json = '{"success":true,"timestamp":1712258287,"base":"EUR","date":"2024-04-04","rates":{"EUR":1,"USD":1.084393,"GBP":0.857603,"JPY":163.974838,"CNY":7.845472,"AUD":1.645339,"HKD":8.489305,"IDR":17231.870307,"MXN":17.969688,"SGD":1.461279,"KRW":1463.073696,"THB":39.802354,"TWD":34.78819}}'
	var Json ='{"success": true,"timestamp": 1718739664,"base": "EUR","date": "2024-06-18","rates":{"USD": 1.073797,"EUR": 1,"CAD": 1.473088,"GBP": 0.844969,"JPY": 169.473,"CNY": 7.78997,"AUD": 1.61364,"HKD": 8.383077,"IDR": 17576.279831,"MXN": 19.773102,"SGD": 1.450876,"KRW": 1482.156173,"THB": 39.36572,"TWD": 34.745887}}'
	var obj = JSON.parse(Json);
	var breakLine = "<br />";
	
	document.write("<hr>");
	
	//document.write(json + breakLine);
	// Printing a single value

	document.writeln("<table>");
	document.writeln("<tr>");
	document.writeln("<th>Time taken</th>");
	document.writeln("<th>" + obj["date"] + "</th>");
	document.writeln("</tr>");

	//for (country in obj["rates"]){
	//	document.write(symbol2country(country) + ': \u0009' + obj["rates"][country] + breakLine);
	//}

	for (country in obj["rates"]) {
		document.writeln("<tr>");
		document.writeln("<td>" + symbol2country(country) + "</td>");
		document.writeln("<td>" + obj["rates"][country] / obj["rates"]["USD"] + "</td>" );
		document.writeln("</tr>");
	}

	document.writeln("</table>");
	// document.write(symbol2country('CNY') + ': \t' + obj["rates"]["CNY"] + breakLine); // single rate
}
	
function symbol2country(symbol){
	var SC = '{"CAD":"CANADIAN DOLLAR","GBP": "BRITISH POUND","EUR": "EURO", "JPY": "JAPANESE YEN","CNY": "CHINESE YUAN","AUD": "AUSTRALIAN DOLLAR", "HKD": "HONG KONG DOLLAR","IDR": "INDONESIAN RUPIAH","MXN": "MEXICAN PESO","SGD": "SINGAPORE DOLLAR","KRW": "SOUTH KOREAN WON","THB": "THAI BAHT","TWD": "NEW TAIWAN DOLLAR","USD": "US DOLLAR"}'
	var oSC = JSON.parse(SC);
	
	return oSC[symbol];
}