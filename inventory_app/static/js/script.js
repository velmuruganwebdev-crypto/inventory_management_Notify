const ws = new WebSocket('ws://' + window.location.host + '/ws/inventory/');

ws.onmessage = function(e) {
    const data = JSON.parse(e.data);
    alert(data.message);  // this popup
};
