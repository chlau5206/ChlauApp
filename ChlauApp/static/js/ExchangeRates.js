// ExchangeRates.js 
function getExchangeRates() {
	fetch("/static/data/LatestRate.json")
		.then((response) => response.json())
		.then(data => {
			//console.log('Fetched data:', data); // Log the fetched data
			//console.log('Data type:', typeof data); // Log the type of the data
			if (typeof data === 'object' && !Array.isArray(data.rates)) {
				populateTable(data.rates);
				console.log("Data populated.")
			} else {
				console.error('Error: Fetched data is not an object');
			}
		})
		.catch(error => console.error('Error fetching data:', error));
}
function populateTable(rateData){
	const tableBody = document.querySelector('#dataTable tbody');
	tableBody.innerHTML = ''; // Clear the table body

	Object.keys(rateData).forEach(key => {
		//console.log("Key: ", key)
		//console.log("value: ", rateData[key])

		const row = document.createElement('tr');

		const countryCell = document.createElement('td');
		countryCell.textContent = symbol2country(key) + ' (' + key + ')';
		row.appendChild(countryCell);

		const rateCell = document.createElement('td');
		rateCell.textContent = rateData[key] / rateData['USD'];
		row.appendChild(rateCell);

		tableBody.appendChild(row);
	});
}
	
function symbol2country(symbol){
	var SC = '{"CAD":"CANADIAN DOLLAR","GBP": "BRITISH POUND","EUR": "EURO", "JPY": "JAPANESE YEN","CNY": "CHINESE YUAN","AUD": "AUSTRALIAN DOLLAR", "HKD": "HONG KONG DOLLAR","IDR": "INDONESIAN RUPIAH","MXN": "MEXICAN PESO","SGD": "SINGAPORE DOLLAR","KRW": "SOUTH KOREAN WON","THB": "THAI BAHT","TWD": "NEW TAIWAN DOLLAR","USD": "US DOLLAR"}'
	var oSC = JSON.parse(SC);
	
	return oSC[symbol];
}

// document.getElementById('fetchData').addEventListener('click', () => {

document.addEventListener('DOMContentLoaded', (event) => {
	getExchangeRates();
});