//_________________________GET LIST____________________________

var idNum = 0

var getListFromServer = function(){
	  var request = new XMLHttpRequest();
	
	request.open("GET", "http://localhost:8080/windshields");
	request.send(null);

	
	
	request.onreadystatechange = function() {
		if (request.readyState === 4){
			if (request.status >= 200 && request.status < 400) {
				console.log(request.responseText);
				console.log(JSON.parse(request.responseText));
				var messages = JSON.parse(request.responseText);
				console.log(messages[0]);
				
				var list = document.getElementById("list");
					list.innerHTML = "";
				
				
				
				for(index in messages) {
						var obj = messages[index];
								
								var newListItem = document.createElement("p");
								newListItem.innerHTML = obj["id"] + ": " + obj["yearstart"] + "-" + obj["yearend"] + " " + obj["make"] + " " +  obj["model"] + " | Part Number: " +  obj["partnumber"] + " " +  obj["location"] + " | Cost: " +  obj["cost"] + " | Quantity: " +  obj["stock"];
						
								var list = document.getElementById("list");
								list.appendChild(newListItem);
					}
		
		
			} else {
				console.error("that didnt work...");
			}
		}
	};
		
};

var getButton = document.getElementById("getButton");
	getButton.onclick = function () {
	console.log("the GET button was clicked!");
	getListFromServer();
};


//_________________________GET ITEM_________________________________



var getItemFromServer = function(){
	  var request = new XMLHttpRequest();
	
	request.open("GET", "http://localhost:8080/windshields");
	request.send(null);

	
	
	request.onreadystatechange = function() {
		if (request.readyState === 4){
			if (request.status >= 200 && request.status < 400) {
				console.log(request.responseText);
				console.log(JSON.parse(request.responseText));
				var messages = JSON.parse(request.responseText);
				console.log(messages[0]);
				
				var list = document.getElementById("list");
					list.innerHTML = "";
				
				var userInput = document.getElementById("partNumSearchText");
				var inputValue = userInput.value;
				var data = "message=" + encodeURIComponent(inputValue);
				console.log(inputValue)
				
				for(index in messages) {
					var obj = messages[index];		
					if (obj["partnumber"] === inputValue) {						
						
						var newListItem = document.createElement("p");
						newListItem.innerHTML = obj["id"] + ": " + obj["yearstart"] + "-" + obj["yearend"] + " " + obj["make"] + " " +  obj["model"] + " | Part Number: " +  obj["partnumber"] + " " +  obj["location"] + " | Cost: " +  obj["cost"] + " | Quantity: " +  obj["stock"];
						
						var objId = obj["id"]
						console.log(objId)
						
						var deleteButton = document.getElementById("deleteButton");
						deleteButton.onclick = function () {
							
							var r = confirm("Are you sure you would like to delete this record?");
								if (r == true) {
									x = "You pressed OK!";
								} else {
									x = "You pressed Cancel!";
								}
							
						
							
							request.open("DELETE", "http://localhost:8080/windshields");
							request.send(data);
						}
						
						var list = document.getElementById("list");
						list.appendChild(newListItem);
							
					}
					}
			} else {
				console.error("that didnt work...");
			}
		}
	};
		
};

var SearchButton = document.getElementById("searchButton");
	searchButton.onclick = function () {
	console.log("the GET button was clicked!");
	getItemFromServer();
};



//_______________________DELETE_________________________________



var deleteItemFromServer = function(){
	var request = new XMLHttpRequest();
	
	request.onreadystatechange = function() {
		if (request.readyState === 4){
			if (request.status >= 200 && request.status < 400) {
				console.log("hey, something worked");
			} else {
				console.error("that didnt work...");
			}
		}
	};
	
	var userInput = document.getElementById("partNumDeleteText");
	var inputValue = userInput.value;
	var data = "message=" + encodeURIComponent(inputValue);
	
	request.open("DELETE", "http://localhost:8080/windshields");
	request.send(data);
};

var deleteButton = document.getElementById("deleteButton");
	deleteButton.onclick = function () {
	console.log("the DELETE button was clicked!");
	deleteItemFromServer();
	getListFromServer();
};

//___________________________CREATE_____________________________



var sendCreationToServer = function(){
	var request = new XMLHttpRequest();
	
	request.onreadystatechange = function() {
		if (request.readyState === 4){
			if (request.status >= 200 && request.status < 400) {
				console.log("hey, something worked");
			} else {
				console.error("that didnt work...");
			}
		}
	};
	
	var userInput1 = document.getElementById("crYearStart");
	var inputValue1 = userInput1.value;
	var userInput2 = document.getElementById("crYearEnd");
	var inputValue2 = userInput2.value;
	var userInput3 = document.getElementById("crMake");
	var inputValue3 = userInput3.value;
	var userInput4 = document.getElementById("crModel");
	var inputValue4 = userInput4.value;
	var userInput5 = document.getElementById("crPartNumber");
	var inputValue5 = userInput5.value;
	var userInput6 = document.getElementById("crLocation");
	var inputValue6 = userInput6.value;
	var userInput7 = document.getElementById("crCost");
	var inputValue7 = userInput7.value;
	var userInput8 = document.getElementById("crStock");
	var inputValue8 = userInput8.value;
	var data = "message=" + " " + encodeURIComponent(inputValue1, inputValue2) + " " + encodeURIComponent(inputValue2) + " " + encodeURIComponent(inputValue3) + " " + encodeURIComponent(inputValue4) + " " + encodeURIComponent(inputValue5) + " " + encodeURIComponent(inputValue6) + " " + encodeURIComponent(inputValue7) + " " + encodeURIComponent(inputValue8);
	
	console.log(data)
	
	request.open("POST", "http://localhost:8080/windshields");
	request.send(data);
};

