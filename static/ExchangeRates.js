function getExchangeRates(){
	fetch("./CurrentExchangeRates.json")
		.then((response) => response.json())
		.then((json) => rate = json.parse(json)
		
		// {

			// // var Json = '{....}'
			// // var obj = JSON.parse(Json)

			// return JSON.parse(Json)
		// } )
		// .catch((e) => console.error(e))

	// var Json ='{"success": true,"timestamp": 1718739664,"base": "EUR","date": "2024-06-18","rates":{"USD": 1.073797,"EUR": 1}}'

	return rate
}

function printExchangeRates(){
	
	var obj = getExchangeRates();

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