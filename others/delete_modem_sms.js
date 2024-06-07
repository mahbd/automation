var xhr = new XMLHttpRequest();
xhr.open('POST', 'http://192.168.0.1/goform/goform_set_cmd_process', true);
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) { // Done
        if (xhr.status === 200) { // OK
            console.log('Response received:', xhr.responseText);
        } else {
            console.error('Error occurred:', xhr.statusText);
        }
    }
};
var body = 'isTest=false&goformId=DELETE_SMS&msg_id=1480%3B1479%3B&notCallback=true';
xhr.send(body);