var createButton = document.getElementById("createButton");
	createButton.onclick = function () {
	console.log("the CREATE button was clicked!");
	sendCreationToServer();
	getListFromServer();
};



//______________________MODIFY_____________________________

var sendModificationToServer = function(){
	  var request = new XMLHttpRequest();
	
	request.open("GET", "http://localhost:8080/windshields");
	request.send(null);

	
	
	request.onreadystatechange = function() {
		if (request.readyState === 4){
			if (request.status >= 200 && request.status < 400) {
				console.log(request.responseText);
				console.log(JSON.parse(request.responseText));
				var messages = JSON.parse(request.responseText);
				console.log(messages[0]);
				
				var list = document.getElementById("list");
					list.innerHTML = "";
				
				var userInput = document.getElementById("partNumUpdateText");
				var inputValue = userInput.value;
				var data = "message=" + encodeURIComponent(inputValue);
				console.log(inputValue)
				
				for(index in messages) {
					var obj = messages[index];		
					if (obj["partnumber"] === inputValue) {						
						
						document.getElementById("mdYearStart").value = obj["yearstart"];
						document.getElementById("mdYearEnd").value = obj["yearend"];
						document.getElementById("mdMake").value = obj["make"];
						document.getElementById("mdModel").value = obj["model"];
						document.getElementById("mdPartNumber").value = obj["partnumber"];
						document.getElementById("mdLocation").value = obj["location"];
						document.getElementById("mdCost").value = obj["cost"];
						document.getElementById("mdStock").value = obj["stock"];
						
						
						
						var userInput1 = document.getElementById("mdYearStart");
						var inputValue1 = userInput1.value;
						var userInput2 = document.getElementById("mdYearEnd");
						var inputValue2 = userInput2.value;
						var userInput3 = document.getElementById("mdMake");
						var inputValue3 = userInput3.value;
						var userInput4 = document.getElementById("mdModel");
						var inputValue4 = userInput4.value;
						var userInput5 = document.getElementById("mdPartNumber");
						var inputValue5 = userInput5.value;
						var userInput6 = document.getElementById("mdLocation");
						var inputValue6 = userInput6.value;
						var userInput7 = document.getElementById("mdCost");
						var inputValue7 = userInput7.value;
						var userInput8 = document.getElementById("mdStock");
						var inputValue8 = userInput8.value;
						var data = "message=" + " " + encodeURIComponent(inputValue1, inputValue2) + " " + encodeURIComponent(inputValue2) + " " + encodeURIComponent(inputValue3) + " " + encodeURIComponent(inputValue4) + " " + encodeURIComponent(inputValue5) + " " + encodeURIComponent(inputValue6) + " " + encodeURIComponent(inputValue7) + " " + encodeURIComponent(inputValue8);
	
						
						var modifyButton = document.getElementById("modifyButton");
						modifyButton.onclick = function () {
							
							var messages = JSON.parse(request.responseText);
							
							for(index in messages) {
								var obj = messages[index];		
								if (obj["partnumber"] === inputValue) {
									
									
									var userInput1 = document.getElementById("mdYearStart");
									var inputValue1 = userInput1.value;
									var userInput2 = document.getElementById("mdYearEnd");
									var inputValue2 = userInput2.value;
									var userInput3 = document.getElementById("mdMake");
									var inputValue3 = userInput3.value;
									var userInput4 = document.getElementById("mdModel");
									var inputValue4 = userInput4.value;
									var userInput5 = document.getElementById("mdPartNumber");
									var inputValue5 = userInput5.value;
									var userInput6 = document.getElementById("mdLocation");
									var inputValue6 = userInput6.value;
									var userInput7 = document.getElementById("mdCost");
									var inputValue7 = userInput7.value;
									var userInput8 = document.getElementById("mdStock");
									var inputValue8 = userInput8.value;
									var data = "message=" + " " + encodeURIComponent(inputValue1, inputValue2) + " " + encodeURIComponent(inputValue2) + " " + encodeURIComponent(inputValue3) + " " + encodeURIComponent(inputValue4) + " " + encodeURIComponent(inputValue5) + " " + encodeURIComponent(inputValue6) + " " + encodeURIComponent(inputValue7) + " " + encodeURIComponent(inputValue8);
								}
							}
									
							
						console.log("the UPDATE button was clicked!");
						request.open("PUT", "http://localhost:8080/windshields");
						request.send(data);
						};
 
						
						
					}
					}
			} else {
				console.error("that didnt work...");
			}
		}
	};
		
};

var updateButton = document.getElementById("updateButton");
	updateButton.onclick = function () {
	console.log("the UPDATE button was clicked!");
	sendModificationToServer();
};










